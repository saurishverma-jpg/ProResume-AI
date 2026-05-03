import streamlit as st

def render_linkedin_scraper():
    """LinkedIn scraper - disabled in cloud deployment"""
    st.info("""
    🔗 **LinkedIn Job Scraper** is not available in the cloud deployment 
    as it requires a local Chrome browser.
    
    To use this feature, run the app **locally** on your machine.
    
    Meanwhile, use the **Job Search** tab to search jobs on other portals!
    """)
