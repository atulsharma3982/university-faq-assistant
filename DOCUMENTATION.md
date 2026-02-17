# Project Documentation

## University FAQ Assistant

------------------------------------------------------------------------

## 1. Introduction

The **University FAQ Assistant** is an AI-powered web application
designed to answer admission-related questions for selected
universities.\
It provides concise, data-grounded responses by combining
retrieval-based context selection, context compression, and a
cloud-hosted language model.

The project demonstrates a practical implementation of a
**Retrieval-Augmented Generation (RAG)** pipeline using minimal
infrastructure and free-tier services.

------------------------------------------------------------------------

## 2. Problem Statement

University admission information is often scattered across long
documents and complex websites, making it difficult for students to
quickly find accurate answers.

Key challenges: - Information overload - Lack of conversational access -
Difficulty navigating official documents - Repetitive queries answered
manually

This project addresses these issues by offering a conversational
assistant that responds using **only verified college data**.

------------------------------------------------------------------------

## 3. Objectives

### Primary Objectives

-   Build a chatbot for answering university admission FAQs
-   Ensure answers are grounded in provided data
-   Reduce token usage using context compression
-   Deploy the system on a free hosting platform

### Secondary Objectives

-   Maintain a clean and responsive user interface
-   Support follow-up questions without repeating college names
-   Keep the architecture simple and understandable

------------------------------------------------------------------------

## 4. System Architecture

### High-Level Architecture

User interacts with a web-based chat interface.\
Requests are processed by a Flask backend, which retrieves relevant
college data, compresses it, and sends it to a cloud-based LLM.

Flow:

User Question\
→ Frontend (HTML/CSS/JS)\
→ Flask Backend\
→ College Detection\
→ College Data Retrieval\
→ ScaleDown Context Compression\
→ Ollama Cloud LLM\
→ Response Returned to User

------------------------------------------------------------------------

## 5. Technology Stack

### Frontend

-   HTML
-   CSS
-   Vanilla JavaScript

### Backend

-   Python
-   Flask

### AI & APIs

-   **Ollama Cloud API** -- Large Language Model for response generation
-   **ScaleDown API** -- Context compression to reduce token size

### Deployment

-   Render (Free Tier)

------------------------------------------------------------------------

## 6. Project Structure

    university-faq-bot/
    │
    ├── backend/
    │   ├── app.py
    │   └── data/
    │       ├── iit_delhi.md
    │       ├── iit_kharagpur.md
    │       ├── jadavpur.md
    │       └── nit_durgapur.md
    │
    ├── frontend/
    │   ├── index.html
    │   ├── style.css
    │   └── script.js
    │
    ├── requirements.txt
    ├── .env.example
    ├── .gitignore
    ├── README.md
    └── DOCUMENTATION.md

------------------------------------------------------------------------

## 7. Core Components

### 7.1 Frontend

The frontend provides a chat-style interface where users can: - Ask
admission-related questions - Select suggested queries - View
AI-generated responses

Responsibilities: - Collect user input - Send requests to backend API -
Display responses dynamically

------------------------------------------------------------------------

### 7.2 Backend

The Flask backend handles: - API routing - College detection logic -
Session-based state management - Data loading - Context compression -
LLM interaction

Session storage ensures that follow-up questions remain contextual to
the selected college.

------------------------------------------------------------------------

### 7.3 College Data

Each supported college has a dedicated Markdown file containing: -
Admission process - Fees - Eligibility - Scholarships - Important
deadlines

Only one college's data is loaded per session to maintain accuracy.

------------------------------------------------------------------------

## 8. Core Logic

### 8.1 College Detection

User questions are scanned for predefined keywords to identify the
relevant college.

Example: - Input: "What is the fee for IITD?" - Detected college: IIT
Delhi

If no college is detected initially, the user is prompted to specify
one.

------------------------------------------------------------------------

### 8.2 Session-Based Context

The selected college is stored per user session, allowing follow-up
questions such as: - "What is the hostel fee?" - "How can I apply?"

without repeating the college name.

------------------------------------------------------------------------

### 8.3 Context Compression

The retrieved college data is compressed using the ScaleDown API before
being sent to the LLM.

Benefits: - Reduced token usage - Faster response time - Lower API cost

------------------------------------------------------------------------

### 8.4 LLM Response Generation

The compressed context and user question are passed to the Ollama Cloud
LLM using a constrained prompt that enforces: - Short and direct
answers - No hallucination - No assumptions outside provided data

------------------------------------------------------------------------

## 9. API Endpoints

### GET /

Serves the frontend application.

### POST /chat

Handles user questions.

Request:

    {
      "question": "What is the tuition fee for IIT Delhi?"
    }

Response:

    {
      "answer": "The tuition fee information is ..."
    }

------------------------------------------------------------------------

## 10. Environment Variables

  Variable            Description
  ------------------- ---------------------------------
  SCALEDOWN_API_KEY   API key for context compression
  OLLAMA_API_KEY      API key for Ollama cloud model

Environment variables are managed locally via `.env` and in production
via Render's dashboard.

------------------------------------------------------------------------

## 11. Deployment

The application is deployed using **Render** (free tier).

Deployment steps: 1. Push code to GitHub 2. Create a new Web Service on
Render 3. Configure build and start commands 4. Add environment
variables 5. Deploy and obtain public URL

------------------------------------------------------------------------

## 12. Supported Colleges

-   IIT Delhi
-   IIT Kharagpur
-   Jadavpur University
-   NIT Durgapur

The system can be extended by adding more data files and keywords.

------------------------------------------------------------------------

## 13. Limitations

-   Limited to four colleges
-   Keyword-based detection
-   No long-term conversation history
-   Cold start delays on free hosting

------------------------------------------------------------------------

## 14. Future Enhancements

-   Add more universities
-   Implement fuzzy matching for college names
-   Support multi-college comparisons
-   Add conversation history
-   Enable streaming responses
-   Admin interface for updating data

------------------------------------------------------------------------

## 15. Conclusion

The University FAQ Assistant demonstrates an end-to-end AI system using
retrieval-based context, context compression, and cloud-hosted language
models.\
It fulfills the project objectives while remaining lightweight,
scalable, and suitable for free-tier deployment.

------------------------------------------------------------------------
