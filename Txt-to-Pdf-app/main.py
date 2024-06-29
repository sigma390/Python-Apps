from fpdf import FPDF
import pandas as pd
from pathlib import Path
import glob

filepaths = glob.glob("Txt/*.txt")






for filepath in filepaths:
    df = pd.read_csv(filepath)
    filename = Path(filepath).stem
    print(filename)
    #create PDF object
    pdf = FPDF(orientation="P",unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", size=16 , style="B")
    #add Filename as First Cell
    pdf.cell(w=50, h=10, txt=filename, ln=1)

    #read and add all text as single string and push to pdf file

    with open(filepath,"r") as file:
        content = file.read()
    pdf.set_font(family="Times",size=10)
    pdf.multi_cell(w=0,h=8,txt=content)




    #output
    pdf.output(f"Outputs/{filename}.pdf")

print(df)

