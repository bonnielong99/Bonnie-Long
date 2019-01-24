
# coding: utf-8

# Bonnie Long January 24, 2019 Thermal Expansion 

# In[1]:


import numpy as np
def Rule4(Q,errorA,errorB,errorC,m,n,o,A,B,C):
    errorQ = Q*np.sqrt(((m*(errorA/A))**2) + ((n*(errorB/B))**2) + ((o*(errorC/C))**2))
    return errorQ

alpha = .00002582925883
Delta_L = .00111 #m
delta_Delta_L = 0.00001414213562 #m
L = .699 #m
delta_L = .0005 #m
Delta_T = 61.48 #C
delta_Delta_T = 0.1272792206 #C
m = 1
n = -1
o = -1

error_alpha = Rule4(alpha, delta_Delta_L, delta_L, delta_Delta_T, m, n, o, Delta_L, L, Delta_T)
print (error_alpha)


# In[2]:


import numpy as np
def Rule4(Q,errorA,errorB,errorC,m,n,o,A,B,C):
    errorQ = Q*np.sqrt(((m*(errorA/A))**2) + ((n*(errorB/B))**2) + ((o*(errorC/C))**2))
    return errorQ

alpha = .00001973684211
Delta_L = .00084 #m
delta_Delta_L = 0.00001414213562 #m
L = .700 #m
delta_L = .0005 #m
Delta_T = 60.80 #C
delta_Delta_T = 0.1272792206 #C
m = 1
n = -1
o = -1

error_alpha = Rule4(alpha, delta_Delta_L, delta_L, delta_Delta_T, m, n, o, Delta_L, L, Delta_T)
print (error_alpha)

