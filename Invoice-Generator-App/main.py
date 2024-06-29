import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)


#read file paths and store into dataframe
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    #get invoice number
    filename = Path(filepath).stem
    invoiceSr = filename.split("-")[0]
    Datee = filename.split("-")[1]
    #create Pdf
    pdf  = FPDF(orientation="P", format="A4", unit="mm" )
    pdf.add_page()
    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=50, h=8, txt="Invoice Sr : "+invoiceSr, ln=1)
    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=50, h=8, txt="Date : "+Datee)
    pdf.output("invoices-Pdf/Example.pdf")


