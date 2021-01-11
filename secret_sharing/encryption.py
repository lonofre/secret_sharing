from random import randint
    
def encrypt(s_filename, n, t, s_clearfile, pswd):
    ''' 
    -----Function under construction -----
    Returns: 

    * Encrypted file using AES.
    
    * File with n pairs (x, P(x)). 

    Params: 

    * s_filename, String. Name of the file where the n point will be stored.

    * n, Integer. n > 2. Total evaluations requiered.

    * t, integer. 1 < t <= n. Determines the polynomial degree. Number of terms.     
    * s_clearfile, String. Name of the file with the decrypted message.
    
    * pswd, String. Password typed by the user.
    '''

    

def get_terms(K, t):
    '''
    Generates a list with t Integers, elements of an t-1 degree polynomial. 

    Params: 
    
    * K, Integer. Encryption key.
    
    * t, Integer. Length of the terms list.

    Returns a list with t terms, where t[0] = K, every other element on the
    list it's a random int in [100, K].
    '''
    terms = [K]
    for i in range(t-1):
        terms.append(randint(100, K))
    return terms
    
def polynomial_value(terms, x):
    '''
    Returns Integer y, where y is the polynomial evaluated on x.
    Evaluates the t-1 polynomial degree. 
    y = K + x*term[1] + x^2*term[2] + ... + x^{t-1}*term[t]

    Params: 
    
    * terms, List. Polynomial representation.

    * x, Integer. Value of x on the polynomial.
    '''
    y = 0
    cont = 1
    for term in terms:
        y = y + (term * cont)
        cont = cont * x

    return y    

def get_points(n, terms):
    '''
    Returns a list with n points (x,y), 
           where x is an Integer generated randomly and
                 y is the evaluation of the polynomial represented on terms
                 on x.

    Params:
     
    * n, Integer. Length of the points list.
    
    * terms. Integer List. Representation of the t-1 polynomial degree.
    '''
    points = []
    for i in range(n):
        x = randint(10, n+10)
        y = polynom_value(terms, x)
        points.append((x, y))
    return points
