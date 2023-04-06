import tkinter as tk     
from classes.CRUD import CRUD
from tkinter import ttk
window = tk.Tk()   
window.geometry("800x800")

crud = CRUD()
categories = crud.readCategories()
category_names = [cat[1] for cat in categories]
display_page = False

# Fenêtre d'ajout d'un produit
def add_product():
    global category_names
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
    category_dropdown = ttk.Combobox(add_window, textvariable=category_var, values=category_names)
    category_dropdown.pack()
    category_dropdown.config(state="readonly")

    button_save = tk.Button(add_window, text="Enregistrer", bg="gray", fg="white", padx=5, pady=5, bd=0, activebackground="light gray", command=lambda: save_product(entry_name.get(), entry_description.get(),entry_price.get(), entry_quantity.get(), category_var.get(), add_window))
    button_save.pack(pady=20)

# Sauvegarde le produit
def save_product(name, description, price, quantity, category, add_window):
    for i in categories:
        if i[1] == category:
            id_category = i[0]
            
    crud.createProduct(name, description, price, quantity, id_category)
    add_window.destroy() 
    home()  

# Fenêtre de modification de produit
def modify_product(product):
    global category_names
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
    category_dropdown = ttk.Combobox(add_window, textvariable=category_var, values=category_names)
    category_dropdown.pack()
    category_dropdown.insert(0, product[5])
    category_dropdown.config(state="readonly")
    button_save = tk.Button(add_window, text="Enregistrer", bg="gray", fg="white", padx=5, pady=5, bd=0, activebackground="light gray", command=lambda: update_product(entry_name.get(), entry_description.get(),entry_price.get(), entry_quantity.get(), category_var.get(), product[0], add_window))
    button_save.pack(pady=20)

# Met à jour le produit modifié
def update_product(name, description, price, quantity, category,  id_product, add_window):
    for i in categories:
        if i[1] == category:
            id_category = i[0]
    crud.updateProduct(name, description, price, quantity, id_category, id_product)
    add_window.destroy()
    home() 

# Suppression d'un produit 
def delete_product(id):
    crud.deleteProduct(id)
    home()

# Fenêtre d'ajout d'une categorie
def add_category():
    add_window = tk.Toplevel(window)
    add_window.geometry("400x400")
    add_window.title("Ajouter une catégorie")

    label_name = tk.Label(add_window, text="Nom :")
    label_name.pack()
    entry_name = tk.Entry(add_window)
    entry_name.pack()

    button_save = tk.Button(add_window, text="Enregistrer", bg="gray", fg="white", padx=5, pady=5, bd=0, activebackground="light gray", command=lambda: save_category(entry_name.get(), add_window))
    button_save.pack(pady=20)

# Sauvegarde la categorie
def save_category(name, add_window):
    print(name)
    crud.createCategory(name)
    add_window.destroy() 
    home()  

# Fenêtre de modification de la categorie
def modify_category(category):
    add_window = tk.Toplevel(window)
    add_window.geometry("400x400")
    add_window.title("Ajouter une catégorie")

    label_name = tk.Label(add_window, text="Nom :")
    label_name.pack()
    entry_name = tk.Entry(add_window)
    entry_name.insert(0, category[1])

    entry_name.pack()

    button_save = tk.Button(add_window, text="Enregistrer", bg="gray", fg="white", padx=5, pady=5, bd=0, activebackground="light gray", command=lambda: update_category(entry_name.get(), category[0], add_window))
    button_save.pack(pady=20)

# Met à jour la catégorie
def update_category(name, id, add_window):
    crud.updateCategory(name, id)
    add_window.destroy()
    home() 

# Suppression de la catégorie
def delete_category(category):
    crud.deleteCategory(category[0])
    home()

# Fenêtre principal
def home():
    categories = crud.readCategories()

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

    button_frame = tk.Frame(main_frame)
    button_frame.pack(padx=20, pady=10, anchor="w")

    button_add_products = tk.Button(button_frame, text="Ajouter un produit", font=("Arial", 13), bg="gray", fg="white", padx=5, pady=5, bd=0, activebackground="light gray", command=add_product)
    button_add_products.pack(side="left", padx=(0, 10))

    button_add_category_names = tk.Button(button_frame, text="Ajouter une catégorie", font=("Arial", 13), bg="gray", fg="white", padx=5, pady=5, bd=0, activebackground="light gray", command=add_category)
    button_add_category_names.pack(side="left", padx=10)

    for category in categories:
        category_frame = tk.Frame(main_frame)
        category_frame.pack(padx=20, pady=10, anchor="w")

        title_products = tk.Label(category_frame, text=category[1], font=("Arial", 15))
        title_products.pack(side="left")

        button_modify_category = tk.Button(category_frame, text="Modifier", bg="gray", fg="white", padx=5, pady=5, bd=0, activebackground="light gray", command=lambda c=category: modify_category(c))
        button_modify_category.pack(side="left", padx=10)

        button_delete_category = tk.Button(category_frame, text="Supprimer", bg="gray", fg="white", padx=5, pady=5, bd=0, activebackground="light gray",  command=lambda c=category: delete_category(c))
        button_delete_category.pack(side="left", padx=10)

        products = crud.readProductsByCategory(category[1])
        for product in products:
            product_frame = tk.Frame(main_frame)
            product_frame.pack(fill="x", padx=20, pady=10)

            name_label = tk.Label(product_frame, text=product[1], font=("Arial", 12), width=18, anchor="w")
            name_label.pack(side="left")

            description_label = tk.Label(product_frame, text=product[2], font=("Arial", 12), width=18, anchor="w")
            description_label.pack(side="left")

            price_label = tk.Label(product_frame, text=str(product[3]) + "€", font=("Arial", 12), width=8, anchor="e")
            price_label.pack(side="left")

            quantity_label = tk.Label(product_frame, text=str(product[4]), font=("Arial", 12), width=8)
            quantity_label.pack(side="left", anchor="e")

            button_modify = tk.Button(product_frame, text="Modifier", bg="blue", fg="white", padx=5, pady=5, bd=0, activebackground="light gray",  command=lambda p=product: modify_product(p))
            button_modify.pack(side="left", padx=10)

            button_delete = tk.Button(product_frame, text="Supprimer", bg="red", fg="white", padx=5, pady=5, bd=0, activebackground="light gray", command=lambda p=product: delete_product(p[0]))
            button_delete.pack(side="left", padx=10)

    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'))

home()
window.mainloop()
crud.cursor.close()
crud.connection.close()