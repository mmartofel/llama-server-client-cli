mkdir -p ~/minio/data

podman run \
   -p 9000:9000 \
   -p 9001:9001 \
   -v ~/minio/data:/data \
   -e "MINIO_ROOT_USER=minio" \
   -e "MINIO_ROOT_PASSWORD=minio123" \
   quay.io/minio/minio server /data --console-address ":9001"

