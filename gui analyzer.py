__author__ = 'legendax24'
__version__ = '1.0.0'

# TODO analyze subdirectories
import os
from hurry.filesize import size, alternative
from tkinter import filedialog, Label
from tkinter import ttk
from ttkthemes import ThemedTk


class Window():

    def __init__(self):
        self.win = ThemedTk(theme="clearlooks")
        self.win.geometry('400x150')
        self.win.title('Legendax24')

        self.dir = None  # for line 28

    def get_dir(self):
        self.dir = filedialog.askdirectory()
        if not self.dir.endswith('\\'):
            self.dir += '\\'
        else:
            pass

    def analyze_dir(self):
        if not self.dir:  # When directory was't chosen
            self.set_label_error1()
        else:
            # creating absolute path to every file of dir
            self.dir_files = next(os.walk(self.dir))[2]
            self.dir_files = [self.dir + i for i in self.dir_files]

            # creating dict with dir's files and their sizes
            self.files_info = {}
            for file in self.dir_files:
                self.filesize = os.path.getsize(file)
                self.filename = os.path.basename(file)
                self.files_info[self.filesize] = self.filename

            try:
                # setting max and min file info
                self.max_filesize = max(self.files_info.keys())  # size of file in bytes
                self.max_size_filename = self.files_info[self.max_filesize]

                self.min_filesize = min(self.files_info.keys())
                self.min_size_filename = self.files_info[self.min_filesize]
                self.set_label_fileinfo()
            except ValueError:  # When directory has no files
                self.set_label_error2()

    def convert_sizes(self):
        self.max_filesize = size(self.max_filesize, system=alternative)
        self.min_filesize = size(self.min_filesize, system=alternative)

    def set_label_fileinfo(self):
        self.convert_sizes()
        self.max_file_label['text'] = f'Biggest file of directory: {self.max_size_filename} - {self.max_filesize}'
        self.max_file_label.pack()

        self.min_file_label['text'] = f'Smallest file of directory: {self.min_size_filename} - {self.min_filesize}'
        self.min_file_label.pack()

    def set_label_error1(self):  # When directory was't chosen
        self.max_file_label['text'] = 'Chose directory for first.'
        self.max_file_label.pack()

    def set_label_error2(self):  # When directory has no files
        self.max_file_label['text'] = 'Directory has no files.'
        self.min_file_label['text'] = ''

        self.max_file_label.pack()
        self.min_file_label.pack()

    def widgets(self):
        ttk.Button(self.win, text='Choose directory', command=self.get_dir).pack()
        ttk.Button(self.win, text='Analyze', command=self.analyze_dir).pack()

        self.max_file_label = Label(self.win)
        self.min_file_label = Label(self.win)

    def run(self):
        self.widgets()
        self.win.mainloop()


window = Window()
window.run()
