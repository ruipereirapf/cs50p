from fpdf import FPDF
from PIL import Image

pdf = FPDF(orientation="portrait", format="A4")

def main():
    name = input("Name: ")
    shirt_str = f"{name} took CS50"
    pdf.add_page()
    pdf.set_font("Times", "B", size=50)
    pdf.cell(text="CS50 Shirtificate", center=True)
    img = Image.open("shirtificate.png")
    pdf.image(img, x=0, y=60)
    pdf.set_xy((pdf.w /2) - 50, (pdf.h /2) - 25)
    pdf.set_font("Times", "B", size=30,)
    pdf.set_text_color(255,255,255)
    pdf.cell(text=shirt_str)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
