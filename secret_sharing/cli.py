import click

@click.group()
def sharing():
    pass

@sharing.command(name='c')
@click.argument('points_output', nargs=1)
@click.argument('total_points', nargs=1)
@click.argument('min_points', nargs=1)
@click.argument('file', type=click.File('r'))
def encrypt_file(points_output, total_points, min_points, file):
    text = file.read(1024)
    if text:
        print(text)    

@sharing.command(name='d')
@click.argument('points_input', type=click.File('r'))
@click.argument('file', type=click.File('r'))
def decrypt_file(points_input, file):
    encrypted_text = file.read(1024)
    points_file = points_input.read(1024)
