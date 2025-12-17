from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

def test_model(model_name):
    print(f"Testing {model_name}...")
    try:
        llm = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0
        )
        res = llm.invoke("Hello, say 'working' if you hear me.")
        print(f"Success with {model_name}: {res.content}")
        return True
    except Exception as e:
        print(f"Failed with {model_name}: {e}")
        return False

# Test variants
test_model("gemini-1.5-flash")
test_model("gemini-1.5-pro")
test_model("gemini-pro")
test_model("models/gemini-1.5-flash")
