import analysis as ana
import gui as gui
import filestore as fs

def find_likely_header():
    # Likely the first text in pdf ana
    # Likely the biggest text from tess
    pass

def parse_page(page_num, text_list, image_list):

    res = ana.tess_get_data(image_list[page_num])
    #f = open("testFILE.csv", "w")
    #f.write(res)
    #f.close()

def init_pdf(pdf_path):
    conv_images = ana.pdf_to_img(pdf_path)
    pdf_text = ana.pypdf_extract_text(pdf_path)
    return (conv_images, pdf_text)

if __name__ == '__main__':
    # pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    path = '.././testpdf2.pdf'
    imgs_marked,texts = init_pdf(path)
    
    imgs_plain = []
    
    tess_data = ana.tess_get_data(imgs_marked)

    # ana.debug_draw_tess_to_image(imgs[4])
    for i in range(len(imgs_marked)):
        imgs_plain.append(imgs_marked[i].copy())
        ana.debug_draw_tess_to_image(imgs_marked[i],i,tess_data=tess_data)

    fs.save_file_cache(imgs_plain, imgs_marked, tess_data, texts,path)
    #parse_page(2, texts, imgs)

    gui.launch_gui(imgs_marked)

    
    #extract_information(path)