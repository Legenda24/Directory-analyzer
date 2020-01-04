__author__ = 'legendax24'
__version__ = '1.0.0'

# TODO analyze subdirectories
import os
from hurry.filesize import size, alternative

while True:
    directory = str(input('Enter directory: '))
    if ':' not in directory or directory == None:
        continue
    else:
        directory += '\\'
        break

dir_files = next(os.walk(directory))[2]
dir_files = [directory + i for i in dir_files]

files_info = {}
for file in dir_files:
    filesize = os.path.getsize(file)
    filename = os.path.basename(file)
    files_info[filesize] = filename

try:
    max_filesize = max(files_info.keys())  # size of file in bytes
    max_size = size(max_filesize, system=alternative)  # convert bytes to kb, mb and etc
    max_size_filename = files_info[max_filesize]

    min_filesize = min(files_info.keys())
    min_size = size(min_filesize, system=alternative)
    min_size_filename = files_info[min_filesize]

    print(f'Biggest file of directory: {max_size_filename} - {max_size}')
    print(f'Smallest file of directory: {min_size_filename} - {min_size}')
except Exception:
    print('Directory has no files')

input('Press ENTER to exit.')
