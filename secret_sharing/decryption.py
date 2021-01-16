from Cryptodome.Cipher import AES
from .lagrange import Lagrange

# Prime number to use a module
prime = 208351617316091241234326746312124448251235562226470491514186331217050270460481

def decrypt(file, points):
    ''' Decrypt a file given a set of points '''

    lagrange = Lagrange(prime)
    int_key = lagrange.interpolation(0, points)
    
    key = int_key.to_bytes(32, byteorder='big')
    nonce = file[:AES.block_size]
    body = file[AES.block_size:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_file = cipher.decrypt(body)

    return decrypted_file
