# MediCare
<b> MediCare is an advanced AI-powered medical chatbot designed to provide accurate, context-aware responses to complex medical queries. Leveraging cutting-edge language models and efficient data retrieval systems, it offers users instant access to reliable medical information, enhancing healthcare accessibility and support. This intelligent system aims to bridge the gap between patients and medical knowledge, providing a user-friendly interface for health-related inquiries.


## How to run?
## Steps:

#### • Clone the repository:

```bash
Project repo: https://github.com/
```
<br>

#### • Create a conda environment after opening the repository:

```bash
conda create -n mchatbot python=3.8 -y
```

```bash
conda activate mchatbot
```
<br>

#### • Install the requirements:
```bash
pip install -r requirements.txt
```

<br>

#### • Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

<br>

#### • Download the quantized model from the link provided in the model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model:
llama-2-7b-chat.ggmlv3.q4_0.bin

## from the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```

```bash
# run the following command
python store_index.py
```

```bash
# finally run the following command
python app.py
```
<br>

#### • Now,
```bash
open up localhost
```
<br>


## Techstack 

- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone


