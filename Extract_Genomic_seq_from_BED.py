
# coding: utf-8

# In[ ]:


# I have not provided the human genome fasta file as it is very large 
# So this code will not run with what is provided in the GitHub


# In[13]:


# Import Required Modules to extract sequences from BED files
#I mostly googled how to do this
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from collections import defaultdict


# In[ ]:


# This function extracts genomic sequences using coordinates provided in a BED file
# The genome is always the same (Human Genome) but the BED file will differ
def Extract_Genomic_Sequence_From_BED (BEDfile, genome = ):
    # parse fasta file and turn into dictionary
    Hum_Genome_sequence = SeqIO.to_dict(SeqIO.parse(open(genome), 'fasta'))
    # read names and coordinates from bed file
    coordinates = defaultdict(list)
    with open(BEDfile) as f:
        for line in f:
            name, start, stop = line.split()
            coordinates[name].append((int(start), int(stop)))
    sequences_of_interest = []
    for name in coordinates:
        for (start, stop) in coordinates[name]:
            long_seq_record = Hum_Genome_sequence[name]
            long_seq = long_seq_record.seq
            alphabet = long_seq.alphabet
            short_seq = str(long_seq)[start-1:stop]
            short_seq_record = SeqRecord(Seq(short_seq, alphabet), id=name, description='')
            sequences_of_interest.append(short_seq_record)
    # write sequences of interest (extracted based on coordinates in BED file) 
    #to output fasta file
    with open('Weak_enhancer.fasta', 'w') as f:
    SeqIO.write(short_seq_records, f, 'fasta')
    return 42


# In[ ]:


# This yields a large fasta file with genomic sequences corresponding to the ChromHMM classes.
# The next step is to extract sequences of the form N19NGG from these fasta files. I will do 
# this in UNIX

