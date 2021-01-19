import click
import csv
import re
from .decryption import decrypt

@click.group()
def sharing():
    pass

@sharing.command(name='c')
@click.argument('points_output', nargs=1)
@click.argument('total_points', nargs=1)
@click.argument('min_points', nargs=1)
@click.argument('filename', type=click.File('rb'))
def encrypt_file(points_output, total_points, min_points, filename):
    ''' Encrypt a file '''

    text = file.read()
    if text:
        print(text)    

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

