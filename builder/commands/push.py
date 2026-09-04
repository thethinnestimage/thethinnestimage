from subprocess import run

def cmd(args):
    run(["docker", "tag", 
        f"localhost/thethinnestimage/{args.name}:{args.tag}",
        f"{args.registry}/{args.namespace}/{args.name}:{args.tag}"],
        check=True)

    run(["docker", "push",
        f"{args.registry}/{args.namespace}/{args.name}:{args.tag}"],
        check=True)