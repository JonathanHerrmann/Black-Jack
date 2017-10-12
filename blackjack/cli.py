import argparse


def get_parser():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="cmd")

    server = subparser.add_parser("serve", description="Start a blackjack game server")
    client = subparser.add_parser("join", description="Join a blackjack server")

    client.add_argument("server", type=str, help="The server to join")


def main():
    parser = get_parser()
    options = parser.parse_args()
    if not options.cmd:
        parser.print_help()

    if options.cmd == "server":
        with BlackjackServer()
