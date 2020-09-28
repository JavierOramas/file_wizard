import os
import shutil
from typer import Typer
from collections import defaultdict
import hashlib
import sys

app = Typer()

def chunk_reader(fobj, chunk_size=1024):
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

def get_hash(filename, first_chunk_only=False, hash=hashlib.sha1):

    hash_obj = hash()
    file_object = open(filename, 'rb')

    if first_chunk_only:
        hash_obj.update(file_object.read(1024))
    else:
        for chunk in chunk_reader(file_object):
            hash_obj.update(chunk)

    hashed = hash_obj.digest()
    file_object.close()

    return hashed

@app.command(name='duplicates', help='Find and remove all duplicate files in a folder')
def duplicates(directory:str, hash=hashlib.sha1):
    hashes_by_size = defaultdict(list)
    hashes_on_1k = defaultdict(list)
    hashes_full = {} 
    
    for cp,dir,files in os.walk(directory):
        for file in files:
            full_path = os.path.join(cp,file)
            try:
                #if the path is a link (softpath) this will take teh reak path
                full_path = os.path.realpath(full_path)
                file_size = os.path.getsize(full_path)
                hashes_by_size[file_size].append(full_path)
            except (OSError, ):
                continue
    for size_in_bytes, files in hashes_by_size.items():
        if len(files) < 2:
            continue
        
        for file in files:
            try:
                small_hash = get_hash(file, first_chunk_only=True)
                hashes_on_1k[(small_hash, size_in_bytes)].append(file)
            except (OSError, ):
                continue
        
        for __, files_list in hashes_on_1k.items():
            
            if len(files_list) < 2:
                continue

            for file in files_list:
                try:
                    full_hash = get_hash(file, first_chunk_only=False)
                    duplicate = hashes_full.get(full_hash)
                    
                    if duplicate:
                        print('Duplicate Found: (1) {} and (2) {}'.format(file, duplicate))
                        option = input('Select what to do with them (0,1,2): ') 
                        if option == '1':
                            os.remove(file)
                        elif option == '2':
                            os.remove(duplicate)
                            
                    else:
                        hashes_full[full_hash] = file
                except (OSError, ):
                    continue
            

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