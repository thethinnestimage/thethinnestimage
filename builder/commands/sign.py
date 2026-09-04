from subprocess import run
COSIGN_VERSION = "3.1.3"

def cmd(args):
    digest = run(["docker", "image", "inspect", "--format={{index .RepoDigests 0}}",
        f"{args.registry}/{args.namespace}/{args.name}:{args.tag}"], capture_output=True, text=True, check=True)

    digest = digest.stdout.strip().split("@")[1]

    run(["go", "run",
        f"github.com/sigstore/cosign/v{COSIGN_VERSION.split(".")[0]}/cmd/cosign@v{COSIGN_VERSION}",
        "sign", "--yes", f"{args.registry}/{args.namespace}/{args.name}@{digest}"],
        check=True)