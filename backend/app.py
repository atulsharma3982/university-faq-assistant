from flask import Flask, request, jsonify, send_from_directory, session
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv("SCALEDOWN_API_KEY")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "../frontend")

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="")
app.secret_key = "replace_this_with_random_string"

# Map keywords to file names

COLLEGE_DATA_FILES = {
    "iit delhi": "iit_delhi.md",
    "iit kharagpur": "iit_kharagpur.md",
    "jadavpur": "jadavpur.md",
    "nit durgapur": "nit_durgapur.md"
}

COLLEGE_KEYWORDS = {
    "iit delhi": [
        "iit delhi",
        "iitd",
        "indian institute of technology delhi",
        "iit delhi college"
    ],
    "iit kharagpur": [
        "iit kharagpur",
        "iitkgp",
        "kgp",
        "indian institute of technology kharagpur",
        "iit kharagpur college"
    ],
    "jadavpur": [
        "jadavpur",
        "jadavpur university",
        "ju",
        "ju kolkata",
        "jadavpur college"
    ],
    "nit durgapur": [
        "nit durgapur",
        "nitd",
        "n.i.t durgapur",
        "national institute of technology durgapur",
        "nit durgapur college"
    ]
}

import requests

def scaledown_compression(context, question):
    url = "https://api.scaledown.xyz/compress/raw/"

    headers = {
        'x-api-key': apikey,
        'Content-Type': 'application/json'
    }

    payload = {
        "context": context,
        "prompt": question,
        "scaledown": {
            "rate": "auto" # Automatic compression rate optimization
        }
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=30)
        response.raise_for_status()

        data = response.json()

        # Adjust key if API returns different field
        compressed = data.get("compressed", "")
        if not compressed:
            # fallback to original context
            return context

        return compressed

    except Exception as e:
        print("ScaleDown error:", e)
        return context

def ollama_response(prompt):
    try:
        url = "https://ollama.com/api/chat"

        headers = {
            "Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "gpt-oss:20b-cloud",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(url, json=data, headers=headers, stream=True)

        final_text = ""
        for line in response.iter_lines():
            if line:
                chunk = json.loads(line.decode())
                final_text += chunk.get("message", {}).get("content", "")

        return final_text if final_text else "No response from AI."

    except Exception as e:
        print("Ollama error:", e)
        return "Sorry, the AI model is not responding right now."


def detect_college(question):
    q = question.lower()
    for college, keywords in COLLEGE_KEYWORDS.items():
        for word in keywords:
            if word in q:
                return college
    return None

def load_college_data(college):
    data_path = os.path.join(BASE_DIR, "data", COLLEGE_DATA_FILES[college])
    with open(data_path, "r", encoding="utf-8") as f:
        return f.read()
    
def detect_multiple_colleges(question):
    q = question.lower()
    found = []

    for college, keywords in COLLEGE_KEYWORDS.items():
        for word in keywords:
            if word in q:
                found.append(college)
                break

    # remove duplicates
    return list(set(found))

@app.route("/")
def serve_index():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/chat", methods=["POST"])
@app.route("/chat", methods=["POST"])
def chat_route():
    data = request.json
    question = data.get("question", "")

    # Detect multiple colleges first
    detected_colleges = detect_multiple_colleges(question)

    # COMPARISON MODE
    if len(detected_colleges) == 2:
        college1, college2 = detected_colleges

        data1 = load_college_data(college1)
        data2 = load_college_data(college2)

        combined_context = f"""
COLLEGE 1: {college1.upper()}
{data1}

COLLEGE 2: {college2.upper()}
{data2}
"""

        compressed = scaledown_compression(combined_context, question)

        prompt = f"""
You are a university comparison assistant.

RULES:
- Compare only using the provided data.
- Keep answers short and structured.
- Do not guess or add extra information.
- Do not use markdown syntax. Use lists or simple paragraph
- Do NOT create tables unless asked.

DATA:
{compressed}

QUESTION:
{question}

ANSWER:
"""

        answer = ollama_response(prompt)
        return jsonify({"answer": answer})

    # NORMAL SINGLE-COLLEGE MODE
    detected = detect_college(question)
    current_college = session.get("college")

    # Case 1: No college selected yet
    if current_college is None:
        if detected:
            session["college"] = detected
            current_college = detected
        else:
            return jsonify({
                "answer": "Please mention the college name first."
            })

    # Case 2: User switches college
    if detected and detected != current_college:
        session["college"] = detected
        current_college = detected

    # Load selected college data
    college_data = load_college_data(current_college)

    # Compress context
    compressed_context = scaledown_compression(college_data, question)

    # Build final prompt
    final_prompt = f"""
You are a university admissions FAQ bot.

RULES:
- Answer ONLY using the provided DATA.
- If the DATA does not contain the answer, say:
  "This information is not available in the provided data."
- Keep answers short and direct.
- Do NOT create tables unless asked.

COLLEGE: {current_college.upper()}

DATA:
{compressed_context}

QUESTION:
{question}

ANSWER:
"""

    answer = ollama_response(final_prompt)

    return jsonify({"answer": answer})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)