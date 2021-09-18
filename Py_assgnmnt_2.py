#!/usr/bin/env python
# coding: utf-8

# ## Q.1

# In[1]:


# Write a program which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
# in a comma-separated sequence on a single line.


# In[4]:


for i in range(2000, 3201):
    if i%7 == 0 and i%5 != 0:
        print(i, end=',')


# ## Q.2

# In[6]:


# Write a Python program to accept the user's first and last name and then getting them 
# printed in the the reverse order with a space between first name and last name.


# In[8]:


first_name = input('Enter your first name:  ')
last_name = input('Enter your Last naem:  ')
print(first_name[::-1],' ',last_name[::-1])


# ## Q.3

# In[9]:


# Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r 3


# In[10]:


volume = 4/3 * 3.14 * (12 ** 3 )
print(volume)


# In[ ]:




