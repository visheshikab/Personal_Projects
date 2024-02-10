{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3df54408-6dff-43dc-a1ed-f3e93008e531",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "# Indian Parliament Debate Trends since 1952"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "## Analyzing Top Words Used in Indian Parliament Debates"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "# Word Cloud for Selected Year Range"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "\n",
    "from streamlit_jupyter import StreamlitPatcher, tqdm\n",
    "\n",
    "StreamlitPatcher().jupyter()  # register streamlit with jupyter-compatible wrappers\n",
    "\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "from wordcloud import WordCloud\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Load the CSV file\n",
    "df = pd.read_csv(r'C:\\Users\\vishe\\Desktop\\Indian Parliament\\practice\\final.csv')\n",
    "\n",
    "st.title('Indian Parliament Debate since 1952')\n",
    "st.header('Analyzing Top Words Used in Indian Parliament Debates')\n",
    "\n",
    "# Sidebar with year range slider\n",
    "st.sidebar.title('Year Range Selection')\n",
    "min_year = int(df['year'].min())\n",
    "max_year = int(df['year'].max())\n",
    "year_range = st.sidebar.slider('Select Year Range:', min_value=min_year, max_value=max_year, value=(min_year, max_year))\n",
    "\n",
    "# Filter DataFrame based on selected year range\n",
    "filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]\n",
    "\n",
    "# Generate word cloud for top_0_words column\n",
    "word_freq = {}\n",
    "for index, row in filtered_df.iterrows():\n",
    "    words_with_prob = eval(row['topic_0_words'])\n",
    "    for word, prob in words_with_prob:\n",
    "        word_freq[word] = word_freq.get(word, 0) + prob\n",
    "\n",
    "# Create the word cloud\n",
    "wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)\n",
    "\n",
    "# Plot the word cloud\n",
    "st.title('Word Cloud for Selected Year Range')\n",
    "plt.figure(figsize=(10, 5))\n",
    "plt.imshow(wordcloud, interpolation='bilinear')\n",
    "plt.axis('off')\n",
    "\n",
    "# Display the word cloud\n",
    "st.pyplot(plt)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a98c9e2-e440-47f9-8f95-410470489e47",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f2242994-e2c9-4149-a235-6b040315c233",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.0b3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
