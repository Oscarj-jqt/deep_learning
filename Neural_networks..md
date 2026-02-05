# Deep Neural Networks — Essential Notes

## 1. What is a Deep Neural Network?
- A deep neural network (DNN) is a neural network with multiple layers.
- Adding more layers helps the network learn complex relationships in data.

## 2. Layers
- Each layer transforms its input into a new representation.
- Stacking layers allows the network to build more complex features step by step.

## 3. Activation Functions
- Activation functions add non-linearity, allowing the network to learn complex patterns.
- The most common is ReLU (Rectified Linear Unit): f(x) = max(0, x)

## 4. Building a Model
- Layers are connected in sequence: input → hidden layers (with activation) → output.
- Example (using Keras):
    ```python
    from tensorflow import keras
    from tensorflow.keras import layers

    This model has 2 hidden layers, each with 4 units (neurons). Each unit processes the input and applies the ReLU activation, which helps the network learn non-linear patterns. The last layer has 1 unit (neuron) with no activation, producing the final output (often used for regression tasks).

    model = keras.Sequential([
        layers.Dense(units=4, activation='relu', input_shape=[2]),  
        layers.Dense(units=4, activation='relu'),                   
        layers.Dense(units=1)                              
    ])
    ```

---

**Summary:**  
A deep neural network is made by stacking several layers, each with an activation function (like ReLU), to learn complex data patterns. The model is usually built sequentially, layer by layer.