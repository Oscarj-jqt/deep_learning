# Stochastic Gradient Descent — Essential Notes

## 1. What is SGD?
- Stochastic Gradient Descent (SGD) is an algorithm used to optimize (train) neural networks.
- It updates the model’s weights step by step to minimize the loss function.

## 2. The Loss Function
- The loss function measures how well the model’s predictions match the true values.
- The goal of training is to find weights that minimize this loss.

## 3. How SGD Works
- Instead of using all data at once, SGD updates weights using small random batches (mini-batches).
- Steps:
  1. Pick a random batch of data.
  2. Calculate the loss and its gradient (direction to improve).
  3. Update the weights a little in the direction that reduces the loss.
  4. Repeat for many batches/epochs.

## 4. Learning Rate and Batch Size
- **Learning rate:** Controls how big each update step is. Too high = unstable, too low = slow.
- **Batch size:** Number of samples per update. Small batch = more updates, more noise; large batch = smoother updates.

## 5. Adding Loss and Optimizer in Keras
- Example:
    ```python
    model.compile(
        loss='mae',                # Mean Absolute Error loss
        optimizer='sgd'            # Stochastic Gradient Descent optimizer
    )
    ```

## 6. Training
- Use `model.fit()` to train the model for several epochs (full passes over the data).
- The loss should decrease over time if training is working.

---

## 7. Complete Example: Building and Training a Deep Neural Network with SGD

```python
from tensorflow import keras
from tensorflow.keras import layers

# Define the model architecture
model = keras.Sequential([
    layers.Dense(512, activation='relu', input_shape=[11]),  # First hidden layer: 512 units, ReLU activation
    layers.Dense(512, activation='relu'),                    # Second hidden layer: 512 units, ReLU activation
    layers.Dense(512, activation='relu'),                    # Third hidden layer: 512 units, ReLU activation
    layers.Dense(1),                                         # Output layer: 1 unit (for regression)
])

# Compile the model with SGD optimizer and MAE loss
model.compile(
    optimizer='sgd',     # Stochastic Gradient Descent optimizer
    loss='mae'           # Mean Absolute Error loss
)

# Train the model
history = model.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),  # Use validation data to monitor performance
    batch_size=256,                      # Number of samples per batch
    epochs=10                            # Number of times to go through the dataset
)
```

**Notes:**
- Start with a simple architecture and adjust based on validation loss.
- The batch size and number of epochs are important hyperparameters.
- Use validation data to check if your model is overfitting or underfitting.

---

This example shows the full process: defining the model, compiling it with the optimizer and loss, and training it on your data.

**Summary:**  
SGD is a method to train neural networks by updating weights in small steps using random batches of data, aiming to minimize the loss function. The learning rate and batch size are key parameters for effective training.