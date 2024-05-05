#
# Marek Martofel, Red Hat
#
# Run Open WebUI (Formerly Ollama WebUI), check their repo at:
# https://github.com/open-webui/open-webui
#

podman run -d \
   -p 8080:8080 \
   -e OLLAMA_BASE_URL=http://host.containers.internal:11434 \
   -v ollama-webui:/app/backend/data \
   --name ollama-webui \
   --restart always ghcr.io/ollama-webui/ollama-webui:main
