#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork1005-2023-01-01">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# <center>
# 
# # Practice lab
# 
# </center>
# 

# <center>
#     
# # **Scenario: Text Analysis**
# 
# </center>
# 

# Estimated time needed: **30** minutes
# 

# # What is Text analysis?
# Text analysis, also known as text mining or text analytics, refers to the process of extracting meaningful information and insights from textual data.
# 

# ## Objectives
#  
# Upon finishing this laboratory exercise, you will gain proficiency in employing various techniques in combination.
# 

# ## Setup
# 

# For this lab, we will be using the following data types:
# * List
# * Strings
# * Classes and objects
# 

# # Let's consider a real-life scenario where you are analyzing customer feedback for a product. You have a large dataset of customer reviews in the form of strings, and you want to extract useful information from them using the three identified tasks:
# 
# **1. String in lower case:**
# You want to Pre-process the customer feedback by converting all the text to lowercase. This step helps standardize the text. Lower casing the text allows you to focus on the content rather than the specific letter casing.
# 
# **2. Frequency of all words in a given string:**
# After converting the text to lowercase, you want to determine the frequency of each word in the customer feedback. This information will help you identify which words are used more frequently, indicating the key aspects or topics that customers are mentioning in their reviews. By analyzing the word frequencies, you can gain insights into the most common issues raised by customers.
# 
# **3. Frequency of a specific word:**
# In addition to analyzing the overall word frequencies, you want to specifically track the frequency of a particular word that is relevant to your analysis. For example, you might be interested in monitoring how often the word "reliable" appears in the customer reviews to gauge customer sentiment about the product's reliability. By focusing on the frequency of a specific word, you can gain a deeper understanding of customer opinions or preferences related to that particular aspect.
# 
# By performing these tasks on the customer feedback dataset, you can gain valuable insights into customer sentiment
# 

# ----
# 

# ## Below is the given string
# 

# In[1]:


givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."


# ### For achieving the above 3 task, We need to create a class with 3 different methods.
# 

# ##### Follow the intruction given in each task and create a class with different methods
# 

# # Task-1 Define the class and its attributes:
# 

# 1. Create a class named TextAnalyzer.
# 2. Define the constructor `__init__` method that takes a text argument.
# 

# In[3]:


# type your code here
class TextAnalyzer(object):
    def __init__(self,text):
        self.text=text


# <details><summary>Click here for the solution</summary>
# 
# ```python
# class TextAnalyzer(object):
#     def __init__(self, text):
#         
#             
# ```
# 
# </details>
# 

# ----
# 

# # Task-2 Formatting the text:
# 

# 1. Inside the constructor, convert the text argument to lowercase using the `lower()` method.
# 2. Remove punctuation marks (periods, exclamation marks, commas, and question marks) from the text using the `replace()` method.
# 3. Assign the formatted text to a new attribute called fmtText.
# 
# **Update the above `TextAnalyzer` class with points mentioned above.**
# 

# In[5]:


# Type your code here 
class TextAnalyzer(object):
    def __init__(self,text):
        fmtText=text.lower()
        fmtText=fmtText.replace('.','').replace('!','').replace('?','').replace(',','')
        slef.fmtText=fmtText


# <details><summary>Click here for the solution</summary>
# 
# ```python
# class TextAnalzer(object):
#     
#     def __init__ (self, text):
#         # remove punctuation
#         formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
#         
#         # make text lowercase
#         formattedText = formattedText.lower()
#         
#         self.fmtText = formattedText
#         
#             
# ```
# 
# </details>
# 

# ----
# 

# # Task-3 Frequency of all unique words:
# 

# * Implement the `freqAll()` method:
#      1. Split the fmtText attribute into individual words using the `split()` method.
#      2. Create an empty dictionary to store the word frequency.
#      3. Iterate over the list of words and update the frequency dictionary accordingly.
#      4. use `count` method for counting the occurence
#      5. Return the frequency dictionary.
#      
# **Update the above `TextAnalyzer` class with points mentioned above.**
# 

# In[7]:


# type your code here
class TextAnalyzer(object):
    def __init__(self,text):
        fmtText=text.lower()
        fmtText=fmtText.replace('.','').replace('!','').replace('?','').replace(',','')
        slef.fmtText=fmtText
    def freqAll(self,fmtText):
        Dict={}
        words=[]
        words=self.fmtText.split(' ')
       
        for key in set(words):
            Dict[key]=word.count(key)
        return Dict
        


# <details><summary>Click here for the solution</summary>
# 
# ```python
# class TextAnalyzer(object):
#     
#     def __init__ (self, text):
#         # remove punctuation
#         formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
#         
#         # make text lowercase
#         formattedText = formattedText.lower()
#         
#         self.fmtText = formattedText
#         
#     def freqAll(self):        
#         # split text into words
#         wordList = self.fmtText.split(' ')
#         
#         # Create dictionary
#         freqMap = {}
#         for word in set(wordList): # use set to remove duplicates in list
#             freqMap[word] = wordList.count(word)
#         
#         return freqMap
#     
#             
# ```
# 
# </details>
# 

# ----
# 

# # Task-4 Frequency of a specific word:
# 

# * Implement the `freqOf(word)` method that takes a word argument:
#    1. create method and pass the word that need to be found
#    2. get the `freqAll` method for look for count and check if that word is in the list.
#    3. Return the count.
#    
# **Update the above `TextAnalyzer` class with points mentioned above.**
# 

# In[33]:


# type your code here 
class TextAnalyzer(object):
    def __init__(self,text):
        fmtText=text.lower()
        fmtText=fmtText.replace('.','').replace('!','').replace('?','').replace(',','')
        self.fmtText=fmtText
    def freqAll(self):
        Dict={}
        words=[]
        words=self.fmtText.split(' ')
    
        for key in set(words):
            Dict[key]=words.count(key)
        return Dict
    def freqOf(self,word):
        Dict=self.freqAll()
        if word in Dict:
            return Dict[word]
        else:
            return 0


# <details><summary>Click here for the solution</summary>
# 
# ```python
# class TextAnalyzer(object):
#     
#     def __init__ (self, text):
#         # remove punctuation
#         formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
#         
#         # make text lowercase
#         formattedText = formattedText.lower()
#         
#         self.fmtText = formattedText
#         
#     def freqAll(self):        
#         # split text into words
#         wordList = self.fmtText.split(' ')
#         
#         # Create dictionary
#         freqMap = {}
#         for word in set(wordList): # use set to remove duplicates in list
#             freqMap[word] = wordList.count(word)
#         
#         return freqMap
#     
#     def freqOf(self,word):
#         # get frequency map
#         freqDict = self.freqAll()
#         
#         if word in freqDict:
#             return freqDict[word]
#         else:
#             return 0
#     
#             
# ```
# 
# </details>
# 

# ## Now, We have successfully created a class with 3 methods
# 

# ## Task-5 Create an instance of TextAnalyzer Class.
# 

# In[34]:


# type your code here
sentence=TextAnalyzer("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")


# <details><summary>Click here for the solution</summary>
# 
# ```python
# analyzed = TextAnalyzer(givenstring)
# ```
# 
# </details>
# 

# ## Task-6 Print the formatted text(lower case string)
# 

# In[35]:


# type your code here
sentence.fmtText


# <details><summary>Click here for the solution</summary>
# 
# ```python
# print("Formatted Text:", analyzed.fmtText)
# ```
# 
# </details>
# 

# ## Task-7 Test freqAll() method
# 

# In[37]:


# type your code here
sentence.freqAll()


# <details><summary>Click here for the solution</summary>
# 
# ```python
# freqMap = analyzed.freqAll()
# print(freqMap)
# ```
# 
# </details>
# 

# ## Task-8 Test freqOf() method
# you have to find the frequency of the following words:-
# 1. "lorem"    
# 2. "diam"   
# 3. "et"    
# <br>
# 
# print the output using **formatting**
# 

# In[41]:


# type your code here
sentence.freqOf('et')


# <details><summary>Click here for the solution</summary>
# 
# ```python
# word = "lorem"
# frequency = analyzed.freqOf(word)
# print(f"The word '{word}' appears {frequency} times.")
# ```
# 
# </details>
# 

# <details><summary>Click here for the solution</summary>
# 
# ```python
# word = "diam"
# frequency = analyzed.freqOf(word)
# print(f"The word '{word}' appears {frequency} times.")
# ```
# 
# </details>
# 

# <details><summary>Click here for the solution</summary>
# 
# ```python
# word = "et"
# frequency = analyzed.freqOf(word)
# print(f"The word '{word}' appears {frequency} times.")
# ```
# 
# </details>
# 

# ----
# 

# ## Authors
# 

# Author1 <br>
# **Akansha yadav**
# 

# ### Other Contributors
# 

# [Contributor with Link](contributor_linl), Contributor No Link
# 

# ## Change Log
# 

# |Date (YYYY-MM-DD)|Version|Changed By|Change Description|
# |-|-|-|-|
# |2023-05-17|0.3|Akansha yadav| Created lab under maintenance|
# |2020-07-17|0.1|Sam     |Create Lab Template|
# |2022-11-19|0.2|Shengkai|Update Lab Template|
# 

# Copyright © 2022 IBM Corporation. All rights reserved.
# 
