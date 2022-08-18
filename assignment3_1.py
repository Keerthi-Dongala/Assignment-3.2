#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2


# In[2]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df= plt.figure()
a= df.add_axes([0,0,1,1])
a.plot(x,y)
a.set_xlabel('x')
a.set_ylabel('y')
a.set_title('title')


# In[4]:


df = plt.figure()
b= df.add_axes([0,0,1,1])
c= df.add_axes([0.2,0.5,.2,.2])


# In[14]:


df = plt.figure()
b= df.add_axes([0,0,1,1])
c= df.add_axes([0.2,0.5,.2,.2])
b.plot(x,y,color="red")
b.set_xlabel('x')
b.set_ylabel('y')
c.set_xlabel('x')
c.set_ylabel('y')
c.plot(x,y,color="red")


# In[15]:


df= plt.figure()

a= df.add_axes([0,0,1,1])
c= df.add_axes([0.2,0.5,.4,.4])


# In[34]:


a.plot(x,z)
a.set_xlabel('X')
a.set_ylabel('Z')


c.plot(x,y)
c.set_xlabel('X')
c.set_ylabel('Y')
c.set_title('zoom')
c.set_xlim(20,22)
c.set_ylim(30,50)

df


# In[21]:


df, axes = plt.subplots(nrows=1, ncols=2)


# In[22]:


axes[0].plot(x,y,color="blue", lw=3, ls='--')
axes[1].plot(x,z,color="red", lw=3, ls='-')
df


# In[33]:


import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2
df, axes = plt.subplots(nrows=1, ncols=2,figsize=(12,2))
axes[0].plot(x,y,color="blue", linewidth=3)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
df
axes[1].plot(x,z,color="red", linewidth=2, linestyle="dashed")
axes[1].set_xlabel('x')
axes[1].set_ylabel('z')
df


# In[ ]:





# In[ ]:




