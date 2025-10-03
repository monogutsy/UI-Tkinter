import tkinter as tk
from tkinter import *
from tkinter import font

# main window
window = tk.Tk()
window.title("Menu")
window.geometry("650x700")
window.configure(bg="#f5ebe4")  


def menu_list():

    # Fonts
    title_font = font.Font(family="Arial", size=15, weight="bold")
    section_font = font.Font(family="Arial", size=9, weight="bold")
    item_font = font.Font(family="Arial", size=8)
    price_font = font.Font(family="Arial", size=7, weight="bold")

    title_label = tk.Label(window, text="MENU", font="Georgia 20 bold", bg="#f5ebe4")
    title_label.pack(pady=10)

    separator = tk.Frame(window, height=4, bd=1, relief="sunken", bg="black")
    separator.pack(fill="x", padx=3, pady=3)

    #container
    container = tk.Frame(window, bg="#f5ebe4")
    container.pack(fill="both", expand=True)

    #Left frame
    left_frame = tk.Frame(container, bg="#f5ebe4")
    left_frame.pack(side="left", fill="both", expand=True)

    #Right frame
    right_frame = tk.Frame(container, bg="#f5ebe4")
    right_frame.pack(side="right", fill="both", padx=10, pady=10)


    #HOT COFFEE SELECTION
    hot_coffee_label = tk.Label(left_frame, text="HOT COFFEE:", font=section_font, bg="#f5ebe4")
    hot_coffee_label.pack(anchor="w", padx=35, pady=(10, 0))

    left_items_frame = tk.Frame(left_frame, bg="#f5ebe4")
    left_items_frame.pack(anchor="w", padx=40, pady=10)

    #Americano Item
    americano = tk.Checkbutton(left_items_frame,text="      Americano\t\t 0.00 php", font=item_font, bg="#f5ebe4")
    americano.grid(row=0, column=0, columnspan=3, sticky="w")

    #Cappuccino
    capuccino = tk.Checkbutton(left_items_frame,text="      Capuccino\t\t 0.00 php", font=item_font, bg="#f5ebe4")
    capuccino.grid(row=1, column=0, columnspan=3, sticky="w")

    #Caffe Machiato
    macchiato = tk.Checkbutton(left_items_frame,text="      Caffe Macchiato\t 0.00 php", font=item_font, bg="#f5ebe4")
    macchiato.grid(row=2, column=0, columnspan=3, sticky="w")

    #Flat White
    flatwhite = tk.Checkbutton(left_items_frame,text="      Flat White\t\t 0.00 php", font=item_font, bg="#f5ebe4")
    flatwhite.grid(row=3, column=0, columnspan=3, sticky="w")

    #Latte
    latte = tk.Checkbutton(left_items_frame,text="      Latte\t\t\t 0.00 php", font=item_font, bg="#f5ebe4")
    latte.grid(row=4, column=0, columnspan=3, sticky="w")

    #Mocha
    mocha = tk.Checkbutton(left_items_frame,text="      Mocha\t\t 0.00 php", font=item_font, bg="#f5ebe4")
    mocha.grid(row=5, column=0, columnspan=3, sticky="w")

    #ICED COFFEE SELECTION
    iced_coffee_label = tk.Label(left_frame, text="ICED COFFEE:", font=section_font, bg="#f5ebe4")
    iced_coffee_label.pack(anchor="w", padx=35, pady=(10, 0))

    #frame
    iced_items_frame = tk.Frame(left_frame, bg="#f5ebe4")
    iced_items_frame.pack(anchor="w", padx=40, pady=10)

    #Caramel Macchiato
    caramel_m = tk.Checkbutton(iced_items_frame,text="      Caramel Macchiato\t 0.00 php", font=item_font, bg="#f5ebe4")
    caramel_m.grid(column=0, columnspan=3, sticky="w")

    #Iced Brew
    iced_brew = tk.Checkbutton(iced_items_frame,text="      Iced Brew\t\t 0.00 php", font=item_font, bg="#f5ebe4")
    iced_brew.grid(column=0, columnspan=3, sticky="w")

    #Iced Americano
    iced_americano = tk.Checkbutton(iced_items_frame,text="      Iced Americano\t\t 0.00 php", font=item_font, bg="#f5ebe4")
    iced_americano.grid(column=0, columnspan=3, sticky="w")

    #Latte
    latte = tk.Checkbutton(iced_items_frame,text="      Latte\t\t\t 0.00 php", font=item_font, bg="#f5ebe4")
    latte.grid(column=0, columnspan=3, sticky="w")

    #Frappe
    frappe = tk.Checkbutton(iced_items_frame,text="      Frappe\t\t 0.00 php", font=item_font, bg="#f5ebe4")
    frappe.grid(column=0, columnspan=3, sticky="w")



    #TEA
    tea_coffee_label = tk.Label(right_frame, text="TEA:", font=section_font, bg="#f5ebe4")
    tea_coffee_label.pack(anchor="w", padx=35, pady=(0, 0))

    tea_items_frame = tk.Frame(right_frame, bg="#f5ebe4")
    tea_items_frame.pack(anchor="w", padx=40, pady=10)

    #Iced Tea
    iced_tea = tk.Checkbutton(tea_items_frame,text="      Iced Tea\t\t 0.00 php", font=item_font, bg="#f5ebe4")
    iced_tea.grid(column=0, columnspan=3, sticky="w")

    #Matcha Latte
    matcha_latte = tk.Checkbutton(tea_items_frame,text="      Matcha Latte\t\t 0.00 php", font=item_font, bg="#f5ebe4")
    matcha_latte.grid(column=0, columnspan=3, sticky="w")

    #Lemon Tea
    lemon_tea = tk.Checkbutton(tea_items_frame,text="      Lemon Tea\t\t 0.00 php", font=item_font, bg="#f5ebe4")
    lemon_tea.grid(column=0, columnspan=3, sticky="w")

    #Milk Tea
    milk_tea = tk.Checkbutton(tea_items_frame,text="      Milk Tea\t\t 0.00 php", font=item_font, bg="#f5ebe4")
    milk_tea.grid(column=0, columnspan=3, sticky="w")




    #SNACKS
    snacks_label = tk.Label(right_frame, text="SNACKS:", font=section_font, bg="#f5ebe4")
    snacks_label.pack(anchor="w", padx=35, pady=(0, 0))

    snacks_items_frame = tk.Frame(right_frame, bg="#f5ebe4")
    snacks_items_frame.pack(anchor="w", padx=40, pady=10)

    #Fries
    fries = tk.Checkbutton(snacks_items_frame,text="      Fries\t\t\t 0.00 php", font=item_font, bg="#f5ebe4")
    fries.grid(column=0, columnspan=3, sticky="w")

    #Cookies
    cookies = tk.Checkbutton(snacks_items_frame,text="      Cookies\t\t 0.00 php", font=item_font, bg="#f5ebe4")
    cookies.grid(column=0, columnspan=3, sticky="w")

    #Cupcake
    cupcake = tk.Checkbutton(snacks_items_frame,text="      Cupcake\t\t 0.00 php", font=item_font, bg="#f5ebe4")
    cupcake.grid(column=0, columnspan=3, sticky="w")

    #Bread
    bread = tk.Checkbutton(snacks_items_frame,text="      Bread\t\t\t 0.00 php", font=item_font, bg="#f5ebe4")
    bread.grid(column=0, columnspan=3, sticky="w")

    #Extra
    extra = tk.Button(snacks_items_frame,text="Extra",relief=FLAT)
    extra.grid(column=0,columnspan=3, sticky="w")


menu_list()


window.mainloop()

