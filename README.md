## Gold Standard Project Design Document (PDD) Generator
 ## Project Overview

This project is an AI-assisted agent that automatically drafts a Gold Standard Project Design Document (PDD) in the official format and tone.
Once a user selects the Project Type (e.g., Renewable Energy, Cookstove, Forestry, Biogas) and Gold Standard version, the system generates a pre-populated, professional draft of the PDD.

The generated document follows the official Gold Standard PDD structure (Sections A–E) and can be downloaded as a .docx file that matches the provided Gold Standard template.

This project works offline — it does not require any API keys.

## HOW TO RUN

1. Install dependencies:
   pip install -r requirements.txt

2. Ensure the file "GoldStandard_PDD_Template.docx"
   (your official PDD reference template) is in this folder.

3. Start the Streamlit app:
   streamlit run app.py

4. Select:
   - Project Type (Solar / Cookstove / Forestry / Biogas)
   - Gold Standard Version (GS4GG v1.5 or Legacy CDM)
   - Click "Generate PDD Draft"

5. Review the generated PDD text preview.

6. Click "Download Gold Standard PDD (.docx)"
   → Your filled official Gold Standard Project Design Document
     will be downloaded instantly.

## OUTPUT FILES

- PDD_Renewable_Energy_(Solar_Power_Project).docx
- PDD_Improved_Cookstove_Project.docx
- PDD_Forestry_/_Reforestation_Project.docx
- PDD_Biogas_Energy_Project.docx
