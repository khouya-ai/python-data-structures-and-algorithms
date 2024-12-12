
from collections import deque

class Node:
    """
    Classe représentant un nœud dans un arbre binaire de recherche.
    Attributs :
        data : Valeur stockée dans le nœud.
        left : Référence au nœud enfant gauche.
        right : Référence au nœud enfant droit.
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node({self.data})"

    def __eq__(self, other):
        return isinstance(other, Node) and self.data == other.data

    def __lt__(self, other):
        return isinstance(other, Node) and self.data < other.data


class BinarySearchTree:
    """
    Classe représentant un arbre binaire de recherche.
    Attributs :
        root : Le nœud racine de l'arbre.
    """

    def __init__(self, data):
        if isinstance(data, (int, float, str)):
            self.root = Node(data)
        elif isinstance(data, list):
            self.root = self.from_list(data)
        elif isinstance(data, set):
            self.root = self.from_set(sorted(data))  # Convertir l'ensemble en liste triée
        elif isinstance(data, dict):
            self.root = self.from_set(data.values())  # Utiliser les valeurs du dictionnaire
        else:
            self.root = None

    def is_empty(self):
        """
        Vérifier si l'arbre binaire de recherche est vide.
        Retourne True si l'arbre est vide, False sinon.
        """
        return self.root is None

    def get_root_value(self):
        """
        Lire la valeur stockée dans la racine de l'arbre.
        Retourne la valeur si la racine existe, sinon None.
        """
        return self.root.data if self.root else None

    def set_root_value(self, value):
        """
        Modifier la valeur stockée dans la racine de l'arbre.
        Si la racine n'existe pas, elle est créée avec la valeur donnée.
        """
        if self.root:
            self.root.data = value
        else:
            self.root = Node(value)

    def get_left_subtree(self):
        """
        Lire le sous-arbre gauche de la racine.
        Retourne le sous-arbre gauche si présent, sinon None.
        """
        return self.root.left if self.root else None

    def get_right_subtree(self):
        """
        Lire le sous-arbre droit de la racine.
        Retourne le sous-arbre droit si présent, sinon None.
        """
        return self.root.right if self.root else None

    def _insert(self, root, data):
        """
        Méthode auxiliaire pour insérer récursivement un nouveau nœud dans l'arbre binaire de recherche.
        """
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
        return root

    def insert(self, data):
        """
        Méthode publique pour insérer un nouveau nœud dans l'arbre binaire de recherche.
        """
        self.root = self._insert(self.root, data)

    def find_minimum(self):
        """
        Trouver le nœud avec la valeur minimale dans l'arbre binaire de recherche.
        Retourne la valeur minimale si l'arbre n'est pas vide, sinon None.
        """
        if self.is_empty():
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.data

    def calculate_size(self):
        """
        Calculer la taille de l'arbre binaire de recherche (nombre total de nœuds).
        Retourne un entier représentant la taille de l'arbre.
        """

        def _size(node):
            if not node:
                return 0
            return 1 + _size(node.left) + _size(node.right)

        return _size(self.root)

    def find(self, data):
        """
        Rechercher un nœud avec une valeur spécifique dans l'arbre binaire de recherche.
        Retourne True si la valeur est trouvée, sinon False.
        """

        def _find(node, data):
            if node is None:
                return False
            if node.data == data:
                return True
            elif data < node.data:
                return _find(node.left, data)
            else:
                return _find(node.right, data)

        return _find(self.root, data)

    def _clear_recursive(self, node):
        """
        Méthode auxiliaire pour supprimer récursivement tous les nœuds de l'arbre.
        """
        if node:
            # Supprimer récursivement les sous-arbres gauche et droit
            self._clear_recursive(node.left)
            self._clear_recursive(node.right)
            # Supprimer le nœud actuel
            node.left = None
            node.right = None

    def clear(self):
        """
        Supprimer tous les nœuds de l'arbre en appelant la méthode auxiliaire récursive.
        """
        self._clear_recursive(self.root)
        self.root = None

    def _count_leaves(self, node):
        """
        Méthode auxiliaire pour compter le nombre de feuilles dans l'arbre de manière récursive.
        """
        if node is None:
            return 0
        # Si le nœud est une feuille (aucun enfant gauche ni droit)
        if node.left is None and node.right is None:
            return 1
        # Sinon, compter les feuilles dans les sous-arbres gauche et droit
        return self._count_leaves(node.left) + self._count_leaves(node.right)

    def count_leaves(self):
        """
        Calculer le nombre de feuilles dans l'arbre.
        Retourne le nombre de feuilles.
        """
        return self._count_leaves(self.root)

    def _in_order_traversal(self, node, result):
        """Méthode auxiliaire pour effectuer un parcours en ordre (infixe)."""
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.data)
            self._in_order_traversal(node.right, result)

    def in_order(self):
        """Retourner les éléments de l'arbre selon le parcours en ordre."""
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _post_order_traversal(self, node, result):
        """Méthode auxiliaire pour effectuer un parcours post-ordre (postfixe)."""
        if node:
            self._post_order_traversal(node.left, result)
            self._post_order_traversal(node.right, result)
            result.append(node.data)

    def post_order(self):
        """Retourner les éléments de l'arbre selon le parcours post-ordre."""
        result = []
        self._post_order_traversal(self.root, result)
        return result

    def _pre_order_traversal(self, node, result):
        """Méthode auxiliaire pour effectuer un parcours pré-ordre (préfixe)."""
        if node:
            result.append(node.data)
            self._pre_order_traversal(node.left, result)
            self._pre_order_traversal(node.right, result)

    def pre_order(self):
        """Retourner les éléments de l'arbre selon le parcours pré-ordre."""
        result = []
        self._pre_order_traversal(self.root, result)
        return result

    def level_order(self):
        """Retourner les éléments de l'arbre selon le parcours en largeur (breadth-first)."""
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            result.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def is_degenerate(self):
        """
        Vérifier si l'arbre binaire de recherche est dégénéré.
        Un arbre est dégénéré s'il ressemble à une liste liée,
        c'est-à-dire qu'il n'a qu'un seul enfant pour chaque nœud.
        Retourne True si l'arbre est dégénéré, sinon False.
        """

        def _is_degenerate(node):
            if node is None:
                return True  # Si le nœud est vide, il est dégénéré par définition
            if node.left and node.right:  # Si le nœud a deux enfants
                return False
            # Si un seul enfant est présent, vérifier les sous-arbres
            return _is_degenerate(node.left) and _is_degenerate(node.right)

        return _is_degenerate(self.root)

    def __str__(self):
        """
        Représentation sous forme de chaîne de l'arbre binaire de recherche en tant que liste triée.
        """
        return str(self.in_order())

    @classmethod
    def from_list(cls, data):
        """
        Construire un arbre binaire de recherche à partir d'une liste d'éléments.
        """
        if not data:
            return None
        tree = cls(data[0])  # Initialiser l'arbre avec le premier élément
        for item in data[1:]:
            tree.insert(item)
        return tree.root

    @classmethod
    def from_dict(cls, data):
        """
        Construire un arbre binaire de recherche à partir d'un dictionnaire (en utilisant ses valeurs).
        """
        return cls.from_list(list(data.values()))

    @classmethod
    def from_set(cls, data):
        """
        Construire un arbre binaire de recherche à partir d'un ensemble (trié avant insertion).
        """
        return cls.from_list(sorted(data))


# Exemple d'utilisation
if __name__ == "__main__":
    # Initialiser l'arbre avec une seule valeur
    bst = BinarySearchTree(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(2)
    bst.insert(7)

    # Vérifier si l'arbre est vide
    print("L'arbre est vide :", bst.is_empty())

    # Lire et modifier la valeur en racine
    print("Valeur en racine :", bst.get_root_value())
    bst.set_root_value(20)
    print("Nouvelle valeur en racine :", bst.get_root_value())

    # Lire les sous-arbres gauche et droit
    print("Sous-arbre gauche :", bst.get_left_subtree())
    print("Sous-arbre droit :", bst.get_right_subtree())

    # Afficher l'arbre sous forme de liste triée
    print("Arbre binaire de recherche sous forme de liste :", bst)

    # Trouver le nœud minimum
    print("Valeur minimale dans l'arbre :", bst.find_minimum())

    # Calculer la taille de l'arbre
    print("Taille de l'arbre :", bst.calculate_size())

    # Rechercher une valeur dans l'arbre
    print("La valeur 7 est dans l'arbre :", bst.find(7))
    print("La valeur 100 est dans l'arbre :", bst.find(100))

    # Créer un arbre à partir d'une liste
    bst_from_list = BinarySearchTree([20, 10, 30, 25, 5])
    print("Arbre binaire de recherche à partir d'une liste :", bst_from_list)

    # Créer un arbre à partir d'un dictionnaire
    bst_from_dict = BinarySearchTree.from_dict({"a": 3, "b": 1, "c": 2})

    # Afficher l'arbre avant de le vider
    print("Arbre avant vidage :", bst)

    # Calculer et afficher le nombre de feuilles
    print("Nombre de feuilles dans l'arbre :", bst.count_leaves())

    # Afficher les parcours de l'arbre
    print("Parcours en ordre (infixe) :", bst.in_order())
    print("Parcours post-ordre (postfixe) :", bst.post_order())
    print("Parcours pré-ordre (préfixe) :", bst.pre_order())
    print("Parcours en largeur (breadth-first) :", bst.level_order())

    # Vider l'arbre
    bst.clear()

    # Vérifier si l'arbre est vide après l'avoir vidé
    print("L'arbre est vide après vidage :", bst.is_empty())
    print("Arbre après vidage :", bst)

    # Arbre dégénéré
    bst_degenerate = BinarySearchTree(10)
    bst_degenerate.insert(20)
    bst_degenerate.insert(150)
    bst_degenerate.insert(200)  # La structure devient dégénérée

    # Arbre non dégénéré
    bst_non_degenerate = BinarySearchTree(10)
    bst_non_degenerate.insert(5)
    bst_non_degenerate.insert(15)

    # Vérification si les arbres sont dégénérés
    print("L'arbre dégénéré est-il dégénéré ? :", bst_degenerate.is_degenerate())  # True
    print("L'arbre non dégénéré est-il dégénéré ? :", bst_non_degenerate.is_degenerate())  # False