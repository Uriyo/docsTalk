# main.py
import os
from rich import print
from ingest import load_docs, chunk_docs
from qa import build_faiss, load_faiss, make_qa

INDEX_DIR = "faiss_index"

def ensure_index():
    if os.path.exists(INDEX_DIR):
        return load_faiss(INDEX_DIR)
    print("[yellow]Building FAISS index… this may take a minute[/]")
    docs = load_docs()
    chunks = chunk_docs(docs)
    db = build_faiss(chunks, INDEX_DIR)
    print("[green]Index built![/]")
    return db

def chat_loop(qa_chain):
    print("[bold green]Welcome to ChaiDocs RAG![/]")
    print("Type your question, or `exit` to quit.\n")
    while True:
        query = input("[cyan]> [/]")
        if query.lower().strip() in ("exit", "quit"):
            break
        res = qa_chain(query)
        print("\n[bold]Answer:[/]", res["result"])
        print("\n[dim]Sources:[/]")
        for doc in res["source_documents"]:
            src = doc.metadata.get("source")
            chunk = doc.metadata.get("chunk_id")
            print(f" • {src} [chunk {chunk}]")
        print()

def main():
    db = ensure_index()
    qa_chain = make_qa(db)
    chat_loop(qa_chain)

if __name__ == "__main__":
    main()


