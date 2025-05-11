from langchain_core.prompts import ChatPromptTemplate

class PromptEngineer:
    """Responsible only for crafting prompts"""
    
    @staticmethod
    def get_rag_prompt():
        """Return the Persian RAG prompt template"""
        template = """
        شما یک دستیار هوشمند فارسی هستید که به سوالات بر اساس متن زمینه پاسخ می‌دهید.
        در صورتی که پاسخ را نمی‌دانید، بگویید "پاسخ در اسناد موجود یافت نشد".
        پاسخ‌ها باید روان، دقیق و به فارسی باشند.
        
        زمینه: {context}
        
        سوال: {question}
        
        لطفاً پاسخ را به فارسی ارائه دهید:
        """
        return ChatPromptTemplate.from_template(template)