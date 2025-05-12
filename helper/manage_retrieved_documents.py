def show_retrieved_docs(docs):
    text = ""
    """Pretty print retrieved documents"""
    text += "\n" + "="*50 + "\n"
    text += "RETRIEVED DOCUMENTS" + "\n"
    text += "="*50 + "\n"
    for i, doc in enumerate(docs, 1):
        text += f"\n📄 Document {i}\n"
        text += f"📂 Source: {doc.metadata.get('source', 'unknown')}\n"
        text += f"📄 Page: {doc.metadata.get('page', 'N/A')}\n"
        text += "\nContent:" + "\n"
        text += "-"*40 + "\n"
        text += doc.page_content[:500] + ("..." if len(doc.page_content) > 500 else "") + "\n"
        text += "-"*40 + "\n"
    
    return text