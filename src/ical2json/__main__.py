usage = """
Transform ical files to json

Usage:
  ical2json --url <url>
  ical2json -h | --help

Options:
  -h --help     Show this screen.
  --url=<url>   The URL of the ical file
"""

from docopt import docopt
from . import calendar
import json
import sys


def main():
    args = docopt(usage)

    if args["--help"]:
        print(usage)
        sys.exit(0)

    print(
        json.dumps(
            calendar.to_jsonable(calendar.from_url(args["--url"])),
            indent=4,
            ensure_ascii=False,
        )
    )
    sys.exit(0)
