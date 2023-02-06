from PyPDF2 import PdfReader
import cv2
import pytesseract
import pdf2image
from PIL import Image, ImageDraw
import csv

def tess_list_to_ana_dict(tess_list) -> dict:
    header_line = tess_list[0]
    out_dict = {}
    
    for header in header_line:
        out_dict[header] = []
        for i in range(len(tess_list[1:])):
            out_dict[header].append(tess_list[1:][i][header_line.index(header)])
    return out_dict

# ---- TODO ------
def ana_dict_to_tess_list(ana_dict: dict, OUTPUT_ORDER = ["level", "page_num", "block_num", "par_num", "line_num", "word_num", "left", "top", "width", "height", "conf", "text"]) -> list:
    
    out_list = [""] * len(list(ana_dict.values())[0])
    for ele in range(len(out_list)):
        out_list[ele] = [""] * len(OUTPUT_ORDER)
    #out_list[len(OUTPUT_ORDER)] = "beans"
    #out_list.insert(len(OUTPUT_ORDER), "beans")
    for key, val in ana_dict.items():
        # preserve list index's
        
        found_index = OUTPUT_ORDER.index(key)
        ctr = 0
        for v in val:
            out_list[ctr][found_index] = v
            ctr += 1
    return out_list
    

def debug_draw_tess_to_image(image: Image, page_number, tess_data = "NONE"):
    config = ('-l eng --oem 1 --psm 3')
    res = {}
    if tess_data == "NONE":
        print("DEBUG: Tess data NOT given...\n\t Generating...")
        res = pytesseract.image_to_data(image, config=config, output_type=pytesseract.Output.DICT)

    elif type(tess_data) is list:
        print("DEBUG: Tess data given...\n\t Converting to dict...")
        res = tess_list_to_ana_dict(tess_data)
    elif type(tess_data) is dict:
        print("DEBUG: Tess data given...")
        

    #ana_dict_to_tess_list(res)
    # draw blocks
    #max_page = res["page_num"][-1]
    #for page_num in range(max_page)+1:
    #    if page_num



    max_block = res["block_num"][-1]
    dr_img = ImageDraw.Draw(image)
    bl = 0
    pr = 0
    ln = 0
    wd = 0
    for i in range(len(res["block_num"])):
        if int(res["page_num"][i])-1 == page_number:
            open_block = res["block_num"][i]
            if bl == open_block:
                mar = 30
                shape = [res["left"][i]-mar, res["top"][i]-mar, res["width"][i]+res["left"][i]+mar, res["height"][i]+res["top"][i]+mar]
                dr_img.rectangle(shape, outline="green")
                pr = 0
                ln = 0
                wd = 0
                bl+=1

            if pr == res["par_num"][i]:
                mar = 15
                shape = [res["left"][i]-mar, res["top"][i]-mar, res["width"][i]+res["left"][i]+mar, res["height"][i]+res["top"][i]+mar]
                dr_img.rectangle(shape, outline="red")
                ln = 0
                wd = 0
                pr += 1

            if ln == res["line_num"][i]:
                mar = 10
                shape = [res["left"][i]-mar, res["top"][i]-mar, res["width"][i]+res["left"][i]+mar, res["height"][i]+res["top"][i]+mar]
                dr_img.rectangle(shape, outline="blue")
                wd = 0
                ln += 1

            if wd == res["word_num"][i]:
                mar = 0
                shape = [res["left"][i]-mar, res["top"][i]-mar, res["width"][i]+res["left"][i]+mar, res["height"][i]+res["top"][i]+mar]
                dr_img.rectangle(shape, outline="orange")
                wd+=1
    
    #image.show()
    print("beans")

def pdf_to_img(pdf_file):
    
    return pdf2image.convert_from_path(pdf_file)

def pypdf_extract_text(pdf_path):
    output = []
    with open(pdf_path, 'rb') as f:
        pdf = PdfReader(f)
        #information = pdf.metadata
        #number_of_pages = len(pdf.pages)
        for page in pdf.pages:
            output.append(page.extract_text())
    return output

def tess_get_data(image):
    config = ('-l eng --oem 1 --psm 3')

    

    if type(image) is list:
        f_row = []
        page_num = 0
        first_flag = False
        for img in image:
            res = pytesseract.image_to_data(img, config=config)
            rows = str.split(res, "\n")
            if first_flag:
                rows.pop(0)
            
            rows.pop(len(rows)-1)
            for row in rows:
                temp = str.split(row, "\t")
                if first_flag:

                    temp[1] = str(page_num)
                f_row.append(temp)
            page_num+=1
            first_flag = True
            
        return f_row
    else:
        res = pytesseract.image_to_data(image, config=config)
        rows = str.split(res, "\n")
        f_row = []
        for row in rows:
            f_row.append(str.split(row, "\t"))
        
        f_row.pop(len(f_row)-1)
        return f_row
    