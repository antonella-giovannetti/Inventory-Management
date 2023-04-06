from classes.Connection import *
# "SELECT produit.nom, produit.description, produit.prix, produit.quantite, categorie.nom FROM produit INNER JOIN categorie ON categorie.id = produit.id_categorie"
class CRUD(Connection):
    def __init__(self):
        super().__init__()

    # Fonctions concernant les catégories 
    def readCategories(self):
        self.cursor.execute("SELECT nom FROM categorie")
        return self.cursor.fetchall()
    
    # Fonctions concernant les produits
    def readProductsByCategory(self, category):
        sql = "SELECT produit.id, produit.nom, produit.description, produit.prix, produit.quantite, categorie.nom FROM produit INNER JOIN categorie ON categorie.id = produit.id_categorie WHERE categorie.nom = %s"
        self.cursor.execute(sql, category)
        return self.cursor.fetchall()
    
    def createProduct(self, name, description, price, quantity, id_category):
        sql = "INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s);" 
        values = (name, description, price, quantity, id_category) 
        self.cursor.execute(sql, values) 
        self.connection.commit() 
        
    def updateProduct(self, name, description, price, quantity, id_category, id_product):
        self.cursor.execute("UPDATE produit SET nom = %s, description = %s, prix = %s, quantite = %s, id_categorie = %s WHERE id = %s;", (name, description, price, quantity, id_category,  id_product))
        self.connection.commit()

    def deleteProduct(self, id):
        self.cursor.execute(f"DELETE FROM produit WHERE id = {id};")
        self.connection.commit()

