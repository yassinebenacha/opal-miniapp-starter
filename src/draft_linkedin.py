import argparse, os, sys, textwrap
from dotenv import load_dotenv

try:
    import google.generativeai as genai
except ImportError:
    print("Please install dependencies with: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

TEMPLATE = """You are a LinkedIn writing assistant.
Write a LinkedIn post from the text below.
Requirements:
- Start with a one-line hook.
- 3–5 short bullets (max 12 words each).
- End with a question or CTA.
- Tone: {tone}.
- Max length: {max_chars} characters.
Return ONLY the post, no preface.

TEXT:
{body}
"""

def draft_post(text: str, tone: str = "professional", max_chars: int = 1200) -> str:
    model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Set GEMINI_API_KEY env var.")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name)
    prompt = TEMPLATE.format(tone=tone, max_chars=max_chars, body=text)
    resp = model.generate_content(prompt)
    return resp.text.strip()

def main():
    load_dotenv()
    p = argparse.ArgumentParser(description="Draft a LinkedIn post from text")
    p.add_argument("--text", required=True, help="Raw article text")
    p.add_argument("--tone", default="professional", choices=["professional", "friendly", "bold"])
    p.add_argument("--max-chars", type=int, default=1200)
    args = p.parse_args()
    post = draft_post(args.text, args.tone, args.max_chars)
    print(post)

if __name__ == "__main__":
    main()
