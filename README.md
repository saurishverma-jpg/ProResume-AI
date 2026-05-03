# 🚀 ProResume-AI

A powerful AI-powered resume analysis and building platform built with Streamlit, Google Gemini AI, and modern web technologies.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red.svg)
![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## ✨ Features

- **🔍 AI Resume Analyzer** — Upload your resume (PDF/DOCX) and get detailed AI-powered feedback including ATS score, skill gaps, strengths, and improvement suggestions
- **📝 Resume Builder** — Build professional resumes using multiple templates (Modern, Professional, Minimal, Creative)
- **📊 Analytics Dashboard** — Track resume submissions, scores, and trends with interactive charts
- **🎯 Job Search** — Search for jobs across multiple portals with smart filters
- **💬 Feedback System** — Collect and analyze user feedback
- **🔐 Admin Panel** — Secure admin dashboard to manage users and view analytics

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit, HTML/CSS |
| AI Engine | Google Gemini 2.5 Flash, OpenRouter |
| PDF Processing | pdfplumber, pypdf, reportlab |
| Database | SQLite |
| Data Viz | Plotly, Matplotlib, Seaborn |
| Resume Export | python-docx |

---

## ⚡ Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/ProResume-AI.git
cd ProResume-AI
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
cp .env.example .env
```
Edit `.env` and add your API keys:
```env
GOOGLE_API_KEY=your_google_gemini_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

**Get API Keys:**
- Google Gemini: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
- OpenRouter: [https://openrouter.ai/keys](https://openrouter.ai/keys)

### 5. Run the application
```bash
python run_app.py
```
Or directly:
```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501**

---

## 📁 Project Structure

```
ProResume-AI/
│
├── app.py                    # Main application entry point
├── run_app.py                # Application launcher
├── ui_components.py          # Reusable UI components
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
├── .gitignore
│
├── config/
│   ├── database.py           # Database setup & queries
│   ├── job_roles.py          # Job roles & required skills
│   └── courses.py            # Course recommendations by role
│
├── utils/
│   ├── ai_resume_analyzer.py # Google Gemini AI analyzer
│   ├── resume_analyzer.py    # Rule-based resume analysis
│   ├── resume_builder.py     # DOCX resume builder (4 templates)
│   ├── resume_parser.py      # PDF/DOCX text extractor
│   ├── database.py           # Utility DB functions
│   └── excel_manager.py      # Excel export manager
│
├── dashboard/
│   └── dashboard.py          # Analytics dashboard
│
├── feedback/
│   └── feedback.py           # Feedback collection system
│
├── jobs/
│   ├── job_search.py         # Job search UI
│   ├── job_portals.py        # Job portal integrations
│   ├── companies.py          # Featured companies data
│   └── suggestions.py        # Search suggestions
│
└── style/
    └── style.css             # Global stylesheet (dark theme)
```

---

## 🔑 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google Gemini API key for AI analysis | Yes |
| `OPENROUTER_API_KEY` | OpenRouter API key (alternative AI models) | Optional |

---

## 📸 Screenshots

### Home Page
The landing page showcases all features with a clean dark UI.

### Resume Analyzer
Upload a PDF or DOCX resume → get AI-powered analysis with:
- Resume Score (0-100)
- ATS Score (0-100)
- Skills gap analysis
- Actionable recommendations
- Downloadable PDF report

### Resume Builder
Fill in your details and choose from 4 professional templates to generate a DOCX resume instantly.

### Dashboard
Interactive analytics showing resume trends, score distributions, and AI model usage.

---

## 🚀 Deployment

### Streamlit Cloud (Free)
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo
4. Add your API keys in **Secrets** settings
5. Deploy!

### Docker
```bash
docker build -t proresume-ai .
docker run -p 8501:8501 --env-file .env proresume-ai
```

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Built with ❤️ using Python and Streamlit.

---

## ⭐ Support

If you found this project helpful, please give it a ⭐ on GitHub!
