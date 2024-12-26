
# Importing necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn import datasets
import matplotlib.pyplot as plt

# Loading the Iris dataset
iris = datasets.load_iris()

# Plotting the first two features of the Iris dataset
_, ax = plt.subplots()
scatter = ax.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])

# Adding a legend to the scatter plot
_ = ax.legend(
    scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes"
)

# Features and labels
X = iris.data  # Features
y = iris.target  # Labels

# Splitting the dataset into training and testing sets (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creating a Naive Bayes classifier (GaussianNB for continuous data)
nb_classifier = GaussianNB()

# Training the model on the training data
nb_classifier.fit(X_train, y_train)

# Making predictions on the test data
y_pred = nb_classifier.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)

# Displaying results
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(classification_report(y_test, y_pred))
