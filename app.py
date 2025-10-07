import streamlit as st
from template_filler import generate_pdd_docx


PDD_DRAFTS = {
    "Renewable Energy (Solar Power Project)": """
A. PROJECT DESCRIPTION
The project involves installation of a 5 MW grid-connected solar photovoltaic (PV) power plant in Rajasthan, India. The project will generate renewable electricity and supply it to the state grid, replacing fossil-fuel-based generation. This initiative will mitigate approximately 7,200 tCO₂e annually while supporting India’s clean energy transition. The project contributes to national renewable energy goals and sustainable rural employment.

B. APPLICATION OF METHODOLOGY AND SDG CONTRIBUTIONS
Applied Methodology: AMS-I.D – Grid-connected renewable electricity generation.
Relevant SDGs:
• SDG 7 – Affordable and Clean Energy
• SDG 8 – Decent Work and Economic Growth
• SDG 13 – Climate Action

C. DURATION AND CREDITING PERIOD
Start Date: 01 January 2025
Operational Lifetime: 25 years
Crediting Period: 10 years (renewable)

D. SAFEGUARDING PRINCIPLES AND GENDER ASSESSMENT
The project complies with Gold Standard Safeguarding Principles. It involves no involuntary resettlement or biodiversity harm. Women and marginalized groups will be trained for solar maintenance, improving gender equity and technical skill development.

E. STAKEHOLDER CONSULTATION
Consultations were conducted in August 2024 with local authorities, NGOs, and community members. The feedback was positive, highlighting employment creation, reduced pollution, and access to clean energy.
""",

    "Improved Cookstove Project": """
A. PROJECT DESCRIPTION
The project distributes 10,000 improved biomass cookstoves to rural households in Jharkhand, India. These stoves increase fuel efficiency and reduce indoor air pollution, leading to better health outcomes and an estimated annual emission reduction of 15,000 tCO₂e. The project empowers women by saving time otherwise spent collecting fuelwood.

B. APPLICATION OF METHODOLOGY AND SDG CONTRIBUTIONS
Applied Methodology: GS TPDDTEC v2.0 – Thermal energy for cooking and heating.
Relevant SDGs:
• SDG 3 – Good Health and Well-being
• SDG 5 – Gender Equality
• SDG 13 – Climate Action

C. DURATION AND CREDITING PERIOD
Start Date: 01 April 2024
Operational Lifetime: 10 years
Crediting Period: 7 years

D. SAFEGUARDING PRINCIPLES AND GENDER ASSESSMENT
The project reduces household air pollution, prevents deforestation, and supports women’s empowerment through improved health, reduced workload, and cost savings.

E. STAKEHOLDER CONSULTATION
Consultations were held with village-level communities, NGOs, and women’s groups. Stakeholders expressed strong support due to health, time-saving, and environmental benefits.
""",

    "Forestry / Reforestation Project": """
A. PROJECT DESCRIPTION
This project rehabilitates 500 hectares of degraded land in Karnataka, India, through afforestation with native tree species. It enhances biodiversity, improves soil fertility, and sequesters approximately 20,000 tCO₂e per year, contributing to sustainable ecosystem restoration.

B. APPLICATION OF METHODOLOGY AND SDG CONTRIBUTIONS
Applied Methodology: AR-AMS0007 – Afforestation and Reforestation of degraded lands.
Relevant SDGs:
• SDG 13 – Climate Action
• SDG 15 – Life on Land
• SDG 8 – Decent Work and Economic Growth

C. DURATION AND CREDITING PERIOD
Start Date: 01 March 2025
Operational Lifetime: 30 years
Crediting Period: 20 years

D. SAFEGUARDING PRINCIPLES AND GENDER ASSESSMENT
The project promotes gender inclusion and equal pay for women in nursery operations and plantation work. No land conflicts or displacement are expected.

E. STAKEHOLDER CONSULTATION
Consultations were conducted with farmers, forest officials, and village representatives. Strong community support was noted due to livelihood and environmental restoration benefits.
""",

    "Biogas Energy Project": """
A. PROJECT DESCRIPTION
The project installs 1,000 household-scale biogas units in rural Maharashtra, India. Each digester converts cattle dung into biogas for clean cooking and lighting. The project replaces firewood and LPG consumption, reducing around 8,500 tCO₂e annually and improving rural sanitation.

B. APPLICATION OF METHODOLOGY AND SDG CONTRIBUTIONS
Applied Methodology: AMS-III.R – Methane recovery in agricultural activities.
Relevant SDGs:
• SDG 7 – Affordable and Clean Energy
• SDG 3 – Good Health and Well-being
• SDG 13 – Climate Action

C. DURATION AND CREDITING PERIOD
Start Date: 01 February 2025
Operational Lifetime: 15 years
Crediting Period: 10 years (renewable)

D. SAFEGUARDING PRINCIPLES AND GENDER ASSESSMENT
No adverse environmental or social impacts expected. Women benefit through reduced cooking smoke exposure and opportunities in biogas management and training.

E. STAKEHOLDER CONSULTATION
Community consultations were held with rural households, dairy cooperatives, and local NGOs. Feedback highlighted energy cost savings and reduced dependence on firewood.
"""
}

st.set_page_config(page_title="Gold Standard PDD Generator", page_icon="🌿", layout="wide")
st.title("Gold Standard Project Design Document (PDD) Generator")
st.markdown("""
This agent drafts a **Gold Standard-compliant Project Design Document (PDD)**  
with pre-populated information and the correct tone, structure, and format.
""")

col1, col2 = st.columns(2)
with col1:
    project_type = st.selectbox("Select Project Type", list(PDD_DRAFTS.keys()))
with col2:
    gs_version = st.selectbox("Select Gold Standard Version", ["GS4GG v1.5", "Legacy CDM"])

if st.button("Generate PDD Draft"):
    draft_text = PDD_DRAFTS[project_type]
    st.success("PDD Draft Generated Successfully!")

    st.markdown(f"### Project Type: {project_type}")
    st.text_area("PDD Draft Preview", draft_text, height=450)

    docx_buffer = generate_pdd_docx(draft_text, project_type)

    st.download_button(
        label="Download Gold Standard PDD (.docx)",
        data=docx_buffer,
        file_name=f"PDD_{project_type.replace(' ', '_')}.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

st.info("Compare your draft with approved projects: https://registry.goldstandard.org/projects?q=&page=1")
