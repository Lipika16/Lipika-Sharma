import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pdf
import fastatools as ft
codontable = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M','ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
              'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K','AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
              'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L','CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
              'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q','CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
              'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
              'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
              'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S','TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
              'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_','TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def translated_sequance(inputfile,outputfile):

    with open(inputfile,"r") as infilename:
        list1=ft.fasta_list(infilename)
        with open(outputfile,'w') as file_write:
            for i in list1:
                seq=''
                for j in range(0,len(i[1]),3):
                    sub = i[1][j:j+3]
                    if len(sub)==3:
                        seq+=codontable[sub]
                #print(seq)
                ft.write_fasta(file_write,i[0],seq[:-1])

#translated_sequance("ecoli-genes-ATG.ffn",'test.txt')
def frequencies(filename):
    freq_dict={}
    sub_freq={}
    with open(filename,'r') as read_file:
        sequances_list=ft.fasta_list(read_file)
        for i in sequances_list:
            for j in range(0,len(i[1]),3):
                codon = i[1][j:j+3]
                if len(codon)==3:
                    if codon in sub_freq:
                        sub_freq[codon]+=1
                    else:
                        sub_freq[codon]=1
        for key1,value1 in sub_freq.items():
            amino=codontable[key1]
            if not amino == 'T' or amino == 'M':
                if amino in freq_dict:
                    freq_dict[amino].append((key1,value1))
                else:
                    freq_dict[amino]=[(key1,value1)]
        return freq_dict

#print(frequencies('ecoli-genes-ATG.ffn'))
with pdf.PdfPages('test.pdf') as pdf_file:
    drosophila=frequencies('chr2L.ffn')
    ecoli=frequencies('ecoli-genes.ffn')
    for key1,value1 in ecoli.items():
        lables_list=[]
        freq1=[]
        freq2=[]
        value1=sorted(value1,key=lambda i:i[0])
        sub_drosophila=sorted(drosophila[key1],key=lambda i:i[0])
        for i in value1:
            lables_list.append(i[0])
            freq1.append(i[1])
        for i in sub_drosophila:
            freq2.append(i[1])
        indexes=list(range(len(freq1)))
        indexes2=[i+0.4 for i in indexes]
        label_index=[i+0.2 for i in indexes]
        figure,ax=plt.subplots()
        ax.bar(indexes,freq1,0.4,color='blue')
        ax.bar(indexes2,freq2,0.4,color='r')
        ax.set_title(key1+": ecoli vs drosphila")
        ax.legend(['ecoli','drosphila'])
        ax.set_xticks(label_index)
        ax.set_xticklabels(lables_list)
        pdf_file.savefig()
        plt.close()