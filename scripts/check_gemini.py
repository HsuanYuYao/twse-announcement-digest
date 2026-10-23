import os
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    resp = client.models.generate_content(
        model="gemini-3.5-flash-lite",   # check AI Studio for the current model names
        contents="Explain what material information is in one sentence.",
    )
    print(resp.text)

if __name__ == "__main__":
    main()
