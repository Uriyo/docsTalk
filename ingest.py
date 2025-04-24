import requests
from bs4 import BeautifulSoup
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

BASE_URL= "https://chaidocs.vercel.app"

def fetch_toc():
    """Scrape the Youtube track sidebar and return all relative URLs"""
    r=requests.get(f"{BASE_URL}/youtube/getting-started")
    soup=BeautifulSoup(r.text,"html.parser")

    sidebar=soup.select_one("nav") #adjust slector
    hrefs = [a.get("href") for a in sidebar.select("a") if a.get("href")]

    seen = set()
    toc=[]
    for href in hrefs:
        if href.startswith("/youtube/") and href not in seen:
            seen.add(href)
            toc.append(href)
    return toc

def fetch_page(path):
    r=requests.get(BASE_URL+ path)
    soup=BeautifulSoup(r.text,"html.parser")
    title=soup.select_one("h1").get_text(strip=True)
    #Grab all paragraphs and lists items
    elems=soup.select_one("h2,h3,p,li")
    text="\n\n".join(e.get_text(strip=True) for e in elems)
    meta={"source": BASE_URL+ path, "title": title}
    return Document(page_content=text,metadata=meta)

def load_docs():
    docs=[]
    for path in fetch_toc():
        docs.append(fetch_page(path))
    return docs



def chunk_docs(docs):
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=200,
    )
    all_chunks=[]
    for doc in docs:
        splits=splitter.split_text(doc.page_content)
        for i,chunk in enumerate(splits):
            meta=doc.metadata.copy()
            meta["chunk_id"]=i
            all_chunks.append(Document(page_content=chunk,metadata=meta))
    return all_chunks


if __name__ == "__main__":
    for path in fetch_toc():
        print(path)