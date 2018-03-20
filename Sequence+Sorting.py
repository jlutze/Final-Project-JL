
# coding: utf-8

# In[ ]:


# This program is designed to remove very similar but not identical sequences from a file
# I want to remove pairs of sequences with fewer than 2 mismatches because 
# these are functionally identical as Cas9 can bind to sequences with some mismatches from
# its target sequence. Additionally, this will cut down on the number of sequences I have to
# search later on 


# In[1]:


# I use the hamming distance as a proxy for the number of mismatches between two sequences
# I found this simple function online 
def hamming_distance(s1, s2):
    #Return the Hamming distance between equal-length sequences. My sequences are equal length 
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


# In[2]:


def extract_dissimilar_sequences (sequences):
    # create a list to store my sequences as well as some variables for iteration 
    # this only works if the input file is sorted such that similar sequences will be proximal
    # but this is very facile in unix 
    global good_sequences
    good_sequences = [0]
    x = 0
    y = 1

    # I use a while loop to iterate through the sequences in the file 
    while y < (len(sequences)):
        # calculate hamming distance between the first two sequences
        dist = int(hamming_distance(sequences[x], sequences[y]))
        # calculate hamming distance between the 2nd sequence and the last sequence I added to
        # my list of good sequences. This is necessary in the case that I have multiple sequences in
        # a row with small hamming distancebetween them. If mindist is large I will need to
        #exclude multiple sequences in between each one I keep
        newdist = int(hamming_distance(sequences[good_sequences[-1]], sequences[y]))
        # min dist is the minimum number of mismatches two sequences can have
        mindist = 2
        # I add only the second integer if the corresponding sequence is similar to the first 
        # and not similar to the previously added sequence
        if dist < mindist and newdist >= mindist:
            good_sequences.append(y)
        # I add both integers if the corresponding sequences are not similar 
        #and I check to be sure I am not duplicating
        elif dist > mindist and x not in good_sequences:
            good_sequences.append(x)
            good_sequences.append(y)
        # if i am trying to add a duplicate sequence, I exclude it
        elif dist > mindist and x in good_sequences:
            good_sequences.append(y)

        # I then increment my vairables by one 
        x = y
        y = (y+1)
    return(good_sequences)


# In[3]:


# open directory and generate list of files within
from os import listdir
from os.path import isfile, join
mypath = '/Users/julianlutze/Desktop/Test'
onlyfiles = [f for f in listdir(mypath) if not f.startswith(".") if isfile(join(mypath, f))]

for i in range(len(onlyfiles)):
    with open (mypath + '/' + onlyfiles[i]) as f:
        sequences = [line.rstrip('\n') for line in f]
        extract_dissimilar_sequences(sequences)
    with open ((onlyfiles[i].split('.')[0]) + '.dissimilar.txt', 'w') as output:
        min_sequences = []
        for x in good_sequences:
            min_sequences.append(sequences[x])
        output.write("\n".join(min_sequences))
        output.close()
    f.close()
