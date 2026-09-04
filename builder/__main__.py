from pathlib import Path
from argparse import ArgumentParser

from .commands import build, push, login, sign

ROOT_DIR = Path(__file__).resolve().parent.parent

def path(value: str) -> Path:
    path = Path(value)
    return (ROOT_DIR / path).resolve()

def main():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    build_parser = subparsers.add_parser("build")
    build_parser.set_defaults(handler=build.cmd)
    build_parser.add_argument("-c", "--context", type=path, default=ROOT_DIR)
    build_parser.add_argument("-f", "--file", type=path, required=True)
    build_parser.add_argument("-n", "--name", required=True)
    build_parser.add_argument("-t", "--tag", default="latest")

    push_parser = subparsers.add_parser("push")
    push_parser.set_defaults(handler=push.cmd)
    push_parser.add_argument("-r", "--registry", required=True)
    push_parser.add_argument("-ns", "--namespace", default="thethinnestimage")
    push_parser.add_argument("-n", "--name", required=True)
    push_parser.add_argument("-t", "--tag", default="latest")

    login_parser = subparsers.add_parser("login")
    login_parser.set_defaults(handler=login.cmd)
    login_parser.add_argument("-r", "--registry", required=True)
    login_parser.add_argument("-u", "--username", default="thethinnestimage")
    login_parser.add_argument("-p", "--password", required=True)

    sign_parser = subparsers.add_parser("sign")
    sign_parser.set_defaults(handler=sign.cmd)
    sign_parser.add_argument("-r", "--registry", required=True)   
    sign_parser.add_argument("-ns", "--namespace", default="thethinnestimage")
    sign_parser.add_argument("-n", "--name", required=True)
    sign_parser.add_argument("-t", "--tag", default="latest")

    args = parser.parse_args()
    args.handler(args)

if __name__ == "__main__":
    main()