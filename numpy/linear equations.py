import numpy as np

# Créer une matrice symétrique définie positive aléatoire A (10x10)
np.random.seed(42)  # Pour la reproductibilité
A = np.random.rand(100, 100) # Générer une matrice A de dimension 10 × 10 avec des valeurs aléatoires comprises entre 0 et 1

A = np.dot(A, A.T)  # Rendre la matrice symétrique et définie positive, ce qui est une condition pour utiliser la décomposition de Cholesky
# Créer un vecteur aléatoire b (10 éléments)
b = np.random.rand(100)
# Résolution en utilisant numpy.linalg.solve
x_solve = np.linalg.solve(A, b)

# Résolution en utilisant la décomposition de Cholesky
L = np.linalg.cholesky(A)
y = np.linalg.solve(L, b)       # Substitution avant
x_cholesky = np.linalg.solve(L.T, y)  # Substitution arrière

# Calculer l'erreur quadratique pour chaque méthode
error_solve = np.linalg.norm(np.dot(A, x_solve) - b)**2
error_cholesky = np.linalg.norm(np.dot(A, x_cholesky) - b)**2

print(f"Erreur quadratique pour solve: {error_solve}")
print(f"Erreur quadratique pour cholesky: {error_cholesky}")