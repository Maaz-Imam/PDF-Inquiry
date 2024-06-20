from langchain_google_genai import ChatGoogleGenerativeAI
from src.key import GOOGLE_API_KEY

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)
result = llm.invoke("Write 1 - 10")
print(result.content)
