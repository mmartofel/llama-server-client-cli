# FROM registry.fedoraproject.org/f33/python3
FROM python:3.10

# Add application sources with correct permissions for OpenShift
USER 0
ADD requirements.txt .

# Create model directory
RUN mkdir -p model
ADD ./venv/model/Meta-Llama-3-8B-Instruct.Q2_K.gguf ./model

RUN chown -R 1001:0 ./
USER 1001

# Install the dependencies
RUN pip install -U "pip>=19.3.1" && \
    pip install -r requirements.txt

# Run the application
CMD python -m llama_cpp.server --host 0.0.0.0 --model ./model/Meta-Llama-3-8B-Instruct.Q2_K.gguf --n_ctx 2048 
