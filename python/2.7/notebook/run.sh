#!/bin/bash

# Reference: https://github.com/ipython/docker-notebook/blob/266cc06f7bcb348c6a0e0527fb4e593fe35387b9/notebook/notebook.sh

# Strict mode
set -euo pipefail
IFS=$'\n\t'

# Set configuration defaults
: ${PASSWORD:=""}
: ${PEM_FILE:="/key.pem"}

# Create a self signed certificate for the user if one doesn't exist
if [ ! -f $PEM_FILE ]; then
  openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout $PEM_FILE -out $PEM_FILE \
    -subj "/C=XX/ST=XX/L=XX/O=dockergenerated/CN=dockergenerated"
  : ${CERTFILE_OPTION="--certfile=$PEM_FILE"}
fi

# Create the hash to pass to the IPython notebook, but don't export it so it doesn't appear
# as an environment variable within IPython kernels themselves
HASH=$(python2.7 -c "from IPython.lib import passwd; print(passwd('${PASSWORD}'))")
unset PASSWORD

jupyter notebook --no-browser --port 8888 --ip=* --certfile=$PEM_FILE --NotebookApp.password="$HASH"
