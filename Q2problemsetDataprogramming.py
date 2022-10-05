#!/usr/bin/env python
# coding: utf-8

# In[2]:


string = 'Supercalifragilisticexpialidocious';
length = len(string);
print(length, "letters in Supercalifragilisticexpialidocious.")


# In[4]:


strval = 'Supercalifragilisticexpialidocious';
if 'ice' in strval:
    print("True")
else:
    print("False")


# In[5]:


str1 = 'Supercalifragilisticexpialidocious';
str2 = 'Honorificabilitudinitatibus';
str3 = 'Bababadalgharaghtakamminarronnkonn';
if len(str1) >= len(str2) and len(str1) >=len(str3):
    print('Supercalifragilisticexpialidocious is the biggest word')
    
elif len(str2) >= len(str1) and len(str2) >= len(str3):
    print('Honorificabilitudinitatibus is biggest word')
    
else:
    print('Bababadalgharaghtakamminarronnkonn is biggest word')


# In[6]:


composerdict = ['Berlioz', 'Borodin','Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
composerdict.sort() 
print(composerdict[0], " its first in the dictionary.")
print(composerdict[6], "its last in the dictionary.")


# In[ ]:




