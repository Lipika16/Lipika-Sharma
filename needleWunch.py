#Lipika Sharma (Assignment-8)

from sys import argv
import numpy as np


def fasta_list(filename):
    with open(filename, 'r') as filename:
        sequ = ''
        head = next(filename)
        for i in filename:
            sequ += i.rstrip('\n')
    return head[1:], sequ


def read_blosum(filename):
    new_dict = {}
    position = 0
    with open(filename, 'r') as f:
        keys = f.readline().strip().split()
        for line in f:
            line = line.strip().split()
            if len(line) > 0:
                temp = {}
                for pos in range(len(keys)):
                    temp[keys[pos]] = float(line[pos + 1])
                new_dict[keys[position]] = temp
                position += 1
    return new_dict


def global_alignement(w, blosum, seq_file1, seq_file2):
    blosum = read_blosum(blosum)
    seq1 = fasta_list(seq_file1)[1]
    seq2 = fasta_list(seq_file2)[1]
    matrix=np.zeros((len(seq2),len(seq1)),np.int)
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            matrix[j][i] = max(matrix[j][i] + blosum[seq1[i]][seq2[j]], matrix[j - 1][i] + w, matrix[j][i - 1] + w)
    return matrix


print(global_alignement(int(argv[1]), argv[2], argv[3], argv[4]))
#global_alignement(-5,'blosum62.txt','GLB7A_CHITH.fasta','GLBE_CHITH.fasta')
#print(np.zeros((5,3),np.int))
