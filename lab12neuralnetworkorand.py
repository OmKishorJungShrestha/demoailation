import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Neural network class
class NeuralNetwork:
    def __init__(self):
        # Initialize weights and bias randomly
        self.weights = np.random.rand(2, 1)  # Two inputs (AND/OR gate)
        self.bias = np.random.rand(1)
        self.learning_rate = 0.1

    # Train the network with inputs and expected output
    def train(self, inputs, expected_output, epochs):
        for epoch in range(epochs):
            total_error = 0
            for x, y in zip(inputs, expected_output):
                # Feed forward
                weighted_sum = np.dot(x, self.weights) + self.bias
                activated_output = sigmoid(weighted_sum)

                # Calculate the error
                error = y - activated_output
                total_error += error ** 2  # Sum of squared errors for monitoring

                # Backpropagation
                adjustments = error * sigmoid_derivative(activated_output)

                # Update weights and bias
                self.weights += self.learning_rate * np.dot(x.reshape(-1, 1), adjustments.reshape(1, -1))
                self.bias += self.learning_rate * adjustments

            if epoch % 1000 == 0:  # Print error every 1000 epochs
                print(f"Epoch {epoch}/{epochs}, Total Error: {total_error}")

    # Predict the output for a given input
    def predict(self, input_data):
        weighted_sum = np.dot(input_data, self.weights) + self.bias
        activated_output = sigmoid(weighted_sum)
        return np.round(activated_output)  # Return 0 or 1 (binary output)


# Define input and output for AND gate
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
and_outputs = np.array([[0], [0], [0], [1]])

# Define input and output for OR gate
or_outputs = np.array([[0], [1], [1], [1]])

# Initialize the neural network
and_gate_nn = NeuralNetwork()
or_gate_nn = NeuralNetwork()

# Train the network for AND gate
print("Training Neural Network for AND gate...")
and_gate_nn.train(inputs, and_outputs, 10000)

# Train the network for OR gate
print("Training Neural Network for OR gate...")
or_gate_nn.train(inputs, or_outputs, 10000)

# Testing AND gate
print("\nAND Gate Results:")
for input_data in inputs:
    print(f"Input: {input_data} Output: {and_gate_nn.predict(input_data)}")

# Testing OR gate
print("\nOR Gate Results:")
for input_data in inputs:
    print(f"Input: {input_data} Output: {or_gate_nn.predict(input_data)}")
