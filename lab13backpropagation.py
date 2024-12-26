#lab13: Back propagation
import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# NeuralNetwork class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases
        self.weights_input_hidden = np.random.rand(input_size, hidden_size) - 0.5
        self.weights_hidden_output = np.random.rand(hidden_size, output_size) - 0.5
        self.learning_rate = 0.5

    def forward(self, x):
        # Forward propagation
        self.input = x
        self.hidden = sigmoid(np.dot(self.input, self.weights_input_hidden))
        self.output = sigmoid(np.dot(self.hidden, self.weights_hidden_output))
        return self.output

    def backward(self, x, y, output):
        # Backpropagation
        output_error = y - output
        output_delta = output_error * sigmoid_derivative(output)

        hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden)

        # Update weights
        self.weights_hidden_output += np.dot(self.hidden.T, output_delta) * self.learning_rate
        self.weights_input_hidden += np.dot(x.T, hidden_delta) * self.learning_rate

    def train(self, x, y, iterations):
        for i in range(iterations):
            output = self.forward(x)
            self.backward(x, y, output)
            if i % 1000 == 0:
                loss = np.mean(np.square(y - output))
                print(f"Iteration {i}, Loss: {loss}")

# Example usage
if __name__ == "__main__":
    # XOR dataset
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    # Initialize and train the network
    nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)
    nn.train(x, y, iterations=10000)

    # Test the network
    print("\nAfter training:")
    print(nn.forward(x))


