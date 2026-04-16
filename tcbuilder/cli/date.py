"""
CLI handling for images subcommand
"""

from tcbuilder.backend import date


PROV_MODE_OFFLINE = "offline"
PROV_MODE_ONLINE = "online"
PROV_MODES = (PROV_MODE_OFFLINE, PROV_MODE_ONLINE)


def do_date():
    """Run 'date' subcommand"""

    date.date()


def init_parser(subparsers):
    """Initialize 'date' subcommands command line interface."""

    parser = subparsers.add_parser(
        "date",
        help="Return the current date/time of the system.",
        allow_abbrev=False)

    parser.add_argument("--remove-storage", dest="remove_storage", action="store_true",
                        help="""Automatically clear storage prior to unpacking a new Easy
                        Installer image.""")
    parser.set_defaults(func=do_date)
