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

# https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python
# vanaf python3 3.7 geen module installeren voor tkinter
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
# Get current directory
initDir = os.getcwd()
print("current directory:",initDir)
fileTypes = [
             ("Gpg Files", "*.gpg", "TEXT"),
             ("All Files", "*")]
# show Open File Dialog             
fileAndPath = filedialog.askopenfilename( title='Select encrypted file'
                                         ,initialdir=initDir
                                         ,filetypes=fileTypes)
if not fileAndPath:
  print("Niets geselecteerd")  
  exit()
else:                                          
  print("InputFilenaName: "+file_path)

# hier code tbv decrypt de inputfile
