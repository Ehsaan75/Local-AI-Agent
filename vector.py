from langchain_ollama import OllamaEmbeddings # type: ignore
from langchain_chroma import Chroma # type: ignore
from langchain_core.documents import Document
import os
import pandas as pd # type: ignore

df = pd.read_csv("workouts.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")
db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        def safe_str(val):
            return str(val) if pd.notnull(val) else ""
        document = Document(
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

vector_store = Chroma(
    collection_name="workouts",
    persist_directory=db_location,
    embedding_function=embeddings,
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 50} # Adjust the number of workouts to retrieve as needed
)