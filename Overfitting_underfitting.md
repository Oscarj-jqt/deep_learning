# Overfitting and Underfitting — Essential Notes

## 1. What are Overfitting and Underfitting?
- **Underfitting:** The model is too simple and cannot capture the patterns in the data. Both training and validation loss are high.
- **Overfitting:** The model is too complex and memorizes the training data, but performs poorly on new (validation) data. Training loss is low, but validation loss increases.

## 2. Learning Curves
- Plotting training and validation loss over epochs helps spot underfitting and overfitting.
- Underfitting: Both losses stay high.
- Overfitting: Training loss drops, validation loss rises after a point.

## 3. Capacity
- Model capacity is how complex the model is (number of layers/units).
- Too little capacity = underfitting. Too much = overfitting.
- Adjust capacity to match the complexity of your data.

## 4. Early Stopping
- Early stopping is a technique to prevent overfitting.
- Stop training when validation loss stops improving.
- Use Keras callbacks to implement early stopping:
    ```python
    from tensorflow.keras.callbacks import EarlyStopping

    early_stopping = EarlyStopping(
        patience=5,              # Number of epochs to wait for improvement
        min_delta=0.001,         # Minimum change to qualify as improvement
        restore_best_weights=True
    )
    ```

## 5. Example: Training with Early Stopping
    ```python
    history = model.fit(
        X_train, y_train,
        validation_data=(X_valid, y_valid),
        callbacks=[early_stopping]
    )
    ```

---


## Real Example: Interpreting Learning Curves (Quick Notes)

- **Small gap, both losses flat:** Likely underfitting. Model too simple, can't learn patterns.Try a bigger model.
- **Validation loss rises, training loss drops:** Overfitting. Model too complex, memorizes training data, poor generalization.Try a smaller model or use early stopping.
- **Early stopping:** Stops training at the best validation loss, helps avoid overfitting. Use learning curves, adjust model capacity, and apply early stopping to find the right balance.
