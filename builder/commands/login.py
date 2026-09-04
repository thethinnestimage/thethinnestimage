from subprocess import run

def cmd(args):
    run(["docker", "login",
        args.registry,
        "-u", args.username,
        "--password-stdin",
        ], input=args.password.encode(), check=True)