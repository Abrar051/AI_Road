import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

def gradient_descent(x,y):
    m_curr = b_curr = 0
    n = len(x)
    iteration = 10000
    learning_rate = 0.008
    for i in range(iteration):
        y_predicted = m_curr * x + b_curr
        md = -(2/n) * sum (x*(y-y_predicted))
        bd = -(2/n) * sum (y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print ('m {} , b {} iteration {}'.format(m_curr,b_curr,i))


def stochastic_gradient_descent(x,y):
    m_curr = b_curr = 0
    n = len(x)
    iteration = 10000
    learning_rate = 0.008
    for i in range(iteration):
        random_index = np.random.randint(n)
        x_index = x[random_index]
        y_index = y[random_index]
        md = -(2/n)* x_index * (y_index - (m_curr * x_index + b_curr))
        bd = -(2/n) * (y_index - (m_curr * x_index + b_curr))
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print('m {} , b {} iteration {}'.format(m_curr, b_curr, i))

#gradient_descent(x,y)
stochastic_gradient_descent(x,y)