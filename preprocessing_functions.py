import pandas as pd
import numpy as np
import re
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import spacy
nlp = spacy.load('en_core_web_sm')


def remove_usernames(post):
    '''
    Function that takes in a string and removes any words with the symbol @ in 
    it. Use this in a list comprehension.
    ---
    Input: <string>
    ---
    Returns: <string>
    '''  
    post = post.split()
    to_remove = [word for word in post if '@' in word]    
    for word in to_remove:
        post.remove(word)
    return ' '.join(post)


def make_alphabetic(text):
    """
    A helper function to remove numbers and punctuation before passing the
    data to my preprocessing pipeline
    ---
    Input: <string>
    ---
    Returns: <string>
    """
    text = re.sub(r"[^A-Za-z\s]*",'', text)
    text = re.sub("\n", '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub("  ", ' ', text)
    return text, text.split()


def extract_hashtags(text):
    """
    A helper function to extract hashtags for future EDA.
    ---
    Input: <string>
    ---
    Returns: <string>
    """
    ht = re.findall(r"#(\w+)", text)
    return ht


def make_vader_score(df1, column):
	"""
	A helper function to convert VADER compound scores into categories. Positive
	if greater than 0.05, Negative is less than -0.05, and Neutral for scores
	in between.
    ---
    Input: Pandas dataframe and column containing compound VADER scores
    ---
    Returns: <string>
	"""
	scores = []
	for i in range(len(df1)):
		x = df1.iloc[i][column]
		if x > 0.05:
			scores.append("Positive")
		elif x < -0.05:
			scores.append("Negative")
		else:
			scores.append('Neutral')
	return scores
