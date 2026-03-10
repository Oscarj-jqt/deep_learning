# Perceptron & Multi-Layer Perceptron (MLP)

## 1. What is a Perceptron?
- A perceptron is a **single-layer linear classifier** (one neuron) used for **binary classification**.
- It decides a class by computing a **weighted sum** of inputs and applying a **threshold**.

## 2. Core Computation (Before Activation)
- The perceptron computes a linear score:
  - \( z = w^\top x + b \)
- Then it applies an activation function to produce the prediction:
  - \( \hat{y} = f(z) \)

