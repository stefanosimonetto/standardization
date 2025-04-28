# streamlit_app.py
# Run this with: streamlit run streamlit_app.py

import streamlit as st

st.title("🛡️ Threat intelligence Standardization Dashboard")

# Inputs Section
st.header("Inputs")
cve_id = st.text_input("CVE-ID", placeholder="e.g., CVE-2025-12345")
enisa_id = st.text_input("ENISA-ID (optional)")
japan_id = st.text_input("Japan-ID (optional)")

st.markdown("---")

# Text & Embeddings Section
st.header("Text & Embeddings")
text_options = st.multiselect(
    "Select information to retrieve:",
    ["Original Text", "Bert embeddings", "Embedding for CVE-to-CWE", "Embedding for CVE-to-CAPEC"],
    default=["Original Text"]
)

st.markdown("---")

# Scoring & Classification Section
st.header("Scoring & Classification")
classification_options = st.multiselect(
    "Select classification and scoring options:",
    ["CVSS Score", "EPSS", "Source-provided Mappings (CWE-NIST, CWE-CNA, CWE-Japan)"],
    default=["CVSS Score"]
)

st.markdown("---")


# Scoring & Classification Section
st.header("CWE & CAPEC & MITRE ATT&CK")
classification_options = st.multiselect(
    "Select the CWE & CAPEC & MITRE ATT&CK options:",
    ["CWE", "CWE view 1003 (Adopted by NIST experts)" "CAPEC", "MITRE ATT&CK"],
    default=["CWE"]
)
st.markdown("---")



# Output Section
st.header("Output")
st.write("The output will include:")
if "Original Text" in text_options:
    st.write("- Original Text (Description)")
if "CVSS Score" in text_options or "CVSS Score" in classification_options:
    st.write("- CVSS Score")
if "EPSS" in text_options or "EPSS" in classification_options:
    st.write("- EPSS Score")
if "KEV" in text_options or "KEV" in classification_options:
    st.write("- Known Exploited Vulnerabilities (KEV) data")
if "Source-provided Mappings (CWE-NIST, CWE-CNA, CWE-Japan)" in classification_options:
    st.write("- Best CWE Mapping")

# Download buttons
st.download_button("Download JSON", data="{}", file_name="cve_profile.json", mime="application/json")
st.download_button("Download Excel", data=b"", file_name="cve_profile.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
