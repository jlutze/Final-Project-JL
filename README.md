# Final-Project-JL
Hi Stefano

Scientific Explanation:
	My lab is seeking to develop CRISPR/Cas9 technologies for use in the lab. Briefly, Cas9 works by making Double Strand Break in genomic DNA at a specific locus. This locus is determined by a target sequence of the form N19NGG where N is any nucleotide (ATCG). Most labs using Cas9 want to cut at one specific locus and minimize off target effects. There are many programs online which function to search a given genome for matches to a sequence provided and provide a score for a given sequence. Low scoring sequences will occur only once in the genome and provide ideal targets 
	However, my lab wants to search for sequences which occur multiple times in the genome — these sequences should occur as often as possible. In this way Cas9 can be used as a tool to introduce large amounts of DNA damage. Additionally, I would like to search for sequences which occur often in a given portion of the genome. Previous work has divided the genome into functionally distinct states depending on epigenetic information; these states include promotors, enhancers and non-coding regions for example1. I have downloaded this chromatin state information from Encode2. 
In simple terms I want to find sequences of the form N19NGG which occur most often in a given genomic subset. This would be a new computational tool, useable by anyone in my lab. Different persons would need to repeat the analysis for different cell types. 

My project seeks to do the following:
1.	Extract the genomic sequences from .BED files corresponding to each class of genomic region. The .BED files give start and end points of each genomic region corresponding to a given state. 
2.	Process the genomic sequences in UNIX to get them ready for sequence matching. 
3.	Extract sequences of the form N19NGG from the genomic sequences. 
4.	Process the extracted sequences in Unix.
5.	Find sequences which occur in only one genomic state. 
6.	Find sequences which occur in only two genomic states. In this way I hope to find sequences which are enriched in one genomic state relative to another.
7.	Calculate the number of matches for each sequence in the genome. 
8.	Find sequences which occur most often in the genome or in a given genomic class and plot these results. 

I have also added a related code which is an adaptation of a genetic algorithm to find a sequence which occurs very often in a given genomic sequence.  This will accomplish a similar aim to the above programs but without any a priori knowledge of sequences which are in the genome. I decided to write a genetic algorithm because I do not know anything about my sequence space and to search every sequence of the form N19NGG would be very memory intensive (this is ~ 1x 10 12 sequences).  

1.	Ernst, Jason, and Manolis Kellis. "Chromatin-state discovery and genome annotation with ChromHMM." nature protocols 12.12 (2017): 2478.
2.	http://rohsdb.cmb.usc.edu/GBshape/cgibin/hgTrackUi?db=hg19&g=wgEncodeBroadHmm
 
 ...........
 
Directions:
1.	Set your directory to the sequences folder in the GitHub
2.	Run the .sh file in UNIX to isolate N19NGG sequences from each file in the sequences folder. Input and output files are the same for this script.
3.	Run the Find Unique Sequences or Find Sequence Intersection .py scripts on the sequences folder. These will output new files into the same directory.
4.	Run the sequence sorting .py file on the sequences directory.
5.	Open the GenomicMatching.R script and you can run any file containing N19NGG sequences to search for matches in the human genome and output a plot. This script is quite slow. 
6.	The Extract_Genomic_Sequences_From_BED file should not be run. I just included it for completeness. I did not upload a .BED file because the ones I use are very large  
7.	The FinalGeneticAlgorithim .py file is an orthogonal project. It can be run using the GA_matching.txt file which consists of 10000 random DNA bases from the human genome. 

