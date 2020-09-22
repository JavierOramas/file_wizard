import os
from typer import Typer

app = Typer()

@app.command(name='purge', help='Remove all files within a directory with a given extension')
def purge(directory:str, ext:str):
    
    for cp,dir,files in os.walk(directory):
        for file in files:
            print(file)
            if file.endswith(ext):
                os.remove(file)
if __name__ == '__main__':
    app()