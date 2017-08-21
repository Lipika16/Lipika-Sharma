seq=input("Enter the sequence of the DNA : ")
print(seq.replace("T","U"))

#Enter the sequence of the DNA : ATCGGTTCCAT
#AUCGGUUCCAU
#Enter the sequence of the DNA : ATGCT
#AUGCU
#Enter the sequence of the DNA : GTCATGCA
#GUCAUGCA
#Enter the sequence of the DNA : TGTTCTTA
#UGUUCUUA
#Enter the sequence of the DNA : GTTAACGTTC
#GUUAACGUUC



word=input("Enter the word to check whether it is a palindrome or not : ")
def palindrome(word):
    word=word.upper()
    word=''.join(filter(str.isalpha, word))
    pal_char = word[::-1]
    print(pal_char)
    if pal_char== word:
        print("True. This is a palindorme")
    else: 
        print("False. This is NOT a palindrome")

palindrome(word)



#Enter the word to check whether it is a palindrome or not : Doc, note: I dissent. A fast never prevents a fatness. I diet on cod. 
#DOCNOTEIDISSENTAFASTNEVERPREVENTSAFATNESSIDIETONCOD
#True. This is a palindrome

#Enter the word to check whether it is a palindrome or not : "All the best!"
#"!TSEBEHTLLA"
#False. This is NOT a palindrome

#Enter the word to check whether it is a palindrome or not : A Man, A Plan, A Canal-Panama! 
#AMANAPLANACANALPANAMA
#True. This is a palindrome

#Enter the word to check whether it is a palindrome or not : This is not my cup of tea !
#AETFOPUCYMTONSISIHT
#False. This is NOT a palindrome

#Enter the word to check whether it is a palindrome or not : A Santa Lived As a Devil At NASA
#ASANTALIVEDASADEVILATNASA
#True. This is a palindrome






valid_year = None
valid_month = None
valid_day = None
leap_year = False

year=int(input("Enter the year : "))
def is_leap_year(year):
    if year%4 == 0:
        return ("True. This is a leap year")
    else:
        return ("False. This is not a leap year")
print(is_leap_year(year))



def is_valid_date(day,month,year):
    if ( (year >= 1) & (year <= 9999) ):
        valid_year = True
    else:
        valid_year = False
    if ( (month > 0) & (month < 13)):
        valid_month = True
    else:
        valid_month = False
    if( leap_year ):
        if( (month == 2) & ( (day <= 0 ) | (day > 29) ) ):
            valid_day = False
        elif( 
             ((month == 4) | (month == 6) | (month == 9) | (month == 11)) &
             ( (day <= 0) | (day > 30))
            ):
            valid_day = False
        elif( 
             ((month == 1) | (month == 3) | (month == 5) | (month == 7) | (month == 8) | (month == 10) | (month == 12)) &
             ( (day <= 0) | (day > 31))
            ):
            valid_day = False
        else:
            valid_day = True
    else:
        if( (month == 2) & ( (day <= 0 ) | (day > 28) ) ):
            valid_day = False
        elif( 
             ((month == 4) | (month == 6) | (month == 9) | (month == 11)) &
             ( (day <= 0) | (day > 30))
            ):
            valid_day = False
        elif( 
             ((month == 1) | (month == 3) | (month == 5) | (month == 7) | (month == 8) | (month == 10) | (month == 12)) &
             ( (day <= 0) | (day > 31))
            ):
            valid_day = False
        else:
            valid_day = True
    if( valid_year & valid_month & valid_day ):
        return True
    else:
        return False

print("Enter Date: ")
date = input()

date_parts = date.split('.')

day = int(date_parts[0])
month = int(date_parts[1])
year = int(date_parts[2])

print(is_valid_date(day, month, year))

#Enter the year : 2016
#True. This is a leap year
#Enter Date: 
#31.4.2016
#False

#Enter the year : 2005
#False. This is not a leap year
#Enter Date: 
#29.02.2005
#False

#Enter the year : 2007
#False. This is not a leap year
#Enter Date: 
#1.13.2017
#False

#Enter the year : 2004
#True. This is a leap year
#Enter Date: 
#0.5.2004
#False

#Enter the year : 2000
#True. This is a leap year
#Enter Date: 
#29.2.2000
#False

#Enter the year : 2016
#True. This is a leap year
#Enter Date: 
#1.0.2016
#False

#Enter the year : 1999
#False. This is not a leap year
#Enter Date: 
#31.12.1999
#True

#Enter the year : 1900
#True. This is a leap year
#Enter Date: 
#29.2.1900
#False

#Enter the year : 2004
#True. This is a leap year
#Enter Date: 
#20.2.2004
#True

#Enter the year : 0
#True. This is a leap year
#Enter Date: 
#1.1.0
#False