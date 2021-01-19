from Cryptodome.Cipher import AES
from .lagrange import Lagrange

# Prime number to use a module
prime = 208351617316091241234326746312124448251235562226470491514186331217050270460481

def decrypt(file, points):
    ''' Decrypt a file given a set of points
    
    Parameters
    ----------
    file: bytes
        The file to decrypt
    points:
        A set of points (x,y) used as a key

    Returns
    -------
    bytes
        the file decrypted
    '''
    try:
        lagrange = Lagrange(prime)
        int_key = lagrange.interpolation(0, points)
    except ArithmeticError as err:
        raise
    
    key = int_key.to_bytes(32, byteorder='big')
    nonce = file[:AES.block_size]
    tag = file[AES.block_size: AES.block_size * 2]
    body = file[AES.block_size * 2:]
    
    try:
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        decrypted_file = cipher.decrypt(body)
    except Exception as err:
        raise

    return decrypted_file
