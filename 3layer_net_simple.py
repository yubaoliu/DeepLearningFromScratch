import numpy as np
from sigmoid import sigmoid

def identify_function(x):
    return x

# Input
print('Input data:')
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

W2 = np.array([ [0.1, 0.4], [0.2, 0.5], [0.3,0.6] ])
B2 = np.array([0.1, 0.2])

W3 = np.array([[0.1, 0.3], [0.2, 0.4] ])
B3 = np.array([0.1, 0.2])

print('X')
print(X)

# first layer
print('First layer:')
A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)

print('A1:')
print(A1)
print('Z1:')
print(Z1)

# Second layer
print('Second layer:')
A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

print('A2:')
print(A2)

print('Z2')
print(Z2)

# Output layer
A3 = np.dot(Z2, W3) + B3
Y = identify_function(A3)

print('A3:')
print(A3)
print('Y:')
print(Y)

