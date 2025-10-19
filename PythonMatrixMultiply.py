import numpy as np


def theta_transpose_x(theta, x):
    """
    Compute the dot product of theta^T and x

    Parameters:
    -----------
    theta : array-like
        Parameter vector of shape (n,) or (n, 1)
    x : array-like
        Feature vector of shape (n,) or (n, 1)

    Returns:
    --------
    float or array
        The dot product result theta^T * x
    """
    theta = np.array(theta).flatten()
    x = np.array(x).flatten()

    # Compute dot product
    result = np.dot(theta, x)

    return result


# Example 1: Basic Usage
theta = [1, 2, 3, 4]
x = [5, 6, 7, 8]
result = theta_transpose_x(theta, x)
print(f"theta^T * x = {result}")  # Output: 70

# Example 2: Linear Regression Hypothesis
# h(x) = theta_0 + theta_1 * x
theta = [0.3, 1.4]  # [intercept, slope]
x = [1, 2.5]  # [bias term (always 1), actual x value]
prediction = theta_transpose_x(theta, x)
print(f"Prediction h(x) = {prediction}")  # Output: 3.8

# Example 3: Multiple samples (vectorized)
theta = np.array([0.3, 1.4])
X = np.array([
    [1, 2.0],
    [1, 3.0],
    [1, 4.0],
    [1, 6.0]
])
predictions = X @ theta  # Matrix multiplication
print(f"Predictions = {predictions}")
