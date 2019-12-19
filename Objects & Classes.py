#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the library

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


class Circle(object):
    
#Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius;
        self.color = color;
    
    
        


# In[13]:


RedCircle = Circle(10, 'red')


# In[14]:


RedCircle


# In[15]:


dir(RedCircle)


# In[16]:


RedCircle.radius


# In[17]:


RedCircle.color


# In[19]:


RedCircle.radius = 1
RedCircle.radius


# In[21]:


RedCircle.add_radius(2)


# In[22]:


print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)


# In[23]:


BlueCircle = Circle(radius=100)


# In[44]:


BlueCircle.drawCircle


# In[45]:


class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  


# In[63]:


# Create a class Circle

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  


# In[64]:


RedCircle = Circle(10, 'red')


# In[66]:


RedCircle.drawCircle()


# In[31]:


RedCircle.radius


# In[38]:


class Rectangle(object):
    def __init__(self,width=4,height=5,color ='red'):

        self.width=width
        self.height = height
        self.color = color
    
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()


# In[67]:


SkinnyRedRectangle = Rectangle(2,3,'yellow')


# In[40]:


SkinnyRedRectangle.width


# In[41]:


SkinnyRedRectangle.height


# In[42]:


SkinnyRedRectangle.color


# In[68]:


SkinnyRedRectangle.drawRectangle()


# In[ ]:




