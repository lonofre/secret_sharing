from .encryption import encrypt
from getpass import getpass
import re
import click
import csv

@click.group()
def sharing():
    pass

@sharing.command(name='c')
@click.argument('total_points', nargs=1)
@click.argument('min_points', nargs=1)
@click.argument('filename', type=click.File('rb'))

def encrypt_file(total_points, min_points, filename):
    '''Encrypts a file. Saves it's encryption and a file with 
    n = total_points points.
<<<<<<< HEAD
=======

>>>>>>> 42cc0651f89574f0e6c3edfaa8e0a804c1263ea1
    TOTAL_POINTS is the number of points will be evaluated.
    
    MIN_POINTS is the degree of the polynomial.
    
    FILENAME is File to encrypt.
    
    '''
    
    data  = filename.read()
    pswd = getpass()
    ciphertext, tag, nonce, points = encrypt(pswd, int(total_points),
                                             int(min_points), data)
    
    f_name = re.sub(r'\.sss$', '', filename.name)
    
    file_out = open(f_name+".ss", "wb")
    [ file_out.write(x) for x in (nonce, tag, ciphertext) ]
    file_out.close()

    with open(f_name+".csv", "w") as csv_file:
        csv_file.write('\n'.join('%s, %s' % point for point in points))
