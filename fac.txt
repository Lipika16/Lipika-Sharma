def fact(n):
    """
    Calculates the factorial of positive integers
    >>> print(fact(3))
    6
    >>> print(fact(5))
    120
    """
    assert (n >= 0), 'Please enter positive interger'
    result = 1
    for i in range(n):
        result = result*(i+1)
    return result

def main():
    print(fact(4))
    
if __name__ == "__main__":
   import doctest
   doctest.testmod()
   main()




