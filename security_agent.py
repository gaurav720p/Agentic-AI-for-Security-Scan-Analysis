import os

from dotenv import load_dotenv
from google import genai

from prompts import SYSTEM_PROMPT

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def analyze_scan(scan_result):
    """
    Analyze the Nmap scan using Gemini AI.
    """

    prompt = f"""
{SYSTEM_PROMPT}

==================================================

NMAP SCAN RESULT

==================================================

{scan_result}

==================================================

Generate the professional security assessment report.

Follow every section exactly.

Do not skip any section.

Keep the report concise but informative.
"""

    try:

        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"""
AI Agent Error

{str(e)}
"""