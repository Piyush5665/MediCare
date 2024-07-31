import os
from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain_community.vectorstores import pinecone 
from pinecone import Pinecone as PC,ServerlessSpec
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

# print(PINECONE_API_KEY)
# print(PINECONE_API_ENV)

pc = PC(api_key=os.environ.get("PINECONE_API_KEY"))

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

index_name="quickstart"

#Initializing the Pinecone
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536, # Replace with your model dimensions
        metric="cosine", # Replace with your model metric
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ) 
    )




#Creating Embeddings for Each of The Text Chunks & storing
docsearch=PC.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)
