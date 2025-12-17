import streamlit as st
import pandas as pd
from pypdf import PdfReader
from crew import run_crew
import os
import json
from pathlib import Path

# Function to load custom CSS
def load_css():
    css_file = Path(__file__).parent / "static" / "style.css"
    if css_file.exists():
        with open(css_file) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Page Config
st.set_page_config(
    page_title="Shadow Strikers RFP Demo",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load Custom CSS
load_css()

# Custom Header with Enhanced Styling
st.markdown("""
    <div style="text-align: center; padding: 2rem 0 1rem 0;">
        <h1 style="margin-bottom: 0.5rem;">
            <span style="font-size: 3.5rem;">🎯</span> Shadow Strikers: Multi-Agent RFP Automation
        </h1>
        <div style="display: inline-block; background: linear-gradient(135deg, rgba(59, 130, 246, 0.2), rgba(168, 85, 247, 0.2)); 
                    border: 1px solid rgba(168, 85, 247, 0.4); border-radius: 20px; padding: 0.4rem 1rem; 
                    margin-top: 0.5rem; font-size: 0.85rem; font-weight: 600; letter-spacing: 0.05em;">
            ✨ POWERED BY AI AGENTS
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; margin-bottom: 3rem;">
        <p style="font-size: 1.2rem; color: #cbd5e1; font-weight: 500;">
            Autonomous discovery, analysis, and proposal generation for B2B tenders
        </p>
    </div>
""", unsafe_allow_html=True)

# Section 1: FILE UPLOAD with Enhanced UI
st.markdown("""
    <h2 style="margin-top: 2rem;">
        <span style="font-size: 2rem;">📄</span> Upload RFP Document
    </h2>
""", unsafe_allow_html=True)
st.markdown("<p style='color: #cbd5e1; margin-bottom: 1.5rem; font-size: 1.05rem;'>Upload your RFP PDF to begin automated analysis</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"],
    help="Upload the RFP document in PDF format"
)

if uploaded_file is not None:
    # Show file info with custom styling
    st.markdown(f"""
        <div style="background: rgba(16, 185, 129, 0.1); 
                    border-left: 4px solid #10b981; 
                    border-radius: 8px; 
                    padding: 1rem; 
                    margin: 1rem 0;">
            <p style="margin: 0; color: #f8fafc;">
                ✅ <strong>File uploaded:</strong> {uploaded_file.name} ({uploaded_file.size / 1024:.2f} KB)
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Extract text
    reader = PdfReader(uploaded_file)
    extracted_text = ""
    for page in reader.pages:
        extracted_text += page.extract_text() + "\n"
    
    st.markdown(f"<p style='color: #cbd5e1; font-size: 0.9rem;'>📊 Extracted {len(extracted_text):,} characters from {len(reader.pages)} pages</p>", unsafe_allow_html=True)

    # Section 2: PROCESS BUTTON with spacing
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        process_button = st.button("🚀 Run AI Agents", use_container_width=True)
    
    if process_button:
        with st.spinner("🤖 AI Agents are analyzing your RFP..."):
            try:
                result = run_crew(extracted_text)
                
                # Success message
                st.markdown("""
                    <div style="background: rgba(16, 185, 129, 0.1); 
                                border-left: 4px solid #10b981; 
                                border-radius: 8px; 
                                padding: 1rem; 
                                margin: 2rem 0;">
                        <p style="margin: 0; color: #f8fafc;">
                            ✅ <strong>Analysis Complete!</strong> Review the results below.
                        </p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Section 3: RESULTS with Enhanced Layout
                st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
                st.markdown("""
                    <h2 style="margin-bottom: 1rem;">
                        <span style="font-size: 2.5rem;">📊</span> Analysis Results
                    </h2>
                """, unsafe_allow_html=True)
                st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
                
                col1, col2 = st.columns(2, gap="large")
                
                with col1:
                    st.markdown("""
                        <h3 style="margin-bottom: 1rem;">
                            <span style="font-size: 1.5rem;">📋</span> RFP Requirement Summary
                        </h3>
                    """, unsafe_allow_html=True)
                    summary = result.get("requirement_summary", "No summary provided.")
                    st.markdown(f"""
                        <div style="background: rgba(255, 255, 255, 0.05); 
                                    backdrop-filter: blur(10px); 
                                    border-radius: 12px; 
                                    border: 1px solid rgba(255, 255, 255, 0.1); 
                                    padding: 1.5rem; 
                                    margin-bottom: 1.5rem;">
                            <p style="color: #cbd5e1; line-height: 1.7;">{summary}</p>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("""
                        <h3 style="margin-bottom: 1rem;">
                            <span style="font-size: 1.5rem;">🎯</span> Best Matching SKU
                        </h3>
                    """, unsafe_allow_html=True)
                    st.json(result.get("sku", {}))
                    
                    st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)
                    
                    st.markdown("""
                        <h3 style="margin-bottom: 1rem;">
                            <span style="font-size: 1.5rem;">💰</span> Quoted Price
                        </h3>
                    """, unsafe_allow_html=True)
                    price = result.get("quote_price", 0)
                    st.metric("Total Quote", f"${price:,}", delta="20% margin applied")
                
                with col2:
                    st.markdown("""
                        <h3 style="margin-bottom: 1rem;">
                            <span style="font-size: 1.5rem;">📝</span> AI-Generated Proposal Draft
                        </h3>
                    """, unsafe_allow_html=True)
                    proposal = result.get("proposal_text", "No proposal generated.")
                    st.markdown(f"""
                        <div style="background: rgba(255, 255, 255, 0.05); 
                                    backdrop-filter: blur(10px); 
                                    border-radius: 12px; 
                                    border: 1px solid rgba(255, 255, 255, 0.1); 
                                    padding: 1.5rem; 
                                    max-height: 600px; 
                                    overflow-y: auto;">
                            <div style="color: #cbd5e1; line-height: 1.7;">{proposal}</div>
                        </div>
                    """, unsafe_allow_html=True)
            
            except Exception as e:
                st.markdown(f"""
                    <div style="background: rgba(239, 68, 68, 0.1); 
                                border-left: 4px solid #ef4444; 
                                border-radius: 8px; 
                                padding: 1rem; 
                                margin: 2rem 0;">
                        <p style="margin: 0; color: #f8fafc;">
                            ❌ <strong>Error:</strong> {str(e)}
                        </p>
                    </div>
                """, unsafe_allow_html=True)

# Footer with Enhanced Styling
st.markdown("<div style='margin: 4rem 0 2rem 0;'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 1.5rem;">
        <p style="color: #cbd5e1; font-size: 1rem; font-weight: 500;">
            <span style="font-size: 1.2rem;">✅</span> <strong>Human-in-the-Loop:</strong> Manager reviews and approves before final submission
        </p>
    </div>
""", unsafe_allow_html=True)
