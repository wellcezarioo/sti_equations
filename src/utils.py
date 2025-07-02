import streamlit as st
import extra_streamlit_components as stx

@st.fragment
def get_manager():
    return stx.CookieManager()

cookie_manager = get_manager()
cookies = cookie_manager.get_all()