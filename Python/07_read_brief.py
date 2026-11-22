from pypdf import PdfReader

pdf = PdfReader("Round2_Brief_Data_Analyst.pdf")

for page_number, page in enumerate(pdf.pages, start=1):
    print(f"\n========== PAGE {page_number} ==========\n")
    print(page.extract_text())