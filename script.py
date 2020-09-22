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


@app.command(name='extract_one', help='extract all files within a directory with a given extension')
def extract(directory:str, destination:str, ext:str ):
    
    os.makedirs(destination, exist_ok=True)
    
    for cp,dir,files in os.walk(directory):
        
        for file in files:
            
            if cp == destination:
                continue
            
            if file.endswith(ext):
                print(f'Moving {file}')
                shutil.move(os.path.join(cp,file), os.path.join(destination,file))

ext = {}
ext['Video'] = ['.mpeg','.mp4','.avi','.mpg','.3gp','.webm', '.mov', '.mkv','.wmv', '.vob', '.ogg', '.ogv']
ext['Audio'] = [ '.mp3', '.wav', '.aac', '.wma', '.dss', '.dvf', '.m4p', '.midi']
ext['Pictures'] = ['.jpg', '.jpeg', '.png', '.jfif', '.exif', '.tiff', '.gif', '.gif', '.bmp', '.ppm', '.pgm', '.pbm', '.pnm', '.webp', '.heif', '.img', '.ico']

def matches_type(f, types):
    for i in ext[types]:
        if(f.lower().endswith(i)):
            return True
    return False

def ends(f,type):
    return f.lower().endswith(type)

@app.command(name='extract',help='extracts all [file_types] (Videos,Audio,Pictures) in [Source Folder] to [Destination Folder]')
def extract_videos(types:str, source:str, dest_folder:str):
    
    os.makedirs('../'+dest_folder,exist_ok=True)
    for cp,dir,files in os.walk(source):
        for f in files:
            if matches_type(f,types):
                os.makedirs(path.join('../'+dest_folder,cp[2:]),exist_ok=True)
                shutil.move(path.join(cp,f),path.join('../'+dest_folder,cp[2:]))
        if len(os.listdir(cp) ) == 0:
            os.rmdir(cp)

@app.command(name='enumerate',help='extracts all [file_types] (Videos,Audio,Pictures) in [Source Folder] to [Destination Folder]')
def extract_videos(types:str, source:str, dest_folder:str):
    
    os.makedirs('../'+dest_folder,exist_ok=True)
    index = 0
    for cp,dir,files in os.walk(source):
        for f in files:
            if ends(f,types):
                os.makedirs(path.join('../'+dest_folder,cp[2:]),exist_ok=True)
                shutil.move(path.join(cp,f),path.join('../'+dest_folder,str(index)+'.jpg'))
                index+=1
        # if len(os.listdir(cp) ) == 0:
        #     os.rmdir(cp)
    # for cp,dir,files in os.walk(dest_folder):
    #     index = 0
    #     for f in
# extract_videos(source_folder,dest_folder)                


if __name__ == '__main__':
    app()