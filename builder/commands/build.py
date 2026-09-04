from subprocess import run

def cmd(args):
    run(["docker", "buildx", "build",
        "-f", args.file,
        "-t", f"localhost/thethinnestimage/{args.name}:{args.tag}",
        "--cache-from", "type=gha",
        "--cache-to", "type=gha,mode=max",
        "--load",
        args.context],
        check=True)