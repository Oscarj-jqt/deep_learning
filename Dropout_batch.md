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

## Real Example: Training a Model with Dropout and Batch Normalization

Below is a typical workflow for training a deep learning model using dropout and batch normalization. This example shows how to compile the model, fit it to the data, and visualize the training and validation loss.

```python
model.compile(
    optimizer='sgd',
    loss='mae',
    metrics=['mae'],
)

EPOCHS = 100
history = model.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),
    batch_size=64,
    epochs=EPOCHS,
    verbose=0,
)

# Visualize the learning curves
history_df = pd.DataFrame(history.history)
history_df.loc[0:, ['loss', 'val_loss']].plot()
print(("Minimum Validation Loss: {:0.4f}").format(history_df['val_loss'].min()))
```

**Explanation:**
- The model is compiled with SGD optimizer and MAE loss.
- Training runs for 100 epochs with a batch size of 64.
- Both training and validation loss are tracked and plotted to monitor overfitting or underfitting.
- The minimum validation loss is printed to help select the best model.

This process helps you evaluate how well dropout and batch normalization are working in practice.
---

**Summary:**  
- Dropout helps prevent overfitting by randomly disabling neurons during training.
- Batch normalization stabilizes and speeds up training by normalizing activations.
- Both are commonly used in modern deep learning models for better performance.