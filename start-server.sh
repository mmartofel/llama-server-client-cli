
cd ./venv
source bin/activate

python -m llama_cpp.server --host 0.0.0.0 --model ./model/Meta-Llama-3-8B-Instruct.Q2_K.gguf --n_ctx 2048

