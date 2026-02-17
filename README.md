# University FAQ Assistant

A lightweight AI-powered chatbot that answers university admission
questions using retrieval-based context and LLM responses.\
The system loads college-specific data, compresses it using the
ScaleDown API, and generates answers using an Ollama cloud model.

------------------------------------------------------------------------

## Live Demo

    https://university-faq-assistant-wv8d.onrender.com

------------------------------------------------------------------------

## Features

-   College-specific question answering
-   Automatic college detection from user queries
-   Context compression using ScaleDown API
-   LLM-based responses via Ollama Cloud
-   Clean, responsive chat interface
-   Session-based state (per-user college memory)
-   Fully deployable on free hosting

------------------------------------------------------------------------

## How It Works

Pipeline overview:

User question\
→ College detection\
→ Load selected college data\
→ ScaleDown compress(context + question)\
→ Send to LLM (Ollama cloud)\
→ Return final answer

------------------------------------------------------------------------

## Tech Stack

### Frontend

-   HTML
-   CSS
-   Vanilla JavaScript

### Backend

-   Python
-   Flask

### AI & APIs

-   Ollama Cloud (LLM)
-   ScaleDown API (context compression)

### Deployment

-   Render (free tier)

------------------------------------------------------------------------

## Project Structure

    university-faq-bot/ \
    │\
    ├── backend/ \
    │ ├── app.py \
    │ └── data/ \
    │ ├── iit_delhi.md \
    │ ├── iit_kharagpur.md \
    │ ├── jadavpur.md \
    │ └── nit_durgapur.md \
    │ ├── frontend/ \
    │ ├── index.html \
    │ ├── style.css \
    │ └── script.js \
    │ ├── requirements.txt \
    ├── .env.example \
    ├── .gitignore \
    └── README.md\

------------------------------------------------------------------------

## Installation (Local Setup)

### 1. Clone the repository

    git clone https://github.com/atulsharma3982/university-faq-bot.git\
    cd university-faq-bot

### 2. Create virtual environment (recommended)

    python -m venv venv
    source venv/bin/activate (macOS/Linux)
    venv\Scripts\activate (Windows)


### 3. Install dependencies

    pip install -r requirements.txt

### 4. Set up environment variables

Create a `.env` file in the project root:

>SCALEDOWN_API_KEY=your_scaledown_key\
>OLLAMA_API_KEY=your_ollama_key

### 5. Run the backend

    python backend/app.py

Open in browser: http://localhost:5000

------------------------------------------------------------------------

## Environment Variables

  | Variable | Purpose |
  | ------------------- | ---------------------------- |
  | SCALEDOWN_API_KEY |  Compresses college context |
  | OLLAMA_API_KEY   |   Accesses cloud LLM |

See `.env.example` for the template.

------------------------------------------------------------------------

## Deployment (Render)

1.  Push code to GitHub
2.  Go to Render dashboard
3.  Create a new Web Service
4.  Connect your repository
5.  Use these settings:

    Build command: pip install -r requirements.txt

    Start command: python backend/app.py


6.  Add environment variables: \
    SCALEDOWN_API_KEY=your_key\
    OLLAMA_API_KEY=your_key

7.  Deploy and use the generated URL

------------------------------------------------------------------------

## Supported Colleges

-   IIT Delhi
-   IIT Kharagpur
-   Jadavpur University
-   NIT Durgapur

The system detects the college automatically from user queries.

------------------------------------------------------------------------

## Example Questions

-   What is the tuition fee for IIT Delhi?
-   How can I apply to Jadavpur University?
-   Scholarships at NIT Durgapur
-   Admission process for IIT Kharagpur

------------------------------------------------------------------------

## Key Design Decisions

### College-specific context

Only one college's data is loaded at a time to: - Reduce token usage -
Improve answer accuracy - Avoid cross-college confusion

### Context compression

ScaleDown reduces: - Token size - Latency - Cost

### Session-based state

Each user session stores the selected college so follow-up questions
remain contextual.

------------------------------------------------------------------------

## Limitations

-   Only four colleges supported
-   No typo-tolerant college detection
-   Free hosting causes cold starts
-   No conversation memory beyond college context

------------------------------------------------------------------------

## Future Improvements

-   Add more universities
-   Fuzzy college name detection
-   Multi-college comparison
-   Conversation history support
-   Streaming responses
-   Admin dashboard for updating data

------------------------------------------------------------------------

## License

This project is for educational and demonstration purposes.

------------------------------------------------------------------------

## Author

>Atul Kumar Sharma\
GitHub: https://github.com/atulsharma3982
