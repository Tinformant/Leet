# Gaussian Naive Bayes Skeleton Code: 

import numpy as np
import math 
from sklearn.metrics import hamming_loss

from scipy.stats import norm

def G_N_B(x, mean, var):
    temp = ((x - mean)** 2) / var
    return (1 / math.sqrt(2 * math.pi * var)) * math.exp(-1/2 * temp)

data = np.genfromtxt('wbdc.txt', delimiter=',')

size = [50, 100, 150, 200, 250, 300, 350, 400, 450]
for sz in size:
    train, test = data[1:sz+1, :], data[sz+1:, :]
    X_trn, y_trn = train[:, 2:], train[:,1]
    X_tst, y_tst = test[:, 2:], test[:,1]
    
    # Compute the label probabilities
    num_benign = 0
    for y in y_trn:
        if y == 1:
            num_benign += 1
            
    prob_benign = num_benign / len(y_trn)
    num_mal = len(y_trn) - num_benign
    prob_malignant = num_mal / len(y_trn)
    
    # Compute the class conditional means, and variance for Gaussian Naive Bayes
    # You 'may' obtain four arrays/lists of size 30, two for means for each label, 
    # and two for variances for each label. 
    
    b_mean = []
    m_mean = []
    b_var = []
    m_var = []
    
    # x should represent the array for each patient
    for i in range(0, 30):
        for j in range(0, len(y_trn)):
            # If it is benign == 1
            print(i)
            print(j)
            if (y_trn[j] == 1):
                print(b_mean[0])
                b_mean[i] += X_trn[j][i]
            else:
                print(m_mean[0])
                m_mean[i] += X_trn[j][i]
            
    for i in b_mean:
        i = i / num_benign
    for i in m_mean:
        i = i / num_mal
    
    for i in range(0, 30):
        for j in range(0, len(y_trn)):
            if y_trn[i] == 1:
                b_var += (X_trn[j][i] - b_mean) ** 2
            else:
                m_var += (X_trn[j][i] - m_mean) ** 2
                
    for i in b_var:
        i = i / num_benign
    for i in m_var:
        i = i / num_mal
    
# Training error
#     for i in range(0, len(y_trn)):
#         out = 1
#         for 
#         prob_mal * 
    
    
    
        
    # Compute the training error, and test error of the GNB model you learnt.
    # You may want to use logarithms for computations
    
# In a single plot, show the values of training and test 
    
