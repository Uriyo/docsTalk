from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
# from langchain.llms import OpenAI
from langchain_community.llms import OpenAI

def build_faiss(chunks,persist_path="faiss_index"):
    embeds=OpenAIEmbeddings()
    db=FAISS.from_documents(chunks,embeds)
    db.save_local(persist_path)
    return db

def load_faiss(persist_path="faiss_index"):
    embeds=OpenAIEmbeddings()

    return FAISS.load_local(
        persist_path,
        embeds,
        allow_dangerous_deserialization=True, 
    )

    
def make_qa(db, k=3):
    retriever = db.as_retriever(search_kwargs={"k": k})
    llm = OpenAI(temperature=0)
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )




