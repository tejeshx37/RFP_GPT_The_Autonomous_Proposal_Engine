from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

# Try a different model
model = "gemini-2.0-flash-lite-preview-02-05"

llm = ChatGoogleGenerativeAI(
    model=model,
    verbose=True,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

print(f"Attempting to invoke {model}...")
try:
    msg = llm.invoke("Hi")
    print(f"RESPONSE: '{msg.content}'")
except Exception as e:
    print(f"EXCEPTION: {e}")
