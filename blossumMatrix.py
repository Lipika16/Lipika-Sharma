import itertools
import math
import numpy
import sys
sequence=[]
#text_file=open('alignment.dat','r')
text_file=open(sys.argv[1],'r') #opens the file which contains the sequence
for sequence in text_file:  # making a list of lists from the sequences in the file
    x=[]
    sequence=sequence.rstrip('\n')
    for amino_acids in sequence:
        x.append(amino_acids)
    sequence.append(x)
#fl=open('scoring matrix.txt','w')
fl=open(sys.argv[2],'w')
seq_len=len(sequence)*len(sequence[0]) #calculates the number of amino acids in the matrix
dict_s={} #dictionary containing the pa(probability of single amino acids)
for i in sequence:
    for j in i:
        if j not in dict_s:
            dict_s[j]=1
        else:
            dict_s[j]+=1
for x,y in dict_s.items():
    dict_s[x]=y/seq_len
#print(dict_s)
comb_pairs=[]
dict_pairs={}  #dictionary containing the pab(probability of pairs of amino acids
for i in range(len(sequence[0])):
    temp=[]
    for j in range(len(sequence)):
        temp.append(sequence[j][i])
    d=itertools.combinations(temp,2) #makes the combinations of pairs of the columns of the matrix
    for i in d:
        comb_pairs.append(''.join(sorted(i)))
for i in comb_pairs:
    if i not in dict_pairs:
        dict_pairs[i]=1
    else:
        dict_pairs[i]+=1
val=sum(dict_pairs.values())
for m,n in dict_pairs.items():
    dict_pairs[m]=n/val
#print(dict_pairs)
exp={} #dictionary containing the expected probability of amino acids
for i,j in dict_pairs.keys():
    e=0
    if i==j: #calculates eaa
        e=dict_s[i]**2
    else: #calculates eab
        e=2*dict_s[i]*dict_s[j]
    exp[i+j]=e
#print(exp)
saa={} #dictionary containing the scores of each pairs of amino acids
for i in exp.keys():
    saa[i]=round(2*math.log2(dict_pairs[i]/exp[i]))
#print(saa)

dp=numpy.zeros((len(dict_s),len(dict_s)),dtype=int) #makes a matrix of uniques amino acids
letters=list(dict_s.keys())
for i,j in saa.keys():
    dp[letters.index(i),letters.index(j)]=saa[i+j] #appending the scores in the matrix
    dp[letters.index(j),letters.index(i)]=saa[i+j] #to fill the symmetric matrix

print("  ",end="",file=fl) #format
for i in letters:
    print('{:>3}'.format(i),end="",file=fl)
print(file=fl)
for i in range(len(dp)):
    print(letters[i],end=" ",file=fl)
    for j in range(len(dp[0])):
        print('{:>3}'.format(dp[i][j]),end="", file=fl)
    print(file=fl)

