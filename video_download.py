#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pytube import YouTube
link = input("Masukan Link Video")
video=YouTube(link)
stream=video.streams.get_highest_resolution()
stream.download()


# In[ ]:




