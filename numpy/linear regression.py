import numpy as np
import matplotlib.pyplot as plt

# Données d'exemple
x = np.linspace(0, 10, 100) # Valeurs de x
# Générer les valeurs de y en utilisant une relation linéaire avec du bruit aléatoire
true_slope = 2.5  # Pente réelle
true_intercept = 1.0  # Intercept réel
noise = np.random.normal(0, 1, size=x.shape)  # Bruit aléatoire

# Valeurs observées de y
y = true_slope * x + true_intercept + noise
# Ajustement linéaire avec numpy.polyfit
coefficients = np.polyfit(x, y, 1)  # Degré 1 pour une régression linéaire
a, b = coefficients  # a = pente, b = ordonnée à l'origine

# Générer les valeurs prédites
y_pred = a * x + b

# Affichage des résultats
print(f"Pente (a) : {a}")
print(f"Ordonnée à l'origine (b) : {b}")

# Tracé des points et de la droite d'ajustement
plt.scatter(x, y, color="blue", label="Données observées")  # Points
plt.plot(x, y_pred, color="red", label="Droite d'ajustement")  # Droite
plt.xlabel("x")
plt.ylabel("y")
plt.title("Régression linéaire avec numpy.polyfit")
plt.legend()
plt.grid()
plt.show()
