# -*- coding: utf-8 -*-
"""cross_entropy_demo1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DNX_VUsj-fbcML4g-nUHbVwUuI78RLB5
"""

import torch as T
import numpy as np
import torch.nn.functional as F
import matplotlib.pyplot as plt

P  = [1.0,   0.0,   0.0,   0.0  ]

Q1 = [0.99,  0.,    0.,    0.01 ]
Q2 = [0.5,   0.25,  0.125, 0.125]
Q3 = [0.25,  0.25,  0.25,  0.25 ]
Q4 = [0.125, 0.125, 0.25,  0.5  ]

ce1 = -P[0]*np.log2(Q1[0])#-P[1]*np.log2(Q1[1])-P[2]*np.log2(Q1[2])-P[3]*np.log2(Q1[3])
ce2 = -P[0]*np.log2(Q2[0])-P[1]*np.log2(Q2[1])-P[2]*np.log2(Q2[2])-P[3]*np.log2(Q2[3])
ce3 = -P[0]*np.log2(Q3[0])-P[1]*np.log2(Q3[1])-P[2]*np.log2(Q3[2])-P[3]*np.log2(Q3[3])
ce4 = -P[0]*np.log2(Q4[0])-P[1]*np.log2(Q4[1])-P[2]*np.log2(Q4[2])-P[3]*np.log2(Q4[3])
print(f'ce1 = {ce1}\nce2 = {ce2}\nce3 = {ce3}\nce4 = {ce4}')

def cross_entropy(P, Q, base=None):
    Q = np.clip(Q, 1e-12, 1-1e-12)  # clip Q to prevent division by zero
    if base == 2:
        return -np.sum(P * np.log2(Q))
    elif base == 10:
        return -np.sum(P * np.log10(Q))
    return -np.sum(P * np.log(Q))

ce1 = cross_entropy(P, Q1)
ce2 = cross_entropy(P, Q2)
ce3 = cross_entropy(P, Q3)
ce4 = cross_entropy(P, Q4)
print(f'ce1 = {ce1}\nce2 = {ce2}\nce3 = {ce3}\nce4 = {ce4}')

F_ce1 = F.cross_entropy(T.tensor(Q1), T.tensor(P))
F_ce2 = F.cross_entropy(T.tensor(Q2), T.tensor(P))
F_ce3 = F.cross_entropy(T.tensor(Q3), T.tensor(P))
F_ce4 = F.cross_entropy(T.tensor(Q4), T.tensor(P))
print(f'ce1 = {F_ce1}\nce2 = {F_ce2}\nce3 = {F_ce3}\nce4 = {F_ce4}')

def softmax_stable(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0) # e_x / np.sum(e_x)

L1 = [3.9, 0.01, 0.01, 0.2]
L2 = [2.4, 0.5,  0.25, 0.2]
L3 = [1.5, 0.5,  0.5,  0.5]
L4 = [0.2, 0.25, 0.5,  3.0]

Q1 = softmax_stable(L1)
Q2 = softmax_stable(L2)
Q3 = softmax_stable(L3)
Q4 = softmax_stable(L4)

ce1 = cross_entropy(P, Q1)
ce2 = cross_entropy(P, Q2)
ce3 = cross_entropy(P, Q3)
ce4 = cross_entropy(P, Q4)
print(f'ce1 = {ce1}\nce2 = {ce2}\nce3 = {ce3}\nce4 = {ce4}')

F_ce1 = F.cross_entropy(T.tensor(L1),T.tensor(P))
F_ce2 = F.cross_entropy(T.tensor(L2),T.tensor(P))
F_ce3 = F.cross_entropy(T.tensor(L3),T.tensor(P))
F_ce4 = F.cross_entropy(T.tensor(L4),T.tensor(P))
print(f'ce1 = {F_ce1}\nce2 = {F_ce2}\nce3 = {F_ce3}\nce4 = {F_ce4}')

F_ce1 = F.cross_entropy(T.tensor([L1]),T.tensor([0]))
F_ce2 = F.cross_entropy(T.tensor([L2]),T.tensor([0]))
F_ce3 = F.cross_entropy(T.tensor([L3]),T.tensor([0]))
F_ce4 = F.cross_entropy(T.tensor([L4]),T.tensor([0]))
print(f'ce1 = {F_ce1}\nce2 = {F_ce2}\nce3 = {F_ce3}\nce4 = {F_ce4}')
print(f'average = {(F_ce1+F_ce2+F_ce3+F_ce4)/4.}')

L = T.tensor(np.array([L1, L2, L3, L4]))
target = T.tensor([0,0,0,0])
ce = F.cross_entropy(L, target)
ce