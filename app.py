from __future__ import annotations

import json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

from data import ARTICLE_RESULTS, BOM, PV_MONTHS, THESIS_DAILY, THESIS_TOTALS

BASE_DIR = Path(__file__).resolve().parent


def build_dashboard() -> str:
    """Load the self-contained animated dashboard and inject source data."""
    template = (BASE_DIR / "dashboard.html").read_text(encoding="utf-8")
    daily = [
        {"doy": day, "tracker": tracker, "fixed": fixed, "gain": gain}
        for day, tracker, fixed, gain in THESIS_DAILY
    ]
    replacements = {
        "__THESIS_DAILY_DATA__": json.dumps(daily, separators=(",", ":")),
        "__PV_MONTHS__": json.dumps(PV_MONTHS, separators=(",", ":")),
        "__ARTICLE_RESULTS__": json.dumps(ARTICLE_RESULTS, separators=(",", ":")),
        "__THESIS_TOTALS__": json.dumps(THESIS_TOTALS, separators=(",", ":")),
        "__BOM_DATA__": json.dumps(BOM, separators=(",", ":")),
    }
    for token, value in replacements.items():
        if token not in template:
            raise RuntimeError(f"Missing dashboard data token: {token}")
        template = template.replace(token, value)
    return template


def main() -> None:
    st.set_page_config(
        page_title="Solar Lab · Dual-Axis Tracker",
        page_icon="☀️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    st.markdown(
        """
        <style>
        [data-testid="stHeader"], [data-testid="stToolbar"], footer {display:none !important;}
        [data-testid="stAppViewContainer"], [data-testid="stMain"] {background:#f3f7f3;}
        .block-container {padding:0 !important; max-width:100% !important;}
        iframe {border:0 !important;}
        </style>
        """,
        unsafe_allow_html=True,
    )
    components.html(build_dashboard(), height=5200, scrolling=True)


if __name__ == "__main__":
    main()
