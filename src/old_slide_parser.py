 # Requirements
 # - Parse bullet points/lists correctly (with proper hierarchy)
 # - Extract and link images
 # - Establish header hierarchy
 # - Interpret and convert tables
 # - Preserve hyperlinks
 # - Clean text of whitespace and weird characters
 # - Convert code blocks
 #      - Convert images of code to code blocks 
 # - ? Mark areas where unsure

from PyPDF2 import PdfReader
import cv2
import pytesseract
import pdf2image
from PIL import Image

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfReader(f)
        information = pdf.metadata
        number_of_pages = len(pdf.pages)
        beans = pdf.pages[2].extract_text()
        beans = pdf.pages[2].get_contents().get_data()
    #'  Robotic System Issues\n●Transparency\n●Explanations available\n●Standards\n●All standards embody a principle\n●Ethical Standards\n●ISO and IEEE etc\n●Ethics\n●Ethical implications of technology'
    # '  Robotic System Issues
    # ●Transparency
    # ●Explanations available
    # ●Standards
    # ●All standards embody a principle
    # ●Ethical Standards
    # ●ISO and IEEE etc
    # ●Ethics
    # ●Ethical implications of technology'

    # C:\Program Files\Tesseract-OCR
    
    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    Text: {beans}
    """

    print(txt)
    return information

def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)


def ocr_core(file):
    text = pytesseract.image_to_string(file)
    return text

def image(pdf_path):
    config = ('-l eng --oem 1 --psm 3')
    #img = cv2.imread(pdf_path)
    images = pdf_to_img(pdf_path)
    
    for pg, img in enumerate(images):
        print(ocr_core(img))
        bruh = pytesseract.image_to_data(img)
        print(bruh)
        break
    #text = pytesseract.image_to_string(img, config=config)
    print("df")


if __name__ == '__main__':
    # pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    path = './issues.pdf'
    image(path)
    #extract_information(path)