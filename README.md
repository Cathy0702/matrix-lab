# matrix-lab

This is a course project for CPSC538P. In this project, we perform property-guided fuzzing using [RESTler](https://github.com/microsoft/restler-fuzzer), a stateful REST API fuzzer developed by Microsoft, on the [Matrix Synapse homeserver](https://github.com/element-hq/synapse). The idea is inspired by [previous work](https://ieeexplore.ieee.org/document/9159084), where a set of security properties is defined. We instantiate these high-level properties into Matrix API sequences and use custom RESTler checkers to probe for violations of expected behaviors.

The security properties and corresponding API sequences we focus on are:

- **Use-after-free rule**
  - A user should not be able to read the content of a message after it has been removed (redacted).
  - A user should not be able to interact with a room that has been effectively deleted.
- **Resource-hierarchy rule**
  - A user should not be able to send messages to a room they are not in (*a message [child resource] is properly constrained by the room [parent resource]*).

This repository contains our artifacts, including filtered Matrix API specification files and an extended version of the RESTler fuzzer. Note that due to the inherent randomness of fuzzing, results may vary across runs.

---

### Set up Matrix Synapse

Matrix Synapse should be set up following the [official documentation](https://element-hq.github.io/synapse/latest/setup/installation.html). We recommend using [Docker](https://hub.docker.com/r/matrixdotorg/synapse), as it is relatively easier to configure. Once Synapse is set up, you should be able to run:

```
curl -s http://your.matrix.homeserver/_matrix/client/versions
```
and receive a valid response.

#### Rate Limiting

Since we are performing fuzzing tests, it is important for the Matrix Synapse server to accept a large number of requests without rate limiting. Synapse allows users to configure rate limits in `homeserver.yaml`. An example configuration is provided in `synapse-data/homeserver.yaml`, where rate limiting is effectively disabled by setting all limits to large values.

You can copy the relevant configurations into your own `homeserver.yaml`. **Note:** this setup is intended for experimental purposes only.

---

### Set up RESTler

This repository provides an extended version of RESTler that includes custom checkers tailored to Matrix Synapse and our filtered API specification files. We recommend using `docker build` for setup.

To build RESTler, clone this repository to your local machine, navigate to the `restler-fuzzer` directory, and run:

```
docker build -t restler .
```

---

### Configuration

Before actually get into fuzzing, you need to configure RESTler for your Matrix Synapse. This include several things you need to take care of.

#### Authentication Token

To make valid requests to Matrix Synapse, you need to configure RESTler with a valid authentication token. The steps are:

1. Manually create an account on your Matrix Synapse server. This can be done by sending a `POST` request to the `/_matrix/client/r0/register` endpoint. Alternatively, you can create an admin account using the admin API. For more details on registration, refer to the [official documentation](https://spec.matrix.org/latest/).
2. Log in to the newly created account by sending a `POST` request to the `/_matrix/client/v3/login` endpoint. Upon successful login, Matrix Synapse will return an authentication token.
3. Paste the authentication token into `restler-synapse/mydata/authentication_token.txt`. RESTler is configured to read this token from `restler-synapse/restler-work/Compile/engine_settings.json`.

#### Specification Files

Three specification files can be found in `restler-synapse/mydata/`:

1. `api.full.json` is the full specification file downloaded from the [official Matrix Client-Server API specification](https://spec.matrix.org/latest/client-server-api/api.json). You can still fuzz using this file, but you will likely observe extremely low coverage and a large amount of noise. Dependencies are not resolved, so RESTler cannot generate valid API sequences.
2. `api.large.json` is a partially filtered version of `api.full.json`. It includes some resolved dependencies. Fuzzing with this file may produce many `5xx` errors, and will result in few custom checker invocations.
3. `api.min.json` is a small specification file tailored to the API sequences used in our experiments. Dependencies are resolved for the selected endpoints.

To **switch between specification files**, modify the `SwaggerSpecFilePath` field in `restler-synapse/restler-work/Compile/config.json`.

---

### Property-guided Fuzzing

At this stage, the configuration is done, and you are ready to do the actual fuzzing. We provide a script, `restler-synapse/run.sh`, to make this process easier. 

#### Compilation

Compilation is performed by running:

```
./run.sh compile
```

This step generates files containing information about the API grammar, dependencies, and other metadata required for fuzzing. The generated files are located in `restler-synapse/restler-work/Compile/`. For more details, refer to the RESTler [official documentation](https://github.com/microsoft/restler-fuzzer/tree/main/docs/user-guide).

**Important:** A successful compilation may overwrite `restler-synapse/restler-work/Compile/engine_settings.json` with default settings, which removes the `authentication` field. You will need to add it back manually; otherwise, RESTler will return a "Not Authenticated" error.

#### Test

Testing is performed by running:

```
./run.sh test
```

This step executes a lightweight run over each endpoint in the selected specification file. The resulting files are stored in `restler-synapse/restler-work/Test/`.

#### Fuzz

Fuzzing is performed by running:

```
./run.sh fuzz
```

The results are stored in `restler-synapse/restler-work/Fuzz/`. For a complete description of output files, refer to the RESTler official documentation. Few interesting files and directories include:

1. `RestlerResults/experimentXX/logs/network.testing.*.txt`  
   These logs record all activity during fuzzing, including generated request sequences and checker invocations.  
   **Note:** These files can grow very quickly in size.
2. `RestlerResults/experimentXX/logs/*Checker.*.txt`  
   Checker-specific logs that are useful for analyzing and counting checker invocations.
3. `RestlerResults/experimentXX/bug_buckets/`  
   This directory contains potential violations identified by checkers. RESTler automatically replays these cases to test for reproducibility.

---

### Auxiliary Script

The repository includes `analyze.py`, a script used to analyze RESTler log files and evaluate checker invocations.

To run the analysis:

```
python3 ./analyze.py [network.testing.*.txt ...]
```
The arguments should be the paths to `network.testing.*.txt` log files from a single fuzzing run, provided **in sequence**. 

By analyzing these logs, the script reports both the expected and actual number of checker invocations.

---

### FAQ

#### I got a "Not Authenticated" error!

This usually means something went wrong in `restler-synapse/restler-work/Compile/engine_settings.json`. Check that the `authentication` field is present, especially after running compilation, which may overwrite `engine_settings.json` with default settings.

#### Can I change the time budget?

Yes! The time budget controls how long fuzzing runs. You can change it by modifying `restler-synapse/run.sh`.

#### I changed the specification file, but RESTler is still using the old one!

After updating `restler-synapse/restler-work/Compile/config.json`, you need to recompile by running `./run.sh compile`.

#### My InvalidDynamicObjectChecker reports bugs?!

Yeah… we’ve seen that too :(. It’s likely a **false positive**. Matrix is quite tolerant with some inputs, RESTler tries to generate what it considers an "invalid txnid", but Matrix often accepts almost any character.
