# Binary Classification — Essential Notes

## 1. What is Binary Classification?
- Binary classification is a type of machine learning where the goal is to predict one of two possible outcomes (e.g., yes/no, 0/1, true/false).
- Examples: spam detection, disease diagnosis, etc.

## 2. Accuracy and Cross-Entropy
- **Accuracy:** Measures the proportion of correct predictions.
- **Cross-entropy loss:** Measures how well the predicted probabilities match the true labels. Lower cross-entropy means better predictions.

## 3. The Sigmoid Function
- The sigmoid activation function outputs values between 0 and 1, making it suitable for binary classification.
- Formula: $\sigma(x) = \frac{1}{1 + e^{-x}}$
- The output can be interpreted as the probability of the positive class.

## 4. Model Structure for Binary Classification
- Typical model:
    ```python
    model = keras.Sequential([
        layers.Dense(units=16, activation='relu', input_shape=[n_features]),
        layers.Dense(units=1, activation='sigmoid')
    ])
    ```
- The last layer uses a sigmoid activation to output a probability.

## 5. Compiling and Training the Model
- Use binary cross-entropy as the loss function and track accuracy:
    ```python
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['binary_accuracy'],
    )
    ```
    ## 5. Compiling and Training the Model
- Use binary cross-entropy as the loss function and track accuracy:
    ```python
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['binary_accuracy'],
    )
    ```

## 6. Evaluating the Model
- Plot training and validation loss and accuracy to monitor performance.
- The best model has low validation loss and high validation accuracy.

---

**Summary:**  
- Binary classification predicts one of two outcomes.
- Use sigmoid activation and binary cross-entropy loss.
- Monitor accuracy and loss to evaluate your model.