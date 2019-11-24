#!/usr/bin/env python
# coding: utf-8

# In[1]:


class fruits:
    
    def _init_(self):
        print('this is a constructor')
        print('this is also prints')
        
    def mango(self):
        print('this is in yellow')
        
    def grape(self):
        print('this is in green')
        


# In[2]:


fobj = fruits()


# In[3]:


fobj.mango()

robj = fruits()
# In[5]:


message = input("tell me something and i will repeat it for you:")
print(message)


# In[6]:


name = input('please enter your name:')
print(f"\n Hello, {name}")


# In[7]:


baby = input('how old are you?')
print(baby)


# In[8]:


baby = input('how old are you?')
baby = int(baby)
print(baby)


# In[9]:


baby>2


# In[10]:


baby>1


# In[12]:


age = input('how old are you?')

age = int(age)

if age>=18:
    print('you are eligible to vote')
else:
    print('try next time!!')


# In[ ]:





# In[ ]:




