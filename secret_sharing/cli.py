from .encryption import encrypt
from .decryption import decrypt
from getpass import getpass
import re
import click
import csv

@click.group()
def sharing():
    pass


@sharing.command(name='d')
@click.argument('filename', type=click.File('rb'))
@click.argument('points_file', type=click.File('r'))
def decrypt_file(filename, points_file):
    ''' Decrypt a file given a list of points
    
    FILENAME is the file with extension .ss that will be
    decrypted

    POINTS_FILE is the list of points given to decrypt
    '''
    if re.search(r'\.ss$', filename.name):
        encrypted_file = filename.read()
        reader = csv.reader(points_file)
        points = [tuple(map(int, row)) for row in reader]
        try:
            decrypted_file = decrypt(encrypted_file, points) 
            new_name = re.sub(r'\.ss$', '', filename.name)
            with open(new_name, 'wb') as f:
                f.write(decrypted_file)
        except ValueError as err:
            pass
        except ZeroDivisionError as err:
            click.echo(f'Error: The  points need to be different')
        except ArithmeticError as err:
            click.echo(f'Error: Wroing points {points}, they are not integers ')
    else:
        click.echo(f'Error: Invalid file extension, it needs to end with .ss')


@sharing.command(name='c')
@click.argument('total_points', nargs=1)
@click.argument('min_points', nargs=1)
@click.argument('filename', type=click.File('rb'))
def encrypt_file(total_points, min_points, filename):
    '''
    Encrypts a file. Saves it's encryption and a file with 
    n = total_points points.
    
    Parameters
    -----------
    TOTAL_POINTS is the number of points will be evaluated.
    
    MIN_POINTS is the degree of the polynomial.
    
    FILENAME is File to encrypt.
    
    '''
    
    data  = filename.read()
    pswd = getpass()
    ciphertext, tag, nonce, points = encrypt(pswd, int(total_points),
                                             int(min_points), data)
    
    f_name = re.sub(r'\.ss$', '', filename.name)
    
    file_out = open(f_name+".ss", "wb")
    [ file_out.write(x) for x in (nonce, tag, ciphertext) ]
    file_out.close()
    
    with open(f_name+".csv", "w") as csv_file:
        csv_file.write('\n'.join('%s, %s' % point for point in points))
