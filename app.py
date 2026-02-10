import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import numpy as np
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Bank Nifty Options Analyzer",
    page_icon="📈",
    layout="wide"
)

# Add custom CSS
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; color: #1E3A8A; text-align: center;}
    .metric-card {background-color: #f8f9fa; padding: 1rem; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Dashboard", "Option Chain", "Paper Trading"],
        icons=["house", "bar-chart", "wallet"],
        default_index=0,
    )

# Dashboard
if selected == "Dashboard":
    st.markdown('<h1 class="main-header">🏦 Bank Nifty Options Analyzer</h1>', unsafe_allow_html=True)
    
    # Quick Stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Bank Nifty", "45,678.90", "+245.60")
    with col2:
        st.metric("PCR", "0.92", "-0.03")
    with col3:
        st.metric("IV", "65.4%", "↑ High")
    with col4:
        st.metric("Max Pain", "45,600", "")
    
    # Sample chart
    st.subheader("Sample Analysis Chart")
    data = pd.DataFrame({
        'Strike': np.arange(45000, 46000, 100),
        'Call_OI': np.random.randint(1000, 50000, 10),
        'Put_OI': np.random.randint(1000, 50000, 10)
    })
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data['Strike'], y=data['Call_OI'], name='Call OI', marker_color='green'))
    fig.add_trace(go.Bar(x=data['Strike'], y=data['Put_OI'], name='Put OI', marker_color='red'))
    st.plotly_chart(fig, use_container_width=True)

elif selected == "Option Chain":
    st.title("🔍 Option Chain Analysis")
    st.info("This feature requires Zerodha API connection")

elif selected == "Paper Trading":
    st.title("💰 Paper Trading Simulator")
    st.success("Virtual trading with ₹1,00,000 capital")

st.markdown("---")
st.markdown("**App created without any local installation!**")
