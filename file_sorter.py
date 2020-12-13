import os, shutil
from pathlib import Path
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# 1. get each file name by path.glob() and put it in a dict
# 2. use logger to log where the files are going this way we have a history
# 3. make new directories if not alredy made
# 4. move file to new directory 

path = Path('.')
files = {
    'exe':[],
    'pdf':[],
    'zip':[]
}

for file in files:
    files[file] = list(path.glob(f'*.{file}'))

    if files[file] != []:
        #check if directory exists
        p = Path('.' + f'/{file}')
        if p.exists() == False:
            os.mkdir(file) 
        for x in files[file]:
            logging.info('Moving file:' + str(x) + ' to: ' + str(p) + ' directory.')
            shutil.move(str(x), str(p))            
    else:
        logging.info('No ' + f'{file}' + ' files to be moved')


