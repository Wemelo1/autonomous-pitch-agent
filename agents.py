import requests
import re

def call_groq(prompt, api_key, temperature=0.2):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        return f"API Error: {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

def agent_market_researcher(raw_text, api_key):
    prompt = f"Analyze this website text and provide a concise profile: Name, Core Value Proposition, Target Industry.\n\nText: {raw_text}"
    return call_groq(prompt, api_key, temperature=0.1)

def agent_ai_strategist(research_data, api_key):
    prompt = f"Review this company profile and identify 2 highly impactful ways they could integrate Generative AI to save time or make money.\n\nProfile: {research_data}"
    return call_groq(prompt, api_key, temperature=0.5)

def agent_pitch_copywriter(research_data, ai_strategy, api_key):
    prompt = f"Write a compelling, professional cold outreach email pitching AI automation services to this company. Use this background and AI strategy. Keep it short, high-energy, with a CTA for a 10-min call.\n\nBackground: {research_data}\nStrategy: {ai_strategy}"
    return call_groq(prompt, api_key, temperature=0.7)

def agent_quality_control(final_pitch, api_key):
    prompt = f"""
    You are a ruthless, high-standards Quality Controller for cold outreach emails. 
    Rate this pitch strictly from 1 to 10 based on this rubric:
    
    - 1-4: Generic, boring, robotic, or lacks a clear Call to Action.
    - 5-6: Okay, but feels like a template. Nothing stands out.
    - 7-8: Professional and relevant, but could be punchier.
    - 9-10: Exceptional, highly personalized, irresistible hook, and a flawless Call to Action.
    
    Be harsh. Most pitches should be a 5 or 6. 
    Reply with ONLY a single number between 1 and 10.
    
    Pitch: {final_pitch}
    """
    qc_result = call_groq(prompt, api_key, temperature=0.1)
    
    try:
        numbers = re.findall(r'\d+', qc_result)
        score = int(numbers[0])
        if score > 10:
            score = 10
    except:
        score = 0
        
    return score