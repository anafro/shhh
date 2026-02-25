# Shhh

**Shhh** is a dead simple secret accessor, that retrieves environment
secrets, and secrets from files.

## Installation

To install Shhh, use:

```bash
pip install shhh
```

With Poetry, do:

```bash
poetry add shhh
```

## Usage

The only function is **Shhh** is `get_secret`.
It returns an environment variable, unless a file exists on path provided in `XXX_FILE` variable.
For example:

```py
username: str = get_secret("APP_USERNAME")
```

**Shhh** searches for a file on path provided in `APP_USERNAME_FILE` variable and, if it exists,
returns its content. Otherwise, returns the value of `APP_USERNAME` variable.

## License

**Shhh** is licensed under MIT.

------------------
Copyright (c) 2026 Anatoly Frolov (anafro). All Rights Reserved.\
`contact@anafro.ru`
