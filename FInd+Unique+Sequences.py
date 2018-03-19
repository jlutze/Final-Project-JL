
# coding: utf-8

# In[ ]:


# The objective of this program is to take a directory of files containing short sequences and 
# create a new file for each original file wherein the new file contains only sequences
# which were unique to each file. IE it removes duplicates across files within a directory


# In[19]:


# Import stuff needed to access files in a directory
from os import listdir
from os import getcwd
from os.path import isfile, join
# define directory of interest. This should be a folder with more than one file of the same type
mypath = '/Users/julianlutze/Desktop/Test'
# generate list of files to process
onlyfiles = [f for f in listdir(mypath) if f.endswith(".txt") if isfile(join(mypath, f))]

#This outer for loop iterayes through the files in the directory, selecting one at a time
# to remove duplicate sequences from. This is the file of interest. 
for i, x in enumerate(onlyfiles):
    # open the file and read contence into memory
    with open (mypath + "/" + onlyfiles[i]) as file_of_interest:
        lines_of_interest = [line.rstrip('\n') for line in file_of_interest]
        lines_of_interest = set(lines_of_interest)
    # this for loop iterates through the other files in the directory 
    for k in range(len(onlyfiles)):
        # I only want to remove sequences found in files other than my file of interest 
        if i != k:
            # open file to compare and read into memory
            with open (mypath + "/" + onlyfiles[k]) as file_to_compare:
                lines_to_compare = [line.rstrip('\n') for line in file_to_compare]
                lines_to_compare = set(lines_to_compare)
                # generate placeholder containing lines in file of interest which are not in
                # file to compare
            abc = [z for z in lines_of_interest if z not in lines_to_compare]
            lines_of_interest = list(abc)
            file_to_compare.close()
            # Once I have gone through all other files I want to write the remaining sequences
            # wich are unique to my file of interest to an output file
            # i call the output file the original filename with 'unique' added 
    with open((onlyfiles[i].split('.'))[0] + 'unique' + ".txt", 'w') as f:
        f.write("\n".join(lines_of_interest))
        f.close
    file_of_interest.close()

