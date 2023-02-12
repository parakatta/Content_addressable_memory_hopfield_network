# Implementation of Content Addressable Memory using Python 


import numpy as np

#memory vectors to be stored as memory. These can be any bits of your choice
mem_vectors = np.array( [[1, 1 ,0, 0, 0 ,0],
 [0, 0 ,0 ,0, 1 ,1],
 [0, 0 ,1, 1 ,0, 0]])

q = len(mem_vectors)
n = len(mem_vectors[0])

#define bipolar memory vectors 
bip_mem_vecs = 2*(mem_vectors) - 1
print(q,n,bip_mem_vecs)

#calculate weight matrix
for i in range(0,q) :
 zd_wt_mat = zd_wt_mat + bip_mem_vecs[i].conj().transpose()*bip_mem_vecs[i]
zd_wt_mat = zd_wt_mat - q*np.identity(n)

#probe = np.array([0,0,0,1,0,1])
print('Enter the probe vector: ')  #you can ask for input or hardcode value
signal_vector = 2*probe - 1
flag = np.array([0])

# this loop runs till the flag is less than the probe vector
while len(flag) != n :
    permindex = np.random.permutation(n)
    old_signal_vector = signal_vector

    for j in range(1,n):    
      act_vec = signal_vector * zd_wt_mat
      print(act_vec[permindex[j]])
      if (act_vec[permindex[j]]).all() > 0:
        
        signal_vector[permindex[j]] = 1
      elif act_vec[permindex[j]].all() < 0:
        signal_vector[permindex[j]] = -1
      print(type(signal_vector),type(old_signal_vector))
    flag = signal_vector * old_signal_vector

#the recalled vector will be close or similar to one of the memory
#vectors specified. Depends on how well the network recalled the vector 
print('The recalled vector is ',signal_vector)
print(0.5*(signal_vector + 1))