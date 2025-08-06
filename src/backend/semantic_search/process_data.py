# System imports
from glob import glob
import os
from uuid import uuid4

# Third-party imports
import faiss
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_core.documents import Document
import torch
from tqdm import tqdm

class VectorStoreCreator:
    """Configuration class for semantic search."""
    def __init__(self):
        self.embedding_model = "sentence-transformers/all-MiniLM-L6-v2"
        self.vector_store_path = "vector_store"
        self.folder_path = "/Users/ha/Downloads/mirrulations/specific/" # Folder path with all HTM files
    
    def get_embedding_model(self):
        return self.embedding_model
    
    def get_vector_store_path(self):
        return self.vector_store_path
    
    def load_vector_store(self):
        """Load the vector store from the specified path."""
        return FAISS.load_local(self.vector_store_path, HuggingFaceEmbeddings(model_name=self.embedding_model))
    
    def save_vector_store(self, vector_store):
        """Save the vector store to the specified path."""
        vector_store.save_local(self.vector_store_path)
        
    def get_device(self):
        """Determine the device to use for embeddings."""
        if torch.cuda.is_available():
            return "cuda"
        elif torch.backends.mps.is_available():
            return "mps"
        else:
            return "cpu"
        
    def load_embeddings(self):
        """Load the embeddings model."""
        return HuggingFaceEmbeddings(
            model_name=self.embedding_model,
            model_kwargs={"device": self.get_device()}
        )
    def process_and_create_vector_store(self):
        """Process the data and create the vector store."""
        embeddings = self.load_embeddings()
        index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))
        
        vector_store = FAISS(
            embedding_function=embeddings,
            index=index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={},
        )
        
        folders = os.listdir(self.folder_path)
        
        for fold in folders:
            for com_file in tqdm(glob(self.folder_path), desc=f"Processing files in {fold}"):
                with open(com_file, "r") as file:
                    text = file.read().lower()
                    vector_store.add_documents(
                        documents=[Document(page_content=text, metadata={"source": com_file})],
                        ids=[str(uuid4())],
                    )

        vector_store.save_local(self.vector_store_path)