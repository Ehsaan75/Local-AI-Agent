from langchain_ollama import OllamaEmbeddings # type: ignore
from langchain_chroma import Chroma # type: ignore
from langchain_core.documents import Document
import os
import pandas as pd # type: ignore

# Load workout data from CSV
df = pd.read_csv("workouts.csv")

# Initialize Ollama embedding model
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Set database location for Chroma vector store
db_location = "./chroma_langchain_db"

# Check if documents need to be added (only if DB doesn't exist)
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    # Iterate through each workout row and create a Document object
    for i, row in df.iterrows():
        def safe_str(val):
            return str(val) if pd.notnull(val) else ""
        document = Document(
            # Combine relevant fields for semantic search
            page_content=(
                safe_str(row["description"]) + " " +
                safe_str(row["exercise_title"]) + " " +
                safe_str(row["exercise_notes"]) + " " +
                safe_str(row["set_type"]) + " " +
                safe_str(row["weight_kg"]) + " " +
                safe_str(row["reps"]) + " " +
                safe_str(row["distance_km"]) + " " +
                safe_str(row["rpe"]) + " " +
                safe_str(row["duration_seconds"])
            ),
            # Add metadata for filtering and context
            metadata={
                "title": safe_str(row["title"]),
                "start_time": safe_str(row["start_time"]),
                "end_time": safe_str(row["end_time"]),
                "superset_id": safe_str(row["superset_id"]),
                "set_index": safe_str(row["set_index"])
            },
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

# Initialise Chroma vector store
vector_store = Chroma(
    collection_name="workouts",
    persist_directory=db_location,
    embedding_function=embeddings,
)

# Add documents to the vector store if needed
if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

# Create a retriever for semantic search over workout data
retriever = vector_store.as_retriever(
    search_kwargs={"k": 30} # Adjust the number of workouts to retrieve as needed
)