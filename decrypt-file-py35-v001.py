# Filenaam:       decrypt-file-py35-v001.py
# Functie:        decrypt een file met gpg obv de python library python-gnupg
# python versie:  3.x
# Documentatie:   zie https://www.saltycrane.com/blog/2011/10/python-gnupg-gpg-example/  

import os
import gnupg # Op ubuntu 20.04 installeer de package mbv pip install python-gnupg
             # Onder Windows10 geeft deze import de melding "No module named 'gnupg'"
             # Echter als men vanaf een terminal in Visual Code in Windows dit draait krijg je de melding niet 
from pprint import pprint
# from encrypt_py35 import PASSPHRASE

# ToDo
# afmaken
filetypes = [
             ("Gpg Files", "*.gpg", "BINARY"),
             ("All Files", "*")]

# show Open File Dialog

# https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
            # tkinter.filedialog.askopenfilename()
print("InputFilenaName: "+file_path)

#opendialog = tkinter.filedialog.Open(parent=master, filetypes=self.filetypes)
#base="bla.gpg"
# Get current directory
#dir = os.getcwd()
#fileName = opendialog.show(initialdir=dir, initialfile=self.base)



# hier code tbv decrypt de inputfile
