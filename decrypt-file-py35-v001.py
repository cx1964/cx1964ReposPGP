# Filenaam:       decrypt-file-py35-v001.py
# Functie:        Decrypt een file met gpg obv de python library python-gnupg
#                 De encryppted file kan mbv een FileDialog geselecteerd worden.
# python versie:  > 3.7
# opmerking:      vanaf python3 3.7 geen module installeren voor tkinter
#
# Documentatie:   zie https://www.saltycrane.com/blog/2011/10/python-gnupg-gpg-example/  
#                     https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python

import os
import gnupg # Op ubuntu 20.04 installeer de package mbv pip install python-gnupg
             # Onder Windows10 geeft deze import de melding "No module named 'gnupg'"
             # Echter als men vanaf een terminal in Visual Code in Windows dit draait krijg je de melding niet 
from pprint import pprint
import tkinter as tk
from tkinter import filedialog

passphraseString ='test'

import platform
system = platform.system().lower()

# Bepaal OS
is_windows = system == 'windows'
is_linux = system == 'linux'
is_mac = system == 'darwin'

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
  print("InputFilenaName: "+fileAndPath)

# Bepaal afhankelijk van OS de gnuhome parameter
if is_linux:
  # onder Ubuntu werkt onderstaande:
  # Onder Linux gnupghome is het pad naar de directory ./gnupg/
  # Onder Linux mag gnupghome als ./gnupg/ op de default plek is geinstalleerd
  print("OS Linux")
  HomePATH = os.environ["HOME"]
  print("HomePATH", HomePATH)
  gnupgHOME = f"/{HomePATH}/.gnupg/"
elif is_windows:
  print("OS windows")
  # Onder Windows obv gpg4win versie 3.x
  # https://www.gpg4win.org/doc/en/gpg4win-compendium_28.html
  HomePATH = os.environ["APPDATA"]
  gnupgHOME = HomePATH+'\\'+'gnupg' #+'\\'
  print("gnupgHOME", gnupgHOME)

gpg = gnupg.GPG(gnupghome=gnupgHOME)


# decrypt selected file
with open(fileAndPath, 'rb') as encryptedFile:
  status = gpg.decrypt_file(  encryptedFile
                             ,passphrase=passphraseString
                             ,output='my-decrypted.txt')

if status.ok: 
  print ("Decrypted file: "+output)

print ('Return code: ', status.ok)
print ('Foutmelding: ', status.status)

print ("Klaar")  