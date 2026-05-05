# 🚀 HookFlow

**HookFlow** is an AI-powered content generation engine designed to turn simple ideas into **high-engagement short-form content**.

It generates:
- Scroll-stopping hooks
- Short-form video scripts
- Engaging captions
- Optimized hashtags
- Structured shot lists

Built for creators, marketers, and anyone producing content for platforms like Instagram Reels and YouTube Shorts.

---

## ⚡ Features

- 🎯 Hook-first content generation
- 🧠 Multi-step AI pipeline (not single prompt)
- 🔁 Retry + validation system for robustness
- 🧹 Output cleaning and structuring
- 🎬 Script generation with pacing & timing
- 🏷️ Hashtag optimization
- 📸 Shot list generation for video production

---

## 🏗️ Architecture

Request → Pipeline → Prompt Builders → LLM → Validators → Structured Output

---

## 📂 Project Structure
```
app/
│
├── main.py
├── routes/
│   └── generate.py
│
├── models/
│   └── request_models.py
│
├── services/
│   ├── pipeline_service.py
│   ├── llm_service.py
│   └── style_service.py
│
├── prompts/
│   ├── hook_prompt.py
│   ├── script_prompt.py
│   ├── caption_prompt.py
│   ├── hashtag_prompt.py
│   ├── shotlist_prompt.py
│   └── hook_score_prompt.py
│
└── utils/
    └── validators.py
```
---

## 🧠 Tech Stack

- Backend: FastAPI
- LLM: Groq / OpenAI-compatible APIs
- Validation: Custom rule-based validators
- Architecture: Modular prompt + pipeline system

---

## 📥 Installation

### 1. Clone the repository

git clone https://github.com/AmoghInfinity/HookFlow.git
cd hookflow

---

### 2. Create virtual environment

python -m venv venv
source venv/bin/activate   (macOS/Linux)
venv\Scripts\activate      (Windows)

---

### 3. Install dependencies

pip install -r requirements.txt

---

### 4. Set environment variables

Create a .env file:

GROQ_API_KEY=your_api_key_here

---

## ▶️ Running the Server

uvicorn app.main:app --reload

Server runs at:

http://127.0.0.1:8000

---

## 📡 API Endpoint

### POST /generate

#### Request Body

{
  "topic": "Street food in Lucknow",
  "platform": "Instagram",
  "tone": "funny",
  "style": "funny",
  "duration": 30
}

---

#### Response

{
  "status": "success",
  "data": {
    "hook_options": [],
    "selected_hook": "",
    "script": "",
    "caption": "",
    "hashtags": [],
    "shot_list": []
  }
}

---

## 🔍 Key Design Decisions

- Multi-step pipeline for better output quality
- Hook-first generation strategy
- Validation layer for structured outputs
- Retry mechanism for reliability

---

## ⚠️ Limitations

- Dependent on LLM response quality
- No caching layer
- No rate limiting
- Style control is rule-based

---

## 🚀 Future Improvements

- Streaming responses
- Hook analytics
- Multi-language support
- Personalization
- Voice + video generation

---

## 👤 Author

Built by Amogh Gupta

---

## ⭐ Support

If you find this useful, consider starring the repo.
