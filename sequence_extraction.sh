cd ~/desktop/Sequences
for FILE in *.txt
do
    tr -d '\n' < $FILE | grep -o '.\{19\}gg' | sort | uniq | sponge $FILE
done
