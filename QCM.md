# Fiche de synthèse — Perceptron & MLP (QCM)

## 1) Perceptron simple (Rosenblatt)

### Ce que le perceptron peut (et ne peut pas) faire
- **Un perceptron simple ne résout que des problèmes de classification linéairement séparables.**
  - Exemple OK : AND, OR (avec un bon encodage).
  - Exemple impossible : **XOR**, car **non linéairement séparable**.

✅ Ta réponse : *linéairement séparables* — correcte.

### Fonction d’activation “classique”
- Historiquement, le perceptron utilise une **fonction seuil** :
  - **Heaviside** (step function) : renvoie 0/1 (ou -1/+1 selon convention).
- Remarque : en pratique moderne, on utilise souvent d’autres activations (sigmoïde, tanh, ReLU) selon les modèles, mais “classique” = **seuil**.

✅ Ta réponse : *Heaviside* — correcte.

### Opération avant l’activation
- Le perceptron calcule d’abord une **combinaison linéaire** :
  - \( z = w^\top x + b \)
- Puis applique l’activation :
  - \( \hat{y} = f(z) \)

⚠️ Correction : ta réponse *“produit matriciel multi-couches”* est imprécise.
- Le bon point essentiel : **produit scalaire / somme pondérée** (éventuellement écrit sous forme matricielle si plusieurs neurones, mais pas “multi-couches” pour un perceptron simple).

### Règle d’apprentissage (mise à jour des poids)
- Règle du perceptron (forme courante) :
  - \( \Delta w = \eta \, (y_{\text{true}} - y_{\text{pred}})\, x \)
  - \( w \leftarrow w + \Delta w \)

✅ Ta réponse : correcte.

### Théorème de convergence du perceptron
- Il garantit que l’algorithme **converge en un nombre fini d’itérations** **si** :
  - les données sont **linéairement séparables** (et \(\eta > 0\), données bornées, etc. selon les formulations).

✅ Ta réponse : correcte.

### Rôle du pas d’apprentissage \( \eta \)
- \( \eta \) contrôle **l’amplitude** de la mise à jour des poids :
  - trop grand : oscillations / instabilité possible,
  - trop petit : apprentissage lent.

✅ Ta réponse : correcte.

### Si la prédiction est correcte, que deviennent les poids ?
- Si \( y_{\text{true}} = y_{\text{pred}} \) alors :
  - \( (y_{\text{true}} - y_{\text{pred}})=0 \Rightarrow \Delta w = 0 \)
  - donc **les poids ne changent pas**.

✅ Ta réponse : correcte (et ton raisonnement est bon).

---

## 2) MLP (Multi-Layer Perceptron)

### Algorithme d’entraînement
- Un MLP est entraîné par :
  - **rétropropagation du gradient (backpropagation)** + une variante de descente de gradient (SGD, Adam, etc.)

✅ Ta réponse : correcte.

### Pourquoi des activations non linéaires ?
- Sans non-linéarité, même avec plusieurs couches, un réseau reste équivalent à **une seule transformation linéaire**.
- Les activations non-linéaires permettent d’apprendre des **frontières de décision non linéaires**.

✅ Ta réponse : correcte.

### Vanishing gradient (gradient évanescent)
- Les fonctions **sigmoïde** (et aussi tanh) sont très concernées :
  - saturation (sorties proches de 0 ou 1) → dérivée très petite → gradients qui “meurent”.

✅ Ta réponse : *sigmoïde* — correcte.

### Sens de propagation des gradients
- Pendant la rétropropagation, les gradients se propagent :
  - **de la sortie vers l’entrée** (couche de sortie → couches cachées → entrée).

✅ Ta réponse : correcte.

### Surapprentissage (overfitting)
- Définition :
  - très bonne perf sur l’entraînement,
  - mauvaise généralisation sur des données nouvelles (test/validation).

✅ Ta réponse : correcte.

### Régularisation par désactivation aléatoire
- **Dropout** : désactive aléatoirement des neurones (ou connexions) pendant l’entraînement.
- Effet : limite la co-adaptation, améliore la généralisation.

✅ Ta réponse : correcte.

---

## 3) Points à corriger dans tes réponses

### Sortie multi-classes : activation typique
❌ Ta réponse : **ReLU** (ce n’est pas l’usage typique pour des probabilités multi-classes)

✅ Correction :
- En classification **multi-classes (une seule classe vraie parmi K)** :
  - on utilise typiquement **Softmax** en sortie,
  - avec une perte du type **cross-entropy**.
- ReLU est surtout utilisée **dans les couches cachées**.

### Batch vs SGD
✅ Ta réponse est globalement correcte, mais voici la formulation “propre” à retenir :
- **Batch Gradient Descent** : gradient calculé sur **tout le dataset** à chaque mise à jour.
- **SGD** : gradient calculé sur **un seul exemple** (ou parfois “quasi-SGD”).
- **Mini-batch** (le plus courant en pratique) : gradient calculé sur un **petit lot** d’exemples.

---

## 4) Universelle approximation
- Théorème : un réseau avec **une seule couche cachée** (avec assez de neurones) peut **approximer toute fonction continue** sur un compact, sous conditions sur l’activation.

✅ Ta réponse : correcte.

---

## 5) ReLU : problème possible
- **Dying ReLU** : si un neurone tombe dans une zone où \(z<0\) tout le temps :
  - sortie = 0,
  - gradient = 0,
  - il peut rester “mort”.

✅ Ta réponse : correcte.

---

## Mémo express (à apprendre)
- Perceptron simple ⇒ **séparation linéaire** uniquement.
- XOR ⇒ **impossible** pour un perceptron simple.
- Perceptron : \(z=w^\top x+b\) puis **seuil (Heaviside)**.
- MLP ⇒ **non-linéarités** + **backprop**.
- Multi-classes sortie ⇒ **Softmax** (pas ReLU).
- Vanishing gradient ⇒ **sigmoïde/tanh** (saturation).
- Overfitting ⇒ bon train / mauvais test.
- Dropout ⇒ régularisation par “extinction” aléatoire.
- ReLU ⇒ efficace mais risque **dying ReLU**.