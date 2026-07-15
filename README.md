# 🛡 Agentic AI for Security Scan Analysis

An AI-assisted cybersecurity application that integrates **Nmap** with **Google Gemini AI** to automatically analyze network scan results and generate structured security assessments.

Instead of manually interpreting Nmap output, the AI agent explains security findings, identifies potential risks, recommends remediation, and suggests appropriate follow-up penetration testing activities.

---

## 🚀 Features

- 🔍 Automated Network Scanning using Nmap
- 🤖 AI-powered Security Analysis using Google Gemini
- 📋 Structured Security Assessment Report
- ⚠ Risk Identification & Prioritization
- 🛠 Remediation Recommendations
- 🎯 Suggested Next VAPT Activities
- 🌐 Simple Flask-based Web Interface

---

## 🧠 Agentic AI Workflow

The AI agent follows a simple decision-making workflow:

```
          Observe
              │
              ▼
     Read Nmap Scan Result
              │
              ▼
           Reason
              │
              ▼
   Analyze Services & Risks
              │
              ▼
           Decide
              │
              ▼
 Recommend Next Security Tests
              │
              ▼
             Act
              │
              ▼
 Generate Security Report
```

---

## 🏗 Project Workflow

```
User
 │
 ▼
Enter Target IP / Domain
 │
 ▼
Flask Web Application
 │
 ▼
Run Nmap Scan
 │
 ▼
Collect Scan Results
 │
 ▼
Google Gemini AI
 │
 ▼
AI Security Analysis
 │
 ▼
Display Report
```

---

## 📂 Project Structure

```text
Agentic-AI-Security-Scan-Analysis/

│── app.py
│── security_agent.py
│── nmap_tool.py
│── prompts.py
│── requirements.txt
│── .env
│── README.md
│
├── templates/
│     └── index.html
│
└── static/
      └── style.css
```

---

## 🛠 Technologies Used

- Python
- Flask
- Google Gemini API
- Nmap
- HTML
- CSS

---

## ⚙ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/Agentic-AI-Security-Scan-Analysis.git

cd Agentic-AI-Security-Scan-Analysis
```

---

### 2. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

Command Prompt

```cmd
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install Nmap

Download and install Nmap from:

https://nmap.org/download.html

Verify installation

```bash
nmap --version
```

---

### 5. Configure Gemini API Key

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Generate a free API key from:

https://aistudio.google.com/

---

### 6. Run Application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### Home Page

_Add Screenshot_

### Nmap Scan Result

_Add Screenshot_

### AI Security Analysis

_Add Screenshot_

---

## 📖 Example AI Report

The AI generates a structured report including:

- Executive Summary
- Open Ports & Services
- Risk Analysis
- Risk Priority
- Remediation
- Recommended Next Security Tests
- Final Verdict

---

## 🎯 Learning Outcomes

This project helped me understand:

- Agentic AI concepts
- Prompt Engineering
- AI API Integration
- Flask Web Development
- Python Automation
- Nmap Integration
- AI-assisted Cybersecurity Workflows

---

## 🔮 Future Improvements

- OWASP ZAP Integration
- Nuclei Integration
- CVSS Scoring
- PDF Report Generation
- Model Fallback Mechanism
- Better UI/UX
- Multi-tool AI-assisted VAPT

---

## ⚠ Disclaimer

This project is intended **only for educational and authorized security testing purposes**.

Only scan systems that you own or have explicit permission to test.

---

## 👨‍💻 Author

**Gaurav**

Cyber Security Enthusiast | VAPT | Python | AI in Cybersecurity

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile
