from encryption import encrypt
from getpass import getpass
import re
import click
import csv
from decryption import decrypt

@click.group()
def sharing():
    pass

@sharing.command(name='c')
@click.argument('total_points', nargs=1)
@click.argument('min_points', nargs=1)
@click.argument('filename', type=click.File('rb'))

def encrypt_file(total_points, min_points, filename):
    '''
     
    Encrypts a file. Saves it's encryption and a file with 
    n = total_points points.

    Parameters
    ----------
    total_points
                Number of points will be evaluated.
    
    min_points
              Degree of the polynomial.
    
    filename
            File to encrypt.
    
    '''
    
    data  = filename.read()
    pswd = getpass()
    ciphertext, tag, nonce, points = encrypt(pswd, int(total_points),
                                             int(min_points), data)
    
    f_name = re.sub(r'\.sss$', '', filename.name).split(sep =".")
    
    file_out = open(f_name[0]+".ss", "wb")
    [ file_out.write(x) for x in (nonce, tag, ciphertext) ]
    file_out.close()

    with open(f_name[0]+".csv", "w") as csv_file:
        csv_file.write('\n'.join('%s, %s' % point for point in points))
