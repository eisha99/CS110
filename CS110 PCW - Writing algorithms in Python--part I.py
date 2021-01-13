#!/usr/bin/env python
# coding: utf-8

# Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\rightarrow$Run All).
# 
# Note that this Pre-class Work is estimated to take **26 minutes**.
# 
# Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE", as well as your name and collaborators below:

# In[ ]:


NAME = "Eisha"
COLLABORATORS = "Eisha, extenal sources used for code"


# ---

# # CS110 Pre-class Work - Writing algorithms in Python--part I
# 
# ## Question 1 [time estimate: 10 minutes]
# 
# Palindromes are a sequence of characters (words, phrases, numbers) that can be read the same both from left to right and from right to left. Examples of palindromes include the word 'madam' and the number 12321.
# 
# 1. Explain how you would use an iterative approach, step by step, to check whether a word is a palindrome.
# 2. Explain also how you would approach this problem using a recursive solution.
# 
# You can use palindromic and non-palindromic words to assist your explanation. 

# 1. Using an iterative approach you would define a range for the number of letters/characters within the palindrome and check whether the first and the last are the same, the second and the second last are the same etc. For instance, first we will consider the length of the word l. We would compare the first half of the word from the first letter to the midpoint (l/2) to the second half. Comparion would be between the letter number 1 with letter l-1 (last). A range function can be used to determine which letters to compare within the loop.
# 2. The recursive approach would utilise a base case (for example a word with 0 letters or 1) when the program would stop. If the word is longer than 1 letter, the function would compare the first letter with the last, Given that these are the same the recursive case would be used (the function would call on itself) to determine whether the remaining word also has equal letters in both the begining and the end.

# ## Question 2 [time estimate: 3 minutes]
# 
# How would you prevent your recursive solution from running forever? In other words, what is the base case of your recursive approach?

# The base case for the recursive function would first check if the length og the world is 2 words or above. The function would only run in this case as otherwise it is impossible for the word to be a palindrome. Next when the function checks the first and the last word in the chosen word, if the two words do not match it would stop running.

# ## Question 3 [time estimate: 3 minutes]
# 
# Is there a base case in an iterative approach? Why or why not?

# No because the iterative approach achieves the same via a loop-continuation conditionsuch that when the first and the last letter of the word do not match the loop breaks.

# ## Question 4 [time estimate: 10 minutes]
# 
# Given the algorithmic strategies you described in question 1, you will now implement these in Python code. Write a function for the iterative approach (using either a `for` or a `while` loop) and another function for the recursive approach. Both functions should return `True` if the provided word is a palindrome, and `False` if the word is not. 
# 
# Validate the correctness of your code by providing examples of words that can be used as test cases. Be prepared to paste your functions and Palindrome words you searched into a Minerva workbook during class.

# In[ ]:


def is_palindrome_iterative(word):
    """
    This function identifies whether a word is a palindrome iteratively.

    Parameters
    ----------
    word : str
        Word we wish to check
    
    Returns
    -------
    bool
        True if input is a palindrome, False otherwise
        
    """
    # YOUR CODE HERE
word = input("Input a word")
#this asks the user to input the word
palindrome = True
for i in range(0,len):
    sideone = word[i]
    sidetwo = word[len(word)-i-1]
    if sideone=sidetwo:
        print("palindrome!")
        #this lets the user know that the letter is a palindrome!
else
palindrome = False  


# In[ ]:


def is_palindrome_recursive(word):
    """
    This function identifies whether a word is a palindrome recursively.

    Parameters
    ----------
    word : str
        Word we wish to check
    
    Returns
    -------
    boolean
        True if input is a palindrome, False otherwise
        
    """
    # YOUR CODE HERE
    raise NotImplementedError()
    if len(word)<2:
    return False   
  else:  
    letter1 = word[0]
    letterlast = word[len(word)-1]
    if firstletter == lastletter:
        return("Palindrome!")


# In[ ]:




