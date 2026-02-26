from os import environ as env
from pathlib import Path


def get_secret(name: str) -> str:
    if name in env:
        return env[name]

    filename_env_key: str = f"{name}_FILE"

    if filename_env_key in env:
        environment_secret_filepath: Path = Path(env[filename_env_key])
        if (
            not environment_secret_filepath.exists()
            or not environment_secret_filepath.is_file()
        ):
            raise ValueError(
                f"{filename_env_key} is provided, but that file not found (that path hidden for security purposes).\nDid you forget to provide that file via docker volumes, for example?"
            )

        with open(environment_secret_filepath, "r") as secret_file:
            return secret_file.read()

    raise ValueError(
        f"Neither {name}, nor {filename_env_key} is present in environment variables."
    )
