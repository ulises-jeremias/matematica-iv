"""
The optimal values of m and b can be actually calculated with way less effort than doing a linear regression. 
this is just to demonstrate gradient descent
"""

from numpy import (array, genfromtxt)

def compute_error_for_line_given_points(b, m, points):
    """
    y = mx + b
    m is slope, b is y-intercept
    """

    totalError = 0
    
    for [x, y] in points:
        totalError += (y - (m * x + b)) ** 2

    return totalError / float(len(points))
        
def step_gradient(b, m, points, learning_rate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))

    for [x, y] in points:
        b_gradient += y - ((m * x) + b)
        m_gradient += x * (y - ((m * x) + b))

    new_b = b - (learning_rate * (-2/N) * b_gradient)
    new_m = m - (learning_rate * (-2/N) * m_gradient)

    return [new_b, new_m]

def gradient_descent(points, b, m, learning_rate, num_iterations):
    for _ in range(0, num_iterations):
        [b, m] = step_gradient(b, m, array(points), learning_rate)
    
    return [b, m]

def run():
    points = genfromtxt("data.csv", delimiter=",")
    print("Length of dataset:", len(points))

    learning_rate = 0.0001
    num_iterations = 1000
    initial_b = 0 # initial y-intercept guess
    initial_m = 0 # initial slope guess

    print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points)))
    print("Running...")

    [b, m] = gradient_descent(points, initial_b, initial_m, learning_rate, num_iterations)

    print("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points)))
    print("y = {0}x + {1}".format(b, m))

    """
    for y in map(lambda p: m * p[0] + b, points):
        print(y)
    """

if __name__ == '__main__':
    run()
