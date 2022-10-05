#!/usr/bin/env python
# coding: utf-8

# # Question No 5
# a. write a function inside(x,y,x1,y1,x2,y2) that returns True or False depending on whether thepoint(x,y)lies in the rectangle with lower left corner (x1,y1) and upper right corner (x2,y2)
# 

# In[ ]:


x = int(input("Enter x: "))
y = int(input("Enter y: "))
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

def insiderfn(x,y,x1,y1,x2,y2):
    
    if(x > x1 and x < x2) and (y > y1 and y < y2):
        print('True')
        
    else:
        print('False')
        
inside(x,y,x1,y1,x2,y2)


# B) Use function inside() from part a. to write an expression that tests whether the point (1,1) lies in both of the following rectangles: one with lower left corner (0.3, 0.5) and upper right corner (1.1, 0.7) and the other with lower left corner (0.5, 0.2) and upper right corner (1.1, 2).

# In[3]:


insiderfn(1,1,0.3,0.5,1.1,0.7)


# In[4]:


insiderfn(1,1,0.5,0.2,1.1,2)


# In[ ]:




