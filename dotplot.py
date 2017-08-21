import matplotlib.pylab as plt
import numpy
def dotplot(seqA,seqB,w,s):
    dp=numpy.zeros((len(seqA),len(seqB)),dtype=int)
    a=int(w/2)
    for i in range(0,len(seqA)-w+1):
        #print(seqA[i:i+w])
        for x in range(0,len(seqB)-w+1):
            counter=0
            #print(seqA[i:i+w],seqB[x:x+w])
            for y in range(0,w):
                if seqA[i:i+w][y]==seqB[x:x+w][y]:
                    counter+=1
            if counter>=s:
                dp[i+a][x+a]=1
    return dp
print(dotplot("WINDQWS","WQNDERS",3,2))
def dotplotASCII(dp,seqA,seqB,heading,filename):
    f = open("first-dotplot.txt","w")
    print(heading, file=f)
    print('|' + seqB,file=f)
    for i in range(len(dp)):
        print(seqA[i], end='', file=f)
        for j in range(len(dp[0])):
            if dp[i][j]==0:
                print(" ", end='', file=f)
            elif dp[i][j]==1:
                print("*", end='', file=f)
        print(file=f)


seqA="peter piper picked a peck of pickled peppers"
seqB="a peck of pickled peppers peter piper picked"
dp = dotplot(seqA,seqB,5,4)
print(dotplotASCII(dp,seqA,seqB,"My first dotplot","first-dotplot.txt"))
plt.imshow(dp)
plt.show()
def dotplot2Grahics(dp,hdA,hdB):
    x=[]
    y=[]
    a=[]
    b=[]
    c=[]
    seqA="peter piper picked a peck of pickled peppers"
    seqB="a peck of pickled peppers peter piper picked"
    dp = dotplot(seqA,seqB,5,4)
    for i in seqA:
        a.append(i)
    for i in seqB:
        b.append(i)
    for i in range(0,len(seqA)+1):
        c.append(i)
    print(c)
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if dp[i][j]==1:
                x.append(j)
                y.append(i)
    plt.scatter(x,y)
    plt.title("scatter plot")
    plt.xlabel(hdA)
    plt.ylabel(hdB)
    plt.axis([0,len(seqA), len(seqB),0])
    plt.xticks(c,a)
    plt.yticks(c,b)
    plt.show()
print(dotplot2Grahics(dp,seqA,seqB))