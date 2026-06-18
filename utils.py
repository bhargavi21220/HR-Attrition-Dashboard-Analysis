import streamlit as st
import base64

def set_background(image_file):

    st.markdown(
        """
        <style>

        .stApp {
            background: linear-gradient(
                135deg,
                #000000,
                #111827,
                #1f2937
            );
        }

        [data-testid="stAppViewContainer"] {
            background: linear-gradient(
                135deg,
                #000000,
                #111827,
                #1f2937
            );
        }

        .block-container {
            background: transparent;
            padding: 2rem;
        }

        h1, h2, h3, h4, h5, h6 {
            color: white !important;
        }

        p, label, span, div {
            color: white !important;
        }

        section[data-testid="stSidebar"] {
            background-color: #0f172a;
        }

        section[data-testid="stSidebar"] * {
            color: white !important;
        }

        [data-testid="metric-container"] {
            background: rgba(0,0,0,0.55);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 15px;
            padding: 20px;
        }

        [data-testid="metric-container"] * {
            color: white !important;
        }

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }

        </style>
        """,
        unsafe_allow_html=True
    )