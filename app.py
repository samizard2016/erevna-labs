import os

import streamlit as st
from streamlit_navigation_bar import st_navbar

import pages as pg


pages = ["Statistical", "Machine Learning", "PGM", "SEM", "Causal Inference","Deep Learning", "GitHub"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "erevnalab.svg")
st.set_page_config(initial_sidebar_state="collapsed")

urls = {"GitHub": "https://github.com/samizard2016/erevna-labs"}
styles = {
    "nav": {
        "background-color": "grey",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "background-color": "black",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
    }
}
options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    logo_path=logo_path,
    urls=urls,
    styles=styles,
    options=options,
)

functions = {
    "Home": pg.show_home,
    "Statistical": pg.show_stat,
    "Machine Learning": pg.show_ML,
    "PGM": pg.show_PGM,
    "SEM": pg.show_SEM,
    "Causal Inference": pg.show_CI,
    "Deep Learning": pg.show_DL,   
}
go_to = functions.get(page)
if go_to:
    go_to()