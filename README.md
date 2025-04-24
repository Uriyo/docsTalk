# 🍵 ChaiDocs RAG

> "Because asking questions should be as satisfying as a perfect cup of chai."

## What is This?

ChaiDocs RAG is a Retrieval-Augmented Generation system that lets you chat with the ChaiDocs documentation. Think of it as having a really smart friend who's read all the docs so you don't have to!

![Tea and Books](https://media.giphy.com/media/3jVT4U5bilspG/giphy.gif)

## 🚀 Features

- Scrapes ChaiDocs content automatically
- Builds a FAISS vector index for speedy retrieval
- Provides accurate answers with source citations
- Works right in your terminal (fancy colors included!)

## 🛠️ Installation

1. Clone this repo faster than you can say "masala chai":
```bash
git clone https://github.com/yourusername/chaidocs-rag.git
cd chaidocs-rag
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## 📚 How to Use

Just run:
```bash
python main.py
```

Then ask any question about ChaiDocs YouTube content:
```
> How do I use the YouTube API with Chai?
```

The system will:
1. Find relevant documentation chunks
2. Generate a helpful answer
3. Show you the source documents

![Mind Blown](https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif)

## 🧩 How It Works

1. **Ingest**: Scrapes docs from ChaiDocs and chunks them into digestible pieces
2. **Embed**: Converts text chunks into vector embeddings using OpenAI
3. **Index**: Stores vectors in a FAISS index for efficient similarity search
4. **Search**: Finds relevant docs when you ask a question
5. **Generate**: Creates a coherent answer using LLM magic

## 🤓 For Developers

Want to extend this? Here's what you need to know:

- `ingest.py`: Handles document scraping and chunking
- `qa.py`: Sets up the FAISS vector store and QA chain
- `main.py`: Puts it all together with a CLI interface

## 📋 Requirements

- Python 3.8+
- OpenAI API key
- A love for documentation (or at least a need to use it)
- A sense of humor (optional but recommended)

## 🚧 Known Issues

- Sometimes the scraper gets confused, like me before my morning chai
- May occasionally hallucinate answers (don't we all?)
- Not all ChaiDocs content is indexed (yet!)

## 🙏 Credits

Built with:
- LangChain
- OpenAI
- FAISS
- BeautifulSoup
- Rich (for those fancy terminal colors)
- Caffeine and determination

## 📄 License

MIT License - Feel free to use it, just don't blame us if it starts making tea jokes.

---

> "Documentation is like chai - best when fresh, accessible, and consumed regularly." 