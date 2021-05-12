#!/usr/bin/env python
# coding: utf-8

# In[65]:


import tensorflow as tf
from tensorflow import keras
inp = []
dictlist = []

model = keras.models.load_model('epicmodel2')
#INPUT THE STRING FROM GUI HERE

text = 'I am a sad man with sad feelings'
max_length = 60
num_words = 92409
Health = ['Depression','Anxiety','Bipolar']


# In[66]:


import pickle
word_index = pickle.load( open( "file.pkl", "rb" ) )


# In[67]:


l1 = []

l1 = list(word_index.keys())


# In[68]:


def conv(text):    
    l = text.split()
    for word in l:
        if(word in l1):
            inp.append(l1.index(word))
        else:
            pass
        
        

        
        
conv(text)
#padding        
inp += [0] * (60 - len(inp))    

 
        


# In[69]:


import numpy as np
inp = np.array(inp)


# In[ ]:





# In[70]:


inp1 = np.reshape(inp,(1,60))


# In[ ]:





# In[71]:



prediction = model.predict(inp1)
#pickle.dump(prediction,open('prediction.pkl','wb'))


# In[72]:


print(prediction)


# In[73]:


# print(text)
print(Health[np.argmax(prediction)])  #USE THE OUTPUT FROM THIS TO DISPLAY 


# In[74]:


print(prediction)


# In[75]:


print(type(prediction))


# In[79]:


l3=prediction.tolist()


# In[81]:


print(l3[0][0])


# In[ ]:




