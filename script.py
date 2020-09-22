import os
import shutil
from typer import Typer

app = Typer()


@app.command(name='purge', help='Remove all files within a directory with a given extension')
def purge(directory:str, ext:str):
    
    for cp,dir,files in os.walk(directory):
        for file in files:
            if file.endswith(ext):
                print(f'Deleting {file}')
                os.remove(os.path.join(cp,file))


@app.command(name='extract', help='extract all files within a directory with a given extension')
def extract(directory:str, destination:str, ext:str ):
    
    os.makedirs(destination, exist_ok=True)
    
    for cp,dir,files in os.walk(directory):
        
        for file in files:
            
            if cp == destination:
                continue
            
            if file.endswith(ext):
                print(f'Moving {file}')
                shutil.move(os.path.join(cp,file), os.path.join(destination,file))


if __name__ == '__main__':
    app()