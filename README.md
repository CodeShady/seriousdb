![seriousdb logo](https://i.imgur.com/ztPW7ZI.png)

# seriousdb - A seriously simple database

<div align="center">

[![Tests](https://github.com/danieldeer/seriousdb/actions/workflows/tests.yml/badge.svg)](https://github.com/danieldeer/seriousdb/actions/workflows/tests.yml)
[![Lint](https://github.com/danieldeer/seriousdb/actions/workflows/lint.yml/badge.svg)](https://github.com/danieldeer/seriousdb/actions/workflows/lint.yml)
[![Typecheck](https://github.com/danieldeer/seriousdb/actions/workflows/typecheck.yml/badge.svg)](https://github.com/danieldeer/seriousdb/actions/workflows/typecheck.yml)
[![Version](https://img.shields.io/badge/dynamic/regex?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdanieldeer%2Fseriousdb%2Fmain%2FVERSION&search=(.%2B)&label=version)](https://github.com/danieldeer/seriousdb/blob/main/VERSION)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://github.com/danieldeer/seriousdb)
[![License](https://img.shields.io/github/license/danieldeer/seriousdb)](https://github.com/danieldeer/seriousdb/blob/main/LICENSE)
[![Stars](https://img.shields.io/github/stars/danieldeer/seriousdb)](https://github.com/danieldeer/seriousdb/stargazers)
[![Forks](https://img.shields.io/github/forks/danieldeer/seriousdb)](https://github.com/danieldeer/seriousdb/network/members)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-blueviolet?logo=github)](https://github.com/danieldeer/seriousdb)

</div>

`seriousdb` is a small, simple key-value database you can query directly over HTTP. It requires zero configuration and is designed to be effortless.
For fullstack projects, `seriousdb` can replace your complete backend.

For setup, usage, architecture, persistence, and contribution guidance, see the [documentation](docs/).

## Quick Start

### Use as Python library

Install using

- pip:
```bash
pip install git+https://github.com/danieldeer/seriousdb.git
```
Or
- uv:
```bash
uv add git+https://github.com/danieldeer/seriousdb.git
```

Then use it directly form your python project:

```python
import seriousdb

seriousdb.set("name", "Alice")
print(seriousdb.get("name"))
```

### Run as HTTP server

Clone the repository, install the project, and start the development server:

```bash
git clone https://github.com/danieldeer/seriousdb.git
cd seriousdb
uv sync
uv run run.py
```

The server is available at `http://127.0.0.1:8000`.

> To change the default IP and PORT, define the environment variables `APP_HOST` and `APP_PORT` to your preferred values.

Interactive API documentation is available at:

- [Swagger UI](http://127.0.0.1:8000/docs)
- [ReDoc](http://127.0.0.1:8000/redoc)
- [OpenAPI schema](http://127.0.0.1:8000/openapi.json)

## Configuration

Server configuration is optional and can be customized from environment variables.
Copy the example file and adjust for local development:

```bash
cp .env.example .env
```

The `.env` file is gitignored and should never be committed.

| Variable              | Default     | Description                                        |
| --------------------- | ----------- | -------------------------------------------------- |
| `SERIOUSDB_DB_FILE`   | `.sdb`      | Path to the on-disk database file.                 |
| `SERIOUSDB_LOG_LEVEL` | `INFO`      | Logging level (DEBUG/INFO/WARNING/ERROR/CRITICAL). |
| `SERIOUSDB_HOST`      | `127.0.0.1` | Host IP where the API is running.                  |
| `SERIOUSDB_PORT`      | `8000`      | Host port which is used by the API.                |

## Documentation

- [API reference](docs/api.md)
- [Architecture](docs/architecture.md)
- [Development guide](docs/development.md)
- [Persistence](docs/persistence.md)
- [Contributing](docs/contributing.md)
- [Testing](docs/testing.md)
- [Project configuration](docs/configuration.md)

## License

This project is licensed under the [MIT License](LICENSE).
