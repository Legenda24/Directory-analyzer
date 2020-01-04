__author__ = 'legendax24'
__version__ = '1.0.0'

# TODO analyze subdirectories
import os
from hurry.filesize import size, alternative
from tkinter import filedialog, Label
from tkinter import ttk
from ttkthemes import ThemedTk

win = ThemedTk(theme="clearlooks")
win.geometry('400x150')
win.title('Legendax24')

directory = None


def get_dir():
    global directory
    directory = filedialog.askdirectory()
    if not directory.endswith('\\'):
        directory += '\\'
    else:
        pass


def analyze_dir():
    global directory
    global max_filesize, min_filesize
    global max_size_filename, min_size_filename

    if not directory:  # When directory was't chosen
        set_label_error1()
    else:
        # creating absolute path to every file of directory
        dir_files = next(os.walk(directory))[2]
        dir_files = [directory + i for i in dir_files]

        # creating dict with directory's files and their sizes
        files_info = {}
        for file in dir_files:
            filesize = os.path.getsize(file)
            filename = os.path.basename(file)
            files_info[filesize] = filename

        try:
            # setting max and min file info
            max_filesize = max(files_info.keys())  # size of file in bytes
            max_size_filename = files_info[max_filesize]  # name of max size file

            min_filesize = min(files_info.keys())
            min_size_filename = files_info[min_filesize]

            convert_sizes(max_filesize, min_filesize)
            max_file_label['text'] = f'Biggest file of directory: {max_size_filename} - {max_filesize}'
            max_file_label.pack()

            min_file_label['text'] = f'Smallest file of directory: {min_size_filename} - {min_filesize}'
            min_file_label.pack()
        except Exception:  # When directory has no files
            set_label_error2()


def convert_sizes(max_size, min_size):
    global max_filesize, min_filesize
    max_filesize = size(max_size, system=alternative)
    min_filesize = size(min_size, system=alternative)


def set_label_error1():  # When directory was't chosen
    global max_file_label
    max_file_label['text'] = 'Chose directory for first.'
    max_file_label.pack()


def set_label_error2():
    global max_file_label, min_file_label
    max_file_label['text'] = 'Directory has no files.'
    min_file_label['text'] = ''

    max_file_label.pack()
    min_file_label.pack()


get_directory = ttk.Button(win, text='Choose directory', command=get_dir).pack()
analyze_directory = ttk.Button(win, text='Analyze', command=analyze_dir).pack()
max_file_label = Label(win)
min_file_label = Label(win)
win.mainloop()
