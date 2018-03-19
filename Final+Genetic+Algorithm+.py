
# coding: utf-8

# In[48]:


# This code is my implimentation of a genetic algorithim to find sequences of the form N19NGG which occour very often 
# in a genome or a subset of a genome. I implimented a genetic algorithim here because it would be computationally intensive 
# to search all possible sequences 


# In[49]:


# here I import some required modules
import random
import string
import re
import numpy as np
import copy


# In[50]:


# this is a snippet of code I found online to replace a gievn proportion of characters in astring with radnomly selected
# characters. I want to just randomly mutate my DNA sequence for use in my genetic algorithim later. The mutations happen
# if the code returns a 0 and so the frequence is set by X in the randint portion. If X = 9 for example the chances
# of a mutation are 1/(0-9) or about 10%. I then add 'gg to the end because I want sequences ending in gg
def mut_seq(seq, X):
    seq = ''.join(i if random.randint(0, X) else random.choice('atcg') for i in seq)
    seq_gg = seq + 'gg'
    return seq_gg


# In[51]:


# Here I open the file in which I want to search for matches and read it into memory as a single long character string 
with open("/Users/julianlutze/Desktop/Seq/UniProt-Q9UN81.txt") as myfile:
    seq_test ="".join(line.rstrip() for line in myfile)


# In[60]:


# this code is my genetic algorithim which compares the number of matches in my test file  for two sequences 
# and then selects the sequence with more matches. That sequence is then mutated and the process is repeated n times
def short_GA(start_seq, n):
    loop = 0
    # use a while loop to set the number of iterations
    while loop < n:
        # I provide a random start sequence that I define and then mutate it
        # I also add 'gg' to the end of my starting sequence
        test_seq = mut_seq(start_seq, 5)
        start_seq = start_seq + 'gg'
        # I count the number of matches for my random start sequence and my mutated sequence
        matches_start = re.findall(start_seq, seq_test)
        matches_test = re.findall(test_seq, seq_test)
        # I then retain the mutated sequence if it has more matches than the original sequence, else discard it 
        # I also remove gg from my sequence at the end of the loop
        if len(matches_test) >= len(matches_start):
            start_seq = test_seq
        start_seq = start_seq[:-2]    
        loop = (loop+1)
    # Finally I return the final sequence and the (hopefully high) number of matches after n rounds
    return(len(matches_start), start_seq)

