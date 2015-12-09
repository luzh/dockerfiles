# Dockerfiles

My Dockerfiles

## CentOS

This directory contains Dockerfiles for building images based on CentOS.

```
.
└── 7                # customized CentOS 7 image
```

## Python

This directory contains Dockerfiles for building images based on CentOS 7 that run Python for different purposes.

```
.
└── 2.7
    ├── baseline     # baseline image that contains python and pip
    ├── numerical    # baseline + numpy + scipy
    └── imaging      # baseline + numpy + scipy + pillow + matplotlib
    └── wxpython     # baseline + numpy + scipy + pillow + matplotlib + wxpython 
```

To run GUI applications (e.g. Python with interactive plotting) in docker, first create a non-root user in the docker image. 
The image/container user name should be the same as the $USER that will run the container on the host machine. The uid/gid
of the user in container should also be identical to the one on the host; otherwise `usermod` and `groupmod` commands are
needed to alter them.

Refer to `python/2.7/Makefile` for building an image "python" with a regular user.

Next give only containers of $USER permission to access the X11 socket on the local host machine, and run a container with
mounted X11 socket and explicitly specified user name.

```
xhost +si:localuser:$USER
docker run -it --rm -e DISPLAY=$DISPLAY -u $USER -v /tmp/.X11-unix:/tmp/.X11-unix -v $PWD:$PWD -w $PWD --entrypoint=/bin/bash python
xhost -si:localuser:$USER
```

The run-time `-u` or `--user` option can be skipped if the image's Dockerfile already sets a user name using `USER`.
