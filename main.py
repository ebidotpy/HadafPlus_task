from core.rag.system import PersianRAGSystem

def main():
    try:
        # Initialize the RAG system
        rag_system = PersianRAGSystem()
        rag_system.initialize()
        
        # Example query
        question = "در علوم هفتم عناصر به چند دسته تقسیم میشوند؟"
        print("\nProcessing...")
        answer = rag_system.query(question)
        
        print(f"Question: {question}")
        print(f"Answer: {answer}")
    except Exception as e:
        print(f"System error: {str(e)}")

if __name__ == "__main__":
    main()


