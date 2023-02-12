# Content_addressable_memory_hopfield_network


# Implementation of Content Addressable Memory using Python 
#
#
###  Content Addressable Memory is a memory that can be accessed by content and not by the address.A CAM recalls data based on the input that partially resembles the data itself. 
### Primary application of the Hopfield network is CAM.
#### Eg: a binary number 11001010 can be recalled given an input that resembles it such as 11001000 where one bit has been distorted.
### The key to the memory is a partially distorted version of the data stored in that memory.Recall is essentially a cleanup operation on a partially distorted input. ### In other words, CAM solves the pattern completion problems.Now imagine that the attractor states represented by the minima of the energy surface are memories that have been programmed into the network. Then the application of a distorted version  of a programmed memory to the network should result in distortion being removed to recall the memory correctly. 
### This correct recall operation however depends on the Hamming distance of the initially applied input state vector from the programmed memory.
### To understand this, observe that movement from an initial point (initial state vector) away from an attractor point (memory state vector) on the energy surface amounts to distortion of certain bits in the state vector. 
### Increasing distortion amounts to increasing the distance from the attractor.
### For distortion to a certain extent, the initial point remains within the basin of attraction of the memory state vector and it falls towards the attractor as time evolves and the network is allowed to relax. For larger distortion in the input vector, the initial point might fall outside the basin of attraction of the programmed memory and enter the basin of attraction of the same other memory.
