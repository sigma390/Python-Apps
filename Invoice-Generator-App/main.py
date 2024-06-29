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
    pdf= FPDF(orientation="P", format="A4", unit="mm" )
    pdf.add_page()
    pdf.set_font(family="Times", size=18, style="B")
    #add sr
    pdf.cell(w=50, h=8, txt="Invoice Sr : "+invoiceSr, ln=1)
    # add date
    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=50, h=8, txt="Date : "+Datee, ln=1)

    #add header
    cols = list(df.columns)
    print(cols[len(cols)-1])
    for i in cols:
        pdf.set_font(family="Times", size=10, style="B")
        pdf.cell(w=35, h=8, txt=str(i), border=1)
    pdf.ln()
    print(cols)


    #add rows or fill rows
    for index, row in df.iterrows():
        for col in cols:
            pdf.set_font(family="Times", size=10)
            pdf.cell(w=35, h=8, txt=str(row[col]), border=1)
        pdf.ln()

    pdf.set_font(family="Times", size=16,style="B")
    totalsum = df["total_price"].sum()
    pdf.cell(w=70,h=10,txt="Total is : "+str(totalsum))









    pdf.output(f"Invoices-Pdf/{invoiceSr}.pdf")


