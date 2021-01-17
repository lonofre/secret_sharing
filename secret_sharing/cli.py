import click

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
@click.argument('points_file', type=click.File('r'))
@click.argument('filename', type=click.File('rb'))
def decrypt_file(points_file, filename):
    ''' Decrypt a file given a list of points'''

    encrypted_file = filename.read()
    points = points_file.read(1024)

