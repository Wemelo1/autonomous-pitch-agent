# 🚀 Autonomous Market Intelligence & Pitch Agent

A multi-agent AI system built to automate B2B market research and cold outreach. Give it a target company's URL, and the system automatically scrapes their website, analyzes their business model, identifies AI integration opportunities, and drafts a hyper-personalized, high-converting pitch.

**Live Demo:** [https://autonomous-pitch-agent-pr0m1se.streamlit.app/]

## 🧠 How It Works (The Multi-Agent Pipeline)

This tool utilizes a modular architecture to ensure high-quality, factual outputs:

1.  **The Extraction Engine:** Uses `BeautifulSoup4` to bypass HTML bloat and extract clean, readable text directly from target URLs.
2.  **Agent 1 (The Researcher):** Analyzes the raw text to map out the company's core value proposition and target audience (Strict low-temperature setting for factual accuracy).
3.  **Agent 2 (The Strategist):** Brainstorms specific, niche-relevant ways the company can save time or generate revenue using AI automation.
4.  **Agent 3 (The Copywriter):** Synthesizes the research and strategy into a persuasive cold email with a clear Call-to-Action.
5.  **Agent 4 (Quality Control):** A strict evaluation agent that grades the final pitch using Regex number extraction. If the pitch scores below 7/10, it flags it for human review.

## 🛠️ Tech Stack
*   **Frontend:** Streamlit 
*   **LLM Engine:** LLaMA 3.3 (via Groq API)
*   **Data Extraction:** Python `requests`, `BeautifulSoup4`
*   **Logic Routing:** Regular Expressions (`re`)

## 💼 Why This Matters for Business
Standard cold outreach is generic and ignored. Manual research takes hours per lead. This pipeline allows agencies, SDRs, and freelancers to generate heavily researched, highly personalized pitches at scale in under 15 seconds. 

---


Built by **Pr0_M1se** — LLM Engineer
