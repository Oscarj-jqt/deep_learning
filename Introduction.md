# Deep Learning

Deep learning is an approach where neural networks make deep stacks of computations to solve complex and hierarchical patterns.

It is used for tasks like natural language translation, image recognition, and game playing, often achieving human-level or better performance.

Each neuron in a neural network performs a simple computation, but the power of deep learning comes from the complexity and depth of the connections between these neurons.

---

## The Linear Unit

A neuron can be represented by a simple mathematical formula:

$$
y = wx + b
$$

- **x** is the input (data we collected).
- **w** is the weight of the connection to the neuron.
- **b** is the bias, a constant that allows the neuron to adjust its output independently of the input.
- **y** is the output (the value produced by the neuron).

A neural network learns by adjusting its weights (**w**) and bias (**b**) to better fit the data.

---

## Using TensorFlow Keras to Create a Model

We use the TensorFlow Keras library to create a model with `keras.Sequential`:

```python
from tensorflow import keras
from tensorflow.keras import layers

# Create a network with 1 linear unit
model = keras.Sequential([
    layers.Dense(units=1, input_shape=[3])
])
```

- **units** define how many outputs we want.
- **input_shape** is the number of columns x features without the target chosen to train the model.