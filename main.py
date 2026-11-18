import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def main():
    print("Welcome to LangChain!")

    # Check for configured API keys
    google_key = os.getenv("GOOGLE_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")
    groq_key = os.getenv("GROQ_API_KEY")

    if google_key:
        print("[+] Found GOOGLE_API_KEY. Initializing Gemini model...")
        try:
            from langchain.chat_models import init_chat_model

            model = init_chat_model("google_genai:gemini-2.5-flash")
            response = model.invoke("Say hello in one brief sentence.")
            print("Response:", response.content)
        except Exception as e:
            print(f"Error invoking Gemini: {e}")
    elif openai_key:
        print("[+] Found OPENAI_API_KEY. Initializing OpenAI model...")
        try:
            from langchain.chat_models import init_chat_model

            model = init_chat_model("openai:gpt-4o")
            response = model.invoke("Say hello in one brief sentence.")
            print("Response:", response.content)
        except Exception as e:
            print(f"Error invoking OpenAI: {e}")
            
    elif groq_key:
        print("[+] Found GROQ_API_KEY. Initializing Groq model...")
        try:
            from langchain_groq import ChatGroq

            model = ChatGroq(model="llama-3.3-70b-versatile")
            response = model.invoke("Say hello in one brief sentence.")
            print("Response:", response.content)
        except Exception as e:
            print(f"Error invoking Groq: {e}")
    else:
        print("No API keys detected in .env.")
        print("Please configure GOOGLE_API_KEY, OPENAI_API_KEY, or GROQ_API_KEY in your .env file.")


if __name__ == "__main__":
    main()
