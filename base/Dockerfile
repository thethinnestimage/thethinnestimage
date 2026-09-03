# FROM ubuntu:24.04 AS bootstrap

FROM thethinnestimage/base AS bootstrap

RUN --mount=type=cache,target=/var/cache/apt,id=thethinnestimage-apt-cache \
    --mount=type=cache,target=/var/lib/apt,id=thethinnestimage-apt-lib-cache \
    --mount=type=bind,source=shared/scripts/apt-install.sh,target=/tmp/apt-install.sh \
    sh /tmp/apt-install.sh debootstrap

RUN --mount=type=cache,target=/var/cache/debootstrap,id=thethinnestimage-debootstrap-cache \
    debootstrap \
        --variant=minbase \
        --components=main,universe \
        # --include=debootstrap \
        --cache-dir=/var/cache/debootstrap \
        --merged-usr \
        --force-check-gpg \
        --log-extra-deps \
        noble \
        rootfs \
        http://archive.ubuntu.com/ubuntu/

FROM scratch

COPY --from=bootstrap /rootfs /