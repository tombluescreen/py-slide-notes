import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def launch_gui(images: Image):
    root = tk.Tk()
    img_container = ttk.Frame(root)
    img_canvas = tk.Canvas(img_container)
    img_scrollbar = ttk.Scrollbar(img_container, orient="vertical", command=img_canvas.yview)
    img_scrollable_frame = ttk.Frame(img_canvas)

    img_scrollable_frame.bind(
        "<Configure>",
        lambda e: img_canvas.configure(
            scrollregion=img_canvas.bbox("all")
        )
    )
    

    img_canvas.create_window((0, 0), window=img_scrollable_frame, anchor="nw")

    img_canvas.configure(yscrollcommand=img_scrollbar.set)

    i = 0
    for img in images:


        tkimg = ImageTk.PhotoImage(img.resize((500,500)))
        #tkimg = tkimg.resize((500,500))
        img1 = tk.Label(img_scrollable_frame, image=tkimg, width=500, height=500)
        img1.photo = tkimg
        #img1.place(x=0, y=100*i)
        img1.grid(row=i,column=0, columnspan=1)
        
        # https://www.tutorialspoint.com/python/tk_text.htm
        tess_text = tk.Text(img_scrollable_frame, width=50)
        tess_text.insert(tk.INSERT, "BEANS")

        pdf_text = tk.Text(img_scrollable_frame, width=50)
        pdf_text.insert(tk.INSERT, "bruh")

        clean_text = tk.Text(img_scrollable_frame, width=100)
        clean_text.insert(tk.INSERT, "huh")
        var1 = tk.IntVar()
        c1 = tk.Checkbutton(img_scrollable_frame, text='Python',variable=var1, onvalue=1, offvalue=0)#, command=print_selection)
        c1.grid(row=i, column=2)



        tess_text.grid(row=i,column=1, columnspan=1, sticky="NSEW")
        pdf_text.grid(row=i,column=3, columnspan=1,  sticky="NSEW")
        clean_text.grid(row=i,column=4,columnspan=2, sticky="NSEW")
        
        #entry.pack(fill="both", side="right")
        i += 1

    img_container.pack(fill="both", expand=True)
    img_canvas.pack(side="left", fill="both", expand=True)
    img_scrollbar.pack(side="right", fill="y")
    #img_scrollable_frame.pack(fill="both")

    root.mainloop()