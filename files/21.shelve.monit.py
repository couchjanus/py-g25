# 21.shelve.monit.py
import os,hashlib
import shelve
import time

# Если file существует, а md5 не совпадает со значением files[file] (файл был изменен), оповещение будет активировано.

# md5 = hash.hexdigest()

# if file in files and md5 != files[file]:
#     print(f'{file} has been changed at {time.strftime("%Y-%m-%d %H:%M:%S")}!')
#     files[file]=md5

def walk(dir):
    files={}
    for file in [item for item in os.listdir(dir) if os.path.isfile(os.path.join(dir,item))]:
        hash = hashlib.md5()
        with open(os.path.join(dir,file), encoding='utf-8') as f:
            for chunk in iter(lambda: f.read(2048), ""):
                hash.update(chunk.encode('utf-8').strip())
        md5 = hash.hexdigest()
                
        if file in files and md5 != files[file]:
            print(f'{file} has been changed at {time.strftime("%Y-%m-%d %H:%M:%S")}!')
        files[file]=md5
    
    return files

files = walk(os.getcwd()+'/test/')

FILENAME = "repohash"

for k, v in files.items():
    with shelve.open(FILENAME) as repo:
        repo[k] = v

with shelve.open(FILENAME) as repo:
    for f in repo.keys():
        print(f)       
    print()
    for h in repo.values():
        print(h) 
