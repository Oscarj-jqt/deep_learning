# Dropout and Batch Normalization — Essential Notes

## 1. Dropout
- Dropout is a technique to prevent overfitting in neural networks.
- During training, dropout randomly "drops" (sets to zero) a fraction of the units in a layer for each batch.
- This forces the network to learn more robust features, not relying too much on any single neuron.
- Typical dropout rates are between 0.2 and 0.5.
- Example:
    ```python
    model = keras.Sequential([
        layers.Dense(16, activation='relu'),
        layers.Dropout(0.3),  # 30% dropout
        layers.Dense(10)
    ])
    ```

## 2. Batch Normalization
- Batch normalization ("batchnorm") normalizes the outputs of a layer to stabilize and speed up training.
- It helps the network train faster and can improve performance, especially on difficult datasets.
- Batch normalization can be added before or after the activation function.
- Example:
    ```python
    model = keras.Sequential([
        layers.Dense(16, activation='relu'),
        layers.BatchNormalization(),
        layers.Dense(10)
    ])
    ```

## 3. Using Both Together
- You can combine dropout and batch normalization in the same model.
- Example:
    ```python
    model = keras.Sequential([
        layers.Dense(128, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.3),
        layers.Dense(64, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.3),
        layers.Dense(1)
    ])
    ```

## 4. Tips
- After adding dropout, you may need to increase the number of units in your layers.
- Batch normalization can act like an adaptive standardization of your data inside the network.

---

**Summary:**  
- Dropout helps prevent overfitting by randomly disabling neurons during training.
- Batch normalization stabilizes and speeds up training by normalizing activations.
- Both are commonly used in modern deep learning models for better performance.