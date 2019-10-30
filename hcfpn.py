#!/usr/bin/env python
# coding: utf-8

# In[3]:


def f2(x,y):
    if(x<y):
        a = x
    else:
        a =y
    for i in range(0,a+1):
        if(x%a==0 and y%a==0):
            return("hcf=",a)
            break
        
        
f2(30,40)
    


# In[1]:


def h2(x,y):
    if (x<y):
        k =x
    else:
        k=y
        
    while (k>0):
        if (x%k==0) and (y%k==0):
            print (k,"is HCF")
            break
        k=k-1
        


# In[1]:


def p1(x):
    a= x
    k =0
    i =1
    while(i<a+1):
        if(a%i==0):
            k = k+1
        i = i+1
    if (k ==2):
        return("it is prime number")
    else:
        return("it is not prime  number")

    


# In[ ]:





# In[ ]:




