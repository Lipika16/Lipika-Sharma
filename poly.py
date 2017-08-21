dna_to_complementary_replace = {"A":"T", "C":"G", "G":"C", "T":"A"}
def dna_to_complementary(s):
    r = ""
    for i in s:
        try:
            if i in dna_to_complementary_replace:
                r += dna_to_complementary_replace[i]
            else:
                raise "Error"  
        except TypeError:
            return ("Error")  
    return r

def DNA(s):
    print("'{}' returns output '{}'".format(s, dna_to_complementary(s.upper())))

DNA("aCgGcAcaTt")

#ACGTGAC' returns output 'TGCACTG'
#'aATcgaT' returns output 'TTAGCTA'
#'gtcha12' returns output 'Error'
#'acagataf12' returns output 'Error'
#'aCgGcAcaTt' returns output 'TGCCGTGTAA'

s1 = [float(x) for x in input("Enter poly 1 : ").split()]
s2 = [float(x) for x in input("Enter poly 1 : ").split()]
print(list(s1))
print(list(s2))
res = [0]*(len(s1)+len(s2)-1)
for o1,i1 in enumerate(s1):
    for o2,i2 in enumerate(s2):
        res[o1+o2] += i1*i2
print(res)

# Enter poly 1 : 3 4 5
# Enter poly 1 : 9 6 7
# [3.0, 4.0, 5.0]
# [9.0, 6.0, 7.0]
# [27.0, 54.0, 90.0, 58.0, 35.0]

# Enter poly 1 : 0.1 3 6
# Enter poly 1 : 6.3 7.8 3
# [0.1, 3.0, 6.0]
# [6.3, 7.8, 3.0]
# [0.63, 19.68, 61.5, 55.8, 18.0]

# Enter poly 1 : 2 33 4
# Enter poly 1 : 33 6
# [2.0, 33.0, 4.0]
# [33.0, 6.0]
# [66.0, 1101.0, 330.0, 24.0]

# Enter poly 1 : 3.3 5
# Enter poly 1 : 2 4
# [3.3, 5.0]
# [2.0, 4.0]
# [6.6, 23.2, 20.0]

# Enter poly 1 : 9 5 2 4 5 5 6
# Enter poly 1 : 1 5 7 3 6 7 3
# [9.0, 5.0, 2.0, 4.0, 5.0, 5.0, 6.0]
# [1.0, 5.0, 7.0, 3.0, 6.0, 7.0, 3.0]
# [9.0, 50.0, 90.0, 76.0, 108.0, 157.0, 152.0, 133.0, 121.0, 95.0, 86.0, 57.0, 18.0]

a=input("Enter string 1: ")
b=input("Enter string 2: ")
a=a.upper()
b=b.upper()
a=''.join(filter(str.isalpha, a)) 
b=''.join(filter(str.isalpha, b)) 
if sorted(a) == sorted(b):
    print(True)
else:
    print(False)
    

# Enter string 1: School master
# Enter string 2: The classroom
# True

# Enter string 1: Punishments
# Enter string 2: Nine Thumps
# False

# Enter string 1: Mother-in-law
# Enter string 2: Hitler woman
# True

# Enter string 1: The earthquakes
# Enter string 2: The queer shakes
# False


# Enter string 1: Jim Morrison 
# Enter string 2: Mr. Mojo Risin
# True

