#load required packages including biostrings
install.packages("stringr")
install.packages("readr")
library(stringr)
library(ggplot2)
library(dplyr)
source("https://bioconductor.org/biocLite.R")
biocLite("Biostrings")
library(Biostrings)

# load into memory the human genome in Bioconductor format.
# I will search every sequence aginst this genome object
library(BSgenome.Hsapiens.UCSC.hg19)
Geneome <- BSgenome.Hsapiens.UCSC.hg19

# Read in the list of sequences into memory 
# being sure each line is a string
List = read_lines("ListOfSequences", skip = 1)
List <-  as.character(List)
SearchSpace = List

# Here I form a processed dictionary format which is a biostrings object
# this makes for faster sequence matching in the next step
PDict(SearchSpace, max.mismatch=NA, tb.start=NA, tb.end=NA, tb.width=NA, algorithm="ACtree2", skip.invalid.patterns=FALSE)
# the function VCountPDict loops over all chromosomes in the genome class object
# and loops over all sequences in the PDict object made in line 25
DataW<- vcountPDict(SearchSpace, Geneome, max.mismatch = 1, min.mismatch = 0, with.indels = FALSE, fixed = TRUE, algorithm = "auto",collapse = FALSE, weight = 1L, verbose = FALSE)

#Here I write a for loop which goes through all the lines in the object DataW
# and creates an object matches for them
for (row in 1:nrow(DataW)) {
  
  Matches <- DataW$count
  
}

# here I write another for loop which creates a data frame B with all sequences and matches
# and another data frame b with matches greater than a certain threshold
all_matches= NULL
best_matches= NULL
for (i in 1:length(SearchSpace)) {
  Num_Matches<- (sum(Matches[seq(i, length(Matches), length(SearchSpace))]))
  all_matches=rbind(all_matches, data.frame(i, Num_Matches))
}
all_matches$Seq_Name <- List
SD <- sd(all_matches$Num_Matches)
# here i define the threshold above which matches are added to best_matches
Avg<- (0.5*SD+ mean(all_matches$Num_Matches))
Counts<- c(all_matches$Num_Matches)
best_matches <- data.frame(filter(all_matches, Num_Matches >= Avg))

# next I calculate a fold change for each sequence as well as the standard deviation
# I then append these to the dataframe
Fold_Change = NULL
StdDev = NULL
for (i in 1:nrow(best_matches)) {
  Fold_Change <- c(Fold_Change, (best_matches[i, 2]/(mean(all_matches$Num_Matches))))
  StdDev <- c(StdDev, (best_matches[i, 2]/SD))
}
best_matches$Fold_Change <- Fold_Change
best_matches$StdDev <- StdDev

# next I order the dataframe with the best matches by the number of matches
best_matches = best_matches[order(-best_matches$Num_Matches),]
# I then write the best match dataframe to a CSV file. This is my final
# output for my code. I can look at this file to get my Cas9 sequences
# of interest in my experiment
write.csv(best_matches, file = "best_matches.csv",row.names=FALSE)
#I then output some information about my matches
print(mean(all_matches$Num_Matches))
print(mean(best_matches$Num_Matches))
#and then plot all data to get a sense of my sequence space 
ggplot(data=all_matches, aes(x=i, y=Num_Matches)) +
  geom_bar(stat="identity")
