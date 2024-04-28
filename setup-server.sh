
python3 -m venv venv
cd ./venv
source bin/activate

# https://github.com/abetlen/llama-cpp-python
pip install llama-cpp-python
pip install openai
pip install uvicorn

mkdir model
cd model

# https://huggingface.co/QuantFactory/Meta-Llama-3-8B-Instruct-GGUF/tree/main?source=post_page-----a563c6a47f49--------------------------------

wget https://huggingface.co/QuantFactory/Meta-Llama-3-8B-Instruct-GGUF/resolve/main/Meta-Llama-3-8B-Instruct.Q2_K.gguf

cd ..

