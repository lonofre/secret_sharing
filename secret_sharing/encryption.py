from random import randint
from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA256

prime = 208351617316091241234326746312124448251235562226470491514186331217050270460481

def encrypt(pswd, n, t, data):
    ''' 
    
    Returns
    --------
    bytes
         the file encripted.
    
    * File with n pairs (x, P(x)). 
    Parameters 
    ----------
    * pswd, String, password typed by the user.
    * n, Integer. n > 2. Total evaluations requiered.
    * t, integer. 1 < t <= n. Determines the polynomial degree(Number of terms).
    * data, String. Data to encrypt.
    
    '''
    key = SHA256.new(pswd.encode('utf8'))
    bytes_key = key.digest()
    int_key = int.from_bytes(bytes_key, "big")
    terms = get_terms(int_key, t)
    points = get_points(n, terms)
    cipher = AES.new(bytes_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    return ciphertext, tag, cipher.nonce, points

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
        terms.append(randint(100000000000000000000000000000000000000000000000000000000000000000000000000000,1000000000000000000000000000000000000000000000000000000000000000000000000000000)%prime)
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
    Returns 
    -------
    * List with n points (x,y), 
           where x is in [1, n] and
                 y is the evaluation of the polynomial represented on terms
                 on i.
    Parameters
    ----------
    * n, Integer. Length of the points list.
    
    * terms. Integer List. Representation of the t-1 polynomial degree.
    '''
    points = []
    for i in range(n):
        y = polynomial_value(terms, i+1)
        points.append((i+1, y))
    return points
