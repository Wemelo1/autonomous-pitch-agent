# 🚀 Autonomous Pitch Agent

A multi-agent AI system that scrapes any company website, analyzes its business, and autonomously generates a hyper-personalized cold outreach pitch — complete with a self-correcting quality control loop.

🔗 **[Live Demo](#)** ← add your Streamlit link here

---

## The Problem

Writing personalized cold outreach emails is time-consuming and most people send generic templates that get ignored. This agent does the research, strategy, and copywriting for you — then grades its own output and regenerates if it's not good enough.

---

## How It Works

```
Target Company URL
      ↓
🕵️ Scraper — fetches and cleans website text (BeautifulSoup)
      ↓
📊 Agent 1: Market Researcher — extracts company name, value proposition, target industry
      ↓
🧠 Agent 2: AI Strategist — identifies 2 high-impact AI integration opportunities
      ↓
✍️ Agent 3: Pitch Copywriter — drafts a personalized cold outreach email
      ↓
⚖️ Agent 4: Quality Control — scores the pitch 1-10 against a strict rubric
      ↓
🔄 If score < 7 → loop back to Copywriter (up to 3 attempts)
      ↓
✅ Final approved pitch delivered to user
```

---

## What Makes This Genuinely Autonomous

Most "agent" projects call an LLM once and display the result. This pipeline:

- Uses **4 specialized agents**, each with a distinct role and prompt tuned for that role
- Implements a **self-correcting feedback loop** — the QC agent scores the pitch, and if it falls below a 7/10 threshold, the system automatically regenerates with a new attempt
- Shows **real-time agent progress** in the UI so users can watch the pipeline execute step by step
- Only delivers output that has passed its own quality bar

---

## Tech Stack

| Layer | Tool |
|---|---|
| LLM | LLaMA 3.3 70B via Groq API |
| Web Scraping | BeautifulSoup + Requests |
| Agent Orchestration | Custom multi-agent pipeline |
| UI | Streamlit |
| Language | Python |

---

## Agent Roles & Prompt Design

Each agent has a deliberately different temperature setting to match its task:

| Agent | Temperature | Why |
|---|---|---|
| Market Researcher | 0.1 | Needs factual, consistent output |
| AI Strategist | 0.5 | Balanced creativity and relevance |
| Pitch Copywriter | 0.7 | High creativity for compelling copy |
| Quality Control | 0.1 | Strict, consistent scoring |

---

## Running Locally

```bash
git clone https://github.com/Wemelo1/autonomous-pitch-agent.git
cd autonomous-pitch-agent
pip install -r requirements.txt
streamlit run app.py
```

You'll need a free [Groq API key](https://console.groq.com/) — enter it in the sidebar when the app loads.

---

## Example Output

**Input:** `https://www.somecompany.com`

**Agent 1 output:** Company profile with core value proposition and target industry

**Agent 2 output:** Two specific AI integration opportunities tailored to that company

**Agent 3 output:** A short, high-energy cold email with a CTA for a 10-minute call

**Agent 4 output:** Quality score + auto-regeneration if below threshold

---

## Why I Built This

I wanted to move beyond single-LLM applications into genuine agentic architecture. The key insight was that different tasks need different AI "personalities" — a researcher needs precision (low temperature), a copywriter needs creativity (high temperature). Adding the QC feedback loop pushed this from a pipeline into something that actually self-corrects, which is the core idea behind autonomous agents.

---

## What I'd Add Next

- [ ] Memory across sessions — track which companies have been pitched
- [ ] Email sending integration — connect to Gmail or SendGrid to send directly
- [ ] Scoring history — chart pitch quality improvements across attempts
- [ ] Support for LinkedIn profiles as input, not just websites
- [ ] Swap sequential pipeline for parallel agent execution where possible

---

Built by **Pr0_M1se** — LLM Engineer
