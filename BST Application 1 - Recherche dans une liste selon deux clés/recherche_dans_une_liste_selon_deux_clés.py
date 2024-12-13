class Etudiant:
    def __init__(self, matricule, nom, moyenne):
        self.matricule = matricule
        self.nom = nom
        self.moyenne = moyenne

    def __repr__(self):
        return f"Etudiant(matricule='{self.matricule}', nom='{self.nom}', moyenne={self.moyenne})"

class Node:
    def __init__(self, key, data):
        self.key = key  # Clé pour l'ABR (matricule ou moyenne)
        self.data = data  # Référence à l'objet étudiant
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        # Insère une clé et un étudiant dans l'ABR
        if not self.root:
            self.root = Node(key, data)
        else:
            self._insert_recursive(self.root, key, data)

    def _insert_recursive(self, current, key, data):
        if key < current.key:
            if current.left is None:
                current.left = Node(key, data)
            else:
                self._insert_recursive(current.left, key, data)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key, data)
            else:
                self._insert_recursive(current.right, key, data)

    def search(self, key):
        # Recherche une clé dans l'ABR
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current, key):
        if current is None:
            return None
        if key == current.key:
            return current.data
        elif key < current.key:
            return self._search_recursive(current.left, key)
        else:
            return self._search_recursive(current.right, key)

    def inorder_traversal(self):
        # Retourne une liste triée des clés avec leurs données
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current, result):
        if current:
            self._inorder_recursive(current.left, result)
            result.append(current.data)
            self._inorder_recursive(current.right, result)

    def print_tree_2d(self):
        # Affiche l'arbre en 2D avec des barres inclinées
        lines = []
        self._build_tree_2d(self.root, 0, False, '', lines)
        for line in lines:
            print(line)

    def _build_tree_2d(self, current, level, is_right, prefix, lines):
        if current is not None:
            # Construire la représentation de l'enfant droit
            self._build_tree_2d(current.right, level + 1, True, prefix + ('    ' if is_right else '│   '), lines)
            # Ajouter la ligne actuelle
            lines.append(prefix + ('┌── ' if is_right else '└── ') + str(current.key))
            # Construire la représentation de l'enfant gauche
            self._build_tree_2d(current.left, level + 1, False, prefix + ('    ' if not is_right else '│   '), lines)

class GestionEtudiants:
    def __init__(self):
        self.abr_matricule = BinarySearchTree()
        self.abr_moyenne = BinarySearchTree()

    def ajouter_etudiant(self, matricule, nom, moyenne):
        etudiant = Etudiant(matricule, nom, moyenne)
        self.abr_matricule.insert(matricule, etudiant)
        self.abr_moyenne.insert(moyenne, etudiant)

    def rechercher_par_matricule(self, matricule):
        return self.abr_matricule.search(matricule)

    def rechercher_par_moyenne(self, moyenne):
        return self.abr_moyenne.search(moyenne)

    def afficher_tous_les_etudiants(self):
        print("\nÉtudiants triés par matricule :")
        for etudiant in self.abr_matricule.inorder_traversal():
            print(etudiant)
        print("\nÉtudiants triés par moyenne :")
        for etudiant in self.abr_moyenne.inorder_traversal():
            print(etudiant)

    def afficher_arbres_2d(self):
        print("\nArbre des matricules (2D):")
        self.abr_matricule.print_tree_2d()
        print("\nArbre des moyennes (2D):")
        self.abr_moyenne.print_tree_2d()

# Exemple d'utilisation
gestion = GestionEtudiants()

# Ajout de 20 étudiants (désordonné)
gestion.ajouter_etudiant("E115", "Samir", 15.5)
gestion.ajouter_etudiant("E104", "Khalid", 12.0)
gestion.ajouter_etudiant("E120", "Loubna", 18.0)
gestion.ajouter_etudiant("E101", "Aziz", 10.5)
gestion.ajouter_etudiant("E118", "Redone", 16.7)
gestion.ajouter_etudiant("E106", "Oussama", 14.2)
gestion.ajouter_etudiant("E113", "Youssef", 19.5)
gestion.ajouter_etudiant("E108", "Abir", 11.0)
gestion.ajouter_etudiant("E117", "Khadija", 13.5)
gestion.ajouter_etudiant("E102", "Rim", 17.8)
gestion.ajouter_etudiant("E110", "Salim", 12.3)
gestion.ajouter_etudiant("E112", "ahmed", 15.0)
gestion.ajouter_etudiant("E105", "Zadi", 18.5)
gestion.ajouter_etudiant("E114", "Karim", 14.0)
gestion.ajouter_etudiant("E109", "Rabiaa", 16.0)
gestion.ajouter_etudiant("E103", "Sanawsar", 10.0)
gestion.ajouter_etudiant("E119", "soundouss", 13.0)
gestion.ajouter_etudiant("E107", "Soulaimane", 19.0)
gestion.ajouter_etudiant("E111", "Radi", 11.5)
gestion.ajouter_etudiant("E116", "Ibrahim", 17.0)

# Recherche
print("\nRecherche par matricule 'E105':")
print(gestion.rechercher_par_matricule("E105"))

print("\nRecherche par moyenne 19.5:")
print(gestion.rechercher_par_moyenne(19.5))

# Affichage de tous les étudiants
print("\nListe de tous les étudiants :")
gestion.afficher_tous_les_etudiants()

# Affichage des arbres en 2D
gestion.afficher_arbres_2d()
