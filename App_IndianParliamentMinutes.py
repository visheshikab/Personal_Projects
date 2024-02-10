#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st

#from streamlit_jupyter import StreamlitPatcher, tqdm

#StreamlitPatcher().jupyter()  # register streamlit with jupyter-compatible wrappers

import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv(r'C:\Users\vishe\Desktop\Indian Parliament\practice\final.csv')

st.title('Indian Parliament Debate since 1952')
st.header('Analyzing Top Words Used in Indian Parliament Debates')

# Sidebar with year range slider
st.sidebar.title('Year Range Selection')
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_range = st.sidebar.slider('Select Year Range:', min_value=min_year, max_value=max_year, value=(min_year, max_year))

# Filter DataFrame based on selected year range
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Generate word cloud for top_0_words column
word_freq = {}
for index, row in filtered_df.iterrows():
    words_with_prob = eval(row['topic_0_words'])
    for word, prob in words_with_prob:
        word_freq[word] = word_freq.get(word, 0) + prob

# Create the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# Plot the word cloud
st.title('Word Cloud for Selected Year Range')
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

# Display the word cloud
st.pyplot(plt)



# In[11]:





# In[ ]:




