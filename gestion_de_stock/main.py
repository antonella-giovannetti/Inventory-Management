import tkinter as tk     
from classes.CRUD import CRUD
from tkinter import ttk
window = tk.Tk()   
window.geometry("800x800")

crud = CRUD()
categories = crud.readCategories()
display_page = False

# Fenêtre d'ajout d'un produit
def add_product():
    add_window = tk.Toplevel(window)
    add_window.geometry("400x400")
    add_window.title("Ajouter un produit")

    label_name = tk.Label(add_window, text="Nom :")
    label_name.pack()
    entry_name = tk.Entry(add_window)
    entry_name.pack()

    label_description = tk.Label(add_window, text="Description :")
    label_description.pack()
    entry_description = tk.Entry(add_window)
    entry_description.pack()

    label_price = tk.Label(add_window, text="Prix en € :")
    label_price.pack()
    entry_price = tk.Entry(add_window)
    entry_price.pack()

    label_quantity = tk.Label(add_window, text="Quantité :")
    label_quantity.pack()
    entry_quantity = tk.Entry(add_window)
    entry_quantity.pack()

    label_category = tk.Label(add_window, text="Catégorie :")
    label_category.pack()
    category_var = tk.StringVar()
    category_dropdown = ttk.Combobox(add_window, textvariable=category_var, values=categories)
    category_dropdown.pack()
    category_dropdown.config(state="readonly")

    button_save = tk.Button(add_window, text="Enregistrer", bg="gray", fg="white", padx=5, pady=5, bd=0, activebackground="light gray", command=lambda: save_product(entry_name.get(), entry_description.get(),entry_price.get(), entry_quantity.get(), category_var.get(), add_window))
    button_save.pack(pady=20)

# Sauvegarde le produit
def save_product(name, description, price, quantity, category, add_window):
    if category == "Chaussures":
        id_category = 1
    elif category == "Vêtements":
        id_category = 2
    elif category == "Accessoires":
        id_category = 3
    crud.createProduct(name, description, price, quantity, id_category)
    add_window.destroy() 
    home()  

# Fenêtre de modification de produit
def modify_product(product):
    add_window = tk.Toplevel(window)
    add_window.geometry("400x400")
    add_window.title("Modifier un produit")

    label_name = tk.Label(add_window, text="Nom :")
    label_name.pack()
    entry_name = tk.Entry(add_window)
    entry_name.pack()
    entry_name.insert(0, product[1])

    label_description = tk.Label(add_window, text="Description :")
    label_description.pack()
    entry_description = tk.Entry(add_window)
    entry_description.pack()
    entry_description.insert(0, product[2])

    label_price = tk.Label(add_window, text="Prix en € :")
    label_price.pack()
    entry_price = tk.Entry(add_window)
    entry_price.pack()
    entry_price.insert(0, product[3])

    label_quantity = tk.Label(add_window, text="Quantité :")
    label_quantity.pack()
    entry_quantity = tk.Entry(add_window)
    entry_quantity.pack()
    entry_quantity.insert(0, product[4])

    label_category = tk.Label(add_window, text="Catégorie :")
    label_category.pack()
    category_var = tk.StringVar()
    category_dropdown = ttk.Combobox(add_window, textvariable=category_var, values=categories)
    category_dropdown.pack()
    category_dropdown.insert(0, product[5])
    category_dropdown.config(state="readonly")
    button_save = tk.Button(add_window, text="Enregistrer", bg="gray", fg="white", padx=5, pady=5, bd=0, activebackground="light gray", command=lambda: update_product(entry_name.get(), entry_description.get(),entry_price.get(), entry_quantity.get(), category_var.get(), product[0], add_window))
    button_save.pack(pady=20)

# Met à jour le produit modifié
def update_product(name, description, price, quantity, category,  id_product, add_window):
    if category == "Chaussures":
        id_category = 1
    elif category == "Vêtements":
        id_category = 2
    elif category == "Accessoires":
        id_category = 3
    crud.updateProduct(name, description, price, quantity, id_category, id_product)
    add_window.destroy()
    home() 

# Suppression d'un produit 
def delete_product(id):
    crud.deleteProduct(id)
    home()

# Fenêtre principal
def home():
    # destroy previous content in main_frame
    for widget in window.winfo_children():
        widget.destroy()

    # Canva
    canvas = tk.Canvas(window, height=500)
    canvas.pack(side="left", fill="both", expand=True)

    # Scroll bar
    scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

    main_frame = tk.Frame(canvas)
    canvas.create_window((0,0), window=main_frame, anchor="nw")

    # Contenu de ma fenêtre
    title = tk.Label(main_frame, text="Nos produits", font=("Arial", 20), justify="left")
    title.pack(padx=20, pady=10, anchor="w")

    button_add_products = tk.Button(main_frame, text="Ajouter un produit", font=("Arial", 13), bg="gray", fg="white", padx=5, pady=5, bd=0, activebackground="light gray", command=add_product)
    button_add_products.pack(padx=20, pady=10, anchor="w")

    for categorie in categories:
        title_products = tk.Label(main_frame, text = categorie, font=("Arial", 15))
        title_products.pack(padx=20, pady=10, anchor="w")
        products = crud.readProductsByCategory(categorie)
        for product in products:
            product_frame = tk.Frame(main_frame)
            product_frame.pack(fill="x", padx=20, pady=10)

            name_label = tk.Label(product_frame, text=product[1], font=("Arial", 12), width=18, anchor="w")
            name_label.pack(side="left")

            description_label = tk.Label(product_frame, text=product[2], font=("Arial", 12), width=18, anchor="w")
            description_label.pack(side="left")

            price_label = tk.Label(product_frame, text=str(product[3]) + "€", font=("Arial", 12), width=5, anchor="e")
            price_label.pack(side="left")

            quantity_label = tk.Label(product_frame, text=str(product[4]), font=("Arial", 12), width=5)
            quantity_label.pack(side="left", anchor="e")

            button_modify = tk.Button(product_frame, text="Modifier", bg="blue", fg="white", padx=5, pady=5, bd=0, activebackground="light gray",  command=lambda p=product: modify_product(p))
            button_modify.pack(side="right", padx=10)

            button_delete = tk.Button(product_frame, text="Supprimer", bg="red", fg="white", padx=5, pady=5, bd=0, activebackground="light gray", command=lambda p=product: delete_product(p[0]))
            button_delete.pack(side="right", padx=10)

    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'))

home()
window.mainloop()
crud.cursor.close()
crud.connection.close()