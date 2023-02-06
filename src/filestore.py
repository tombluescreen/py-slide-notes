import os
import pathlib

BASE_FILE_PATH = "./cache.beans"

def is_base_path_valid():
    return os.path.exists(BASE_FILE_PATH)


def init_base_path():
    if is_base_path_valid() == False:
        os.mkdir(BASE_FILE_PATH)


def save_file_cache(plain_imgs, marked_imgs, tess_data, pdf_data, og_pdf_path, save_name = None):
    
    init_base_path()
    pdf_path = pathlib.Path(og_pdf_path)
    base_path = pathlib.Path(BASE_FILE_PATH)
    
    if save_name == None:
        save_name = pdf_path.name
    
    save_name = save_name + str(hash(save_name))

    save_path = pathlib.Path(f"{base_path}/{save_name}")

    save_path.mkdir()

    print(f"Saving to {save_path}")

    plain_path = pathlib.Path(f"{save_path}/plain")
    plain_path.mkdir()
    marked_path = pathlib.Path(f"{save_path}/marked")
    marked_path.mkdir()

    for img in range(len(plain_imgs)):
        plain_imgs[img].save(f"{plain_path}/{img}.png")
    
    for img in range(len(marked_imgs)):
        marked_imgs[img].save(f"{marked_path}/{img}.png")

    f = open(f"{save_path}/tess_data.csv", "x")
    for row in tess_data:
        f.write(",".join(row) + "\n")
    #f.write(str(tess_data))
    f.close()

    f = open(f"{save_path}/pdf_data", "x")
    f.write("\n".join(pdf_data))
    f.close()

    print(f"Save complete")
    


def read_file_cache():
    pass