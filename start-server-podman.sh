#
# Marek Martofel, Red Hat
#
# Run Llama server
#

podman run \
   --name llama-server \
   -d \
   -p 8000:8000 \
   quay.io/mmartofe/llama-server

