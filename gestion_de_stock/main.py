import tkinter as tk     
from classes.CRUD import CRUD
from tkinter import ttk
window = tk.Tk()   
window.geometry("800x800")

crud = CRUD()
categories = crud.readCategories()
display_page = False



# Ajouter un produit dans une autre fenêtre
def add_products():
    add_window = tk.Toplevel(window)
    add_window.geometry("400x300")
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

    button_save = tk.Button(add_window, text="Enregistrer", bg="gray", fg="white", padx=5, pady=5, bd=0, activebackground="light gray", command=lambda: save_product(entry_name.get(), entry_description.get(),entry_price.get(), entry_quantity.get(), category_var.get()))
    button_save.pack(pady=(20,20))

# Sauvegarde le produit
def save_product(name, description, price, quantity, category):
    if category == "Chaussures":
        id_category = 1
    elif category == "Vêtements":
        id_category = 2
    elif category == "Accessoires":
        id_category = 3
    crud.createProduct(name, description, price, quantity, id_category)

# Fenêtre principal
def home():
    title = tk.Label (text = "Nos produits", font=("Arial", 20),  anchor="center", padx=30, pady=30)
    title.pack()
    button_add_products = tk.Button(window, text="Ajouter un produit", font=("Arial", 13), bg="gray", fg="white", padx=5, pady=5, bd=0, activebackground="light gray", command=add_products)
    button_add_products.pack(pady=(20,20))

    for categorie in categories:
        title_products = tk.Label (text = categorie, font=("Arial", 15),  anchor="center", padx=30, pady=30)
        title_products.pack()
        products = crud.readProductsByCategory(categorie)
        for product in products:
            product_frame = tk.Frame(window)
            product_frame.pack(fill="x", padx=10, pady=5)

            name_label = tk.Label(product_frame, text=product[0], font=("Arial", 12))
            name_label.pack(side="left", padx=10)

            material_label = tk.Label(product_frame, text=product[1], font=("Arial", 12))
            material_label.pack(side="left", padx=10)

            price_label = tk.Label(product_frame, text=str(product[2]), font=("Arial", 12))
            price_label.pack(side="left", padx=10)

            quantity_label = tk.Label(product_frame, text=str(product[3]), font=("Arial", 12))
            quantity_label.pack(side="left", padx=10)

            button_modify = tk.Button(window, text="Modifier", bg="blue", fg="white", padx=5, pady=5, bd=0, activebackground="light gray")
            button_modify.pack(pady=(20,20))

            button_delete = tk.Button(window, text="Supprimer", bg="red", fg="white", padx=5, pady=5, bd=0, activebackground="light gray")
            button_delete.pack(pady=(10,10))
home()
window.mainloop()
crud.cursor.close()
crud.connection.close()