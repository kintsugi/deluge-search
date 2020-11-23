import os
import re
from pathlib import Path

import click


class Torrent:
    def __init__(self, id, torrent_data={}):
        self.id = id.decode("utf-8")

        if not torrent_data["name"]:
            raise ValueError("invalid torrent, no name")

        if not torrent_data["save_path"]:
            raise ValueError("invalid torrent, no name")

        for key in torrent_data:
            setattr(self, key, torrent_data[key])

        self.file_path = str(
            Path(os.path.join(torrent_data["save_path"], torrent_data["name"]))
        )

    def print(self):
        torrent_data = self.__dict__
        for key in torrent_data:
            click.echo(f"{key}: {torrent_data[key]}")
        click.echo()
