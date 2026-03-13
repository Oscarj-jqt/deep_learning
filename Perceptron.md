# Perceptron & Multi-Layer Perceptron (MLP)

## 1. What is a Perceptron?
- A perceptron is a **single-layer linear classifier** (one neuron) used for **binary classification**.
- It decides a class by computing a **weighted sum** of inputs and applying a **threshold**.

## 2. Core Computation (Before Activation)
- The perceptron computes a linear score:
  - \( z = w^\top x + b \)
- Then it applies an activation function to produce the prediction:
  - \( \hat{y} = f(z) \)

## 3. Classic Activation Function (Rosenblatt)
- The classic perceptron uses a **step / threshold function**:
  - **Heaviside** (outputs 0/1, or -1/+1 depending on convention)

## 4. What Problems Can a Perceptron Solve?
- A perceptron converges (and can perfectly classify) **only if the data is linearly separable**.
- It **cannot** solve non-linearly separable problems such as:
  - **XOR**, because XOR is **not linearly separable**.

## 5. Perceptron Learning Rule
- Weight update rule:
  - \( \Delta w = \eta \,(y_{\text{true}} - y_{\text{pred}})\,x \)
  - \( w \leftarrow w + \Delta w \)
- If the prediction is correct (\(y_{\text{true}} = y_{\text{pred}}\)):
  - \( \Delta w = 0 \) → **weights are not changed**
- Learning rate \( \eta \):
  - controls the **magnitude of weight corrections**
  - too large can destabilize training; too small slows learning

