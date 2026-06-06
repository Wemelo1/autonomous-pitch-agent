import streamlit as st
from scraper import scrape_website
from agents import agent_market_researcher, agent_ai_strategist, agent_pitch_copywriter, agent_quality_control

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(page_title="AI Pitch Agent", page_icon="🚀", layout="centered")

st.title("🚀 Autonomous Pitch Agent")
st.caption("Enter a company URL, and our multi-agent AI will scrape, analyze, and draft a hyper-personalized outreach pitch.")

# ==========================================
# SIDEBAR SETTINGS
# ==========================================
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("Groq API Key", type="password", placeholder="gsk_...")
    st.divider()
    st.caption("Built by Pr0_M1se 🚀")

# ==========================================
# MAIN DASHBOARD UI
# ==========================================
target_url = st.text_input("🔗 Target Company URL", placeholder="https://www.example.com")

if st.button("Generate Pitch"):
    if not api_key:
        st.error("⚠️ Please enter your Groq API Key in the sidebar first!")
        st.stop()
        
    if not target_url:
        st.warning("⚠️ Please enter a URL to analyze.")
        st.stop()

    # The visual status container that shows real-time agent progress
    with st.status("Initializing Multi-Agent Pipeline...", expanded=True) as status:
        
        # Step 1: Scrape
        st.write("🕵️‍♂️ **System:** Scraping website data...")
        raw_text = scrape_website(target_url)
        if "Error" in raw_text:
            status.update(label="Scraping Failed", state="error")
            st.error(raw_text)
            st.stop()

        # Step 2: Research
        st.write("📊 **Agent 1 (Researcher):** Analyzing core company identity...")
        research_data = agent_market_researcher(raw_text, api_key)

        # Step 3: Strategy
        st.write("🧠 **Agent 2 (Strategist):** Brainstorming AI integration ideas...")
        ai_strategy = agent_ai_strategist(research_data, api_key)

        # Step 4 & 5: Copywriter + Quality Control loop
        max_retries = 3
        score = 0
        attempt = 0

        for attempt in range(max_retries):
            attempt_label = f"(Attempt {attempt + 1}/{max_retries})"
            st.write(f"✍️ **Agent 3 (Copywriter):** Crafting the outreach pitch... {attempt_label}")
            final_pitch = agent_pitch_copywriter(research_data, ai_strategy, api_key)

            st.write(f"⚖️ **Agent 4 (Quality Control):** Grading the pitch... {attempt_label}")
            score = agent_quality_control(final_pitch, api_key)

            if score >= 7:
                st.write(f"✅ **QC Passed** with score {score}/10 on attempt {attempt + 1}.")
                break
            else:
                if attempt < max_retries - 1:
                    st.write(f"🔄 **QC Score {score}/10 — below threshold. Regenerating pitch...**")

        status.update(label="Pipeline Complete!", state="complete", expanded=False)

    # ==========================================
    # DISPLAY FINAL RESULTS
    # ==========================================
    st.divider()
    
    if score >= 7:
        st.success(f"✅ **Pitch Approved** (Quality Score: {score}/10)")
    else:
        st.error(f"⚠️ **Pitch Needs Review** (Quality Score: {score}/10)")
        
    st.subheader("Final Outreach Proposal")
    st.markdown(final_pitch)
    
    with st.expander("🔍 View AI Strategy Breakdown"):
        st.markdown(ai_strategy)