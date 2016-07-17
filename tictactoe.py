
# coding: utf-8

# In[1]:

import numpy as np
import os
from random import randint


# In[2]:

def loseLose():
    #row-wise
    flag=0
    for i in range(3):
        #print ("row")
        count=0
        position=0
        for j in range(3):
            if tt_matrix[i,j]==2:
                count = count+1
            else:
                position=j
        if count==2:     
            if tt_matrix[i,position]!=1:
                tt_matrix[i,position]=1
                flag=1
    if flag==0:
        #column-wise
        #print ("col")
        for j in range(3):
            count=0
            position=0
            for i in range(3):
                if tt_matrix[i,j]==2:
                    count = count+1
                else:
                    position=i
            if count==2:     
                if tt_matrix[position,j]!=1:
                    tt_matrix[position,j]=1
                    flag=1
    if flag==0:
        #print ("dia")
        #diagonal-wise
        for i in range(3):
           
            count = 0
            position=0
            for i in range(3):
                if tt_matrix[i,i]==2:
                    count = count+1
                    
                else:
                    position=i
                    
        if count==2:    
            
            if tt_matrix[position,position]!=1:
                tt_matrix[position,position]=1
                flag=1
    if flag==0:
        #print ("AI")
        flag1=0
        for _ in range(9):
            if flag1==0:
                r = randint(1,9)
                for i in range(3):
                    for j in range(3):
                        if r == if_matrix[i,j]:
                            if tt_matrix[i,j] < 1:
                                tt_matrix[i,j]=1
                                flag1=1
                            


# In[ ]:

if __name__ == "__main__":
    tt_matrix = np.zeros((3,3))
    if_matrix = np.zeros((3,3))
    count =0
    for i in range(3):
        for j in range(3):
            if_matrix[i,j]=count+1
            count = count+1
    print if_matrix
    while True:
        player = int(raw_input("Enter your position.."))
	os.system('clear')
	print if_matrix
        for i in range(3):
            for j in range(3):
                if player == if_matrix[i,j]:
                    if tt_matrix[i,j] < 1:
                        tt_matrix[i,j]=2
                        loseLose()
                        print tt_matrix
                    else:
                        print "Wrong position..."
       


# In[ ]:



