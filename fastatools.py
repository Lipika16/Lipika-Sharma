def single_fasta_sequence(filename):
    hd=''
    seq=''
    hd=next(filename)
    hd=hd.rstrip('\n')
    for i in filename:
        seq+=i.rstrip('\n')
    return hd,seq

def fasta_list(filename):
    a=[]
    for i in filename:
        i=i.rstrip('\n')
        if i[0]==">":
            i='*'+i[1:]+'*'
        a.append(i)
    a=''.join(a)
    h=a.split('*')[1:]
    ll=[]
    for f in range(0,len(h),2):
        ll.append((h[f],h[f+1]))
    return ll

def fasta_sequences(filename):
    seq=''
    hd=''
    counter=0
    for i in filename:
        i=i.rstrip('\n')
        if i[0]==">":
            if counter>0:
                yield hd,seq
                seq=''
            hd=i
            counter+=1
        else:
            seq+=i
    else:
        yield hd,seq

'''f=open("ecoli-proteome.faa",'r')
max1=0
for i,j in fasta_sequences(f):
    if len(j)>max1:
        max1=len(j)
print(max1)
f.close()
f=open("ecoli-proteome.faa",'r')
min1=max1
for i,j in fasta_sequences(f):
    if len(j)<min1:
        min1=len(j)
print(min1)
f.close()
'''
def sequences():
    filename=open("ecoli-genes-ATG.ffn")
    outfile=open("writeseq","w")
    def write_fasta(outfile):
        oo=fasta_list(filename)
        for i in oo:
            outfile.write(i[0])
            for j in range(0,len(i[1]),70):
                outfile.write(i[1][j:j+70])

def write_fasta(outfile,head,seq):

    if outfile.tell()==0:

        outfile.write(head)
    else:
        outfile.write('\n'+head)
    for j in range(0,len(seq),70):
        outfile.write('\n'+seq[j:j+70])
