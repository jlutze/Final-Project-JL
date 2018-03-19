
# coding: utf-8

# In[ ]:


# The objective of this program is to take a directory of files containing short sequences and 
# create a new file for each original file wherein the new file contains only sequences
# which occour in any pair of files in the original directory. IE it finds the union of every 
# two files in a directory 


# In[4]:


# import modules needed 
from os import listdir
from os.path import isfile, join
pairs = []
# generate a list of files in the directory given by mypath 
mypath = '/Users/julianlutze/Desktop/Test'
onlyfiles = [f for f in listdir(mypath) if not f.startswith(".") if not f.endswith(".ipynb") if isfile(join(mypath, f))]


# In[5]:


#generate a list of all possible pairs of files in the directory
list_of_pairs = [(onlyfiles[p1], onlyfiles[p2]) for p1 in range(len(onlyfiles)) for p2 in range(p1+1,len(onlyfiles))]
print(list_of_pairs)


# In[14]:


#iterate through the list of pairs
for x in list_of_pairs:
    #read the two files in a given pair into memory
    with open (mypath + '/' + x[0]) as f:
        lines1 = [line.rstrip('\n') for line in f]
    with open (mypath + '/' + x[1]) as g:
        lines2 = [line.rstrip('\n') for line in g]
        #create an output file to store the union of sequences and then write the union 
        # of sequences into that file 
    with open(x[0].split('.')[0] +'_union_' + x[1].split('.')[0] + ".txt", "w") as text_file:
        y= list(set(lines1) & set(lines2))
        text_file.write("\n".join(y))
    text_file.close()


# In[ ]:


# This code could be combined with the unique sequences extraction code to generate sequences
# found only in the union of a single pair of files

