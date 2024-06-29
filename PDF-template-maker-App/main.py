from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
#set false to avoid auto page breakage
pdf.set_auto_page_break(auto=False, margin=0)

user = input()
#use dataframe

df = pd.read_csv("topics.csv")
for index, rows in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    #add heading
    pdf.set_text_color(100,100,100)
    #add a Heading
    pdf.cell(w=0, h=12, txt=rows['Topic'], align="L", ln=1)

    #add lines and also , take step as 10 and 200 is width , also y represent height
    for y in range (20,298,10):
        pdf.line(10, y,200,y)


    pdf.ln(248) #means WHITESPACE

    #add footer
    pdf.set_font(family="Times", style="I", size=12)
    pdf.cell(w=0, h=12, txt=rows['Topic'], align="R", ln=1)
    pdf.cell(w=0, h=12, txt="created by " + user, align="R", ln=1)
    pdf.cell(w=0, h=12, txt="user", align="R", ln=1)
    pdf.set_text_color(100, 100, 100)



    for i in range(int(rows['Pages'])-1):
        pdf.add_page()
        pdf.ln(258)

        pdf.set_font(family="Times", style="I", size=12)
        pdf.cell(w=0, h=12, txt=rows['Topic'], align="R", ln=1)
        pdf.cell(w=0, h=10, txt="created by " + user, align="R", ln=1)
        pdf.set_text_color(100, 100, 100)
        # add lines and also , take step as 10 and 200 is width , also y represent height
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("Topics.pdf")





