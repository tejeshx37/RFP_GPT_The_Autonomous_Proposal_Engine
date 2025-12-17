from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

print("--- ALL AVAILABLE MODELS ---")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
print("----------------------------")

def test_model(model_name):
    print(f"Testing {model_name}...")
    try:
        llm = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0
        )
        res = llm.invoke("Hello")
        print(f"Success with {model_name}: {res.content}")
        return True
    except Exception as e:
        print(f"Failed with {model_name}: {e}")
        return False

# Try finding a valid one from the list automatically
# But first print them.
