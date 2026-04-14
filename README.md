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

### Property-guided Fuzzing on Matrix

Before actually get into fuzzing, you need to configure RESTler for your Matrix Synapse. This include several things you need to take care of.

#### Authentication Token

To make valid requests to Matrix Synapse, you need to configure RESTler with a valid authentication token. The steps are:

1. Manually create an account on your Matrix Synapse server. This can be done by sending a `POST` request to the `/_matrix/client/r0/register` endpoint. Alternatively, you can create an admin account using the admin API. For more details on registration, refer to the [official documentation](https://spec.matrix.org/latest/).
2. Log in to the newly created account by sending a `POST` request to the `/_matrix/client/v3/login` endpoint. Upon successful login, Matrix Synapse will return an authentication token.
3. Paste the authentication token into `restler-synapse/mydata/authentication_token.txt`. RESTler is configured to read this token from `restler-synapse/restler-work/Compile/engine_settings.json`.

#### Specification Files

There are three specification files can be found in `restler-synapse/mydata/`. 

1. `api.full.json` is the full specification file downloaded from [Matrix official Client-Server API specification](https://spec.matrix.org/latest/client-server-api/api.json). You can still fuzz it if you wish, but you will likely to get extremely low coverage and lots of noise. Dependencies are not resolved for this file, so RESTler cannot perform valid API sequences.
2. `api.large.json` is the large specification file

---

### FAQ

#### Error Not Authenticated

#### Can I change my time budget?

#### False Positive
