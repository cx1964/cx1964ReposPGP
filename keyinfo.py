# file: keyinfo.py
# functie: verweken van keyinfo


# Onder Windows wordt win4gpg gebruikt als officiele
# zie documentatie https://www.gpg4win.org/features.html
# Vraag is hoe wordt dit geinstalleerd
# waar worden de configfile en de keys die met het programma zijn aangemaakt opgeslagen.
# is dat zoals nu in dit script wordt gebruikt   gnupgHOME = "C:\\Users\\fontacx\\.gnupg\\" ????

# Er is nu geinstalleerd winGPG 1.0.1 en geen win4gpg !!!
# uitzoeken hoe win4gpg downloaden en installeren
# Zie https://en.wikipedia.org/wiki/Gpg4win



import os
import gnupg # Op ubuntu 20.04 installeer de package mbv pip install python-gnupg
             # Onder Windows10 geeft deze import de melding "No module named 'gnupg'"
             # Echter als men vanaf een terminal in Visual Code in Windows dit draait krijg je de melding niet 
from pprint import pprint
# from encrypt_py35 import PASSPHRASE

import platform
system = platform.system().lower()

# Bepaal OS
is_windows = system == 'windows'
is_linux = system == 'linux'
is_mac = system == 'darwin'


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
  gnupgHOME = HomePATH+'\\'+'gnupg'+'\\'
  print("gnupgHOME", gnupgHOME)

# ToDo
# debug:
# Onder windows C:\Users\fontacx\.gnupg bevat de files pubring.kbx en is dit onder Linux ook zo ???
# Onder Windows werkt nog niet van command line




gpg = gnupg.GPG(gnupghome=gnupgHOME)

public_keys = gpg.list_keys()
private_keys = gpg.list_keys(True)
aantalPrivateKeys= len([private_keys])
aantalPublicKeys= len([public_keys])

# Print key info
print("\n")
print("Aantal private_keys:", aantalPrivateKeys)
print("Aantal public_keys:" , aantalPublicKeys)
print("\n")

# debug
print("\nHet script werkt onder Windows goed tot hier !!!")
print("Indien script vanuit Visual code wordt gedraait en de python interpreter is ingesteld op env_python3_pgp") 

print("\n")
print("private_keys[0]['keyid']:" ,private_keys[0]['keyid'] )
print("private_keys[0]['type']:"  ,private_keys[0]['type'] )
print("private_keys[0]['trust']:" ,private_keys[0]['trust'] )
print("private_keys[0]['length']:",private_keys[0]['length'] )
print("private_keys[0]['uids']:"  ,private_keys[0]['uids'] )
print("\n")
print("public_keys[0]['keyid']:" ,public_keys[0]['keyid'] )
print("public_keys[0]['type']:"  ,public_keys[0]['type'] )
print("public_keys[0]['trust']:" ,public_keys[0]['trust'] )
print("public_keys[0]['length']:",public_keys[0]['length'] )
print("public_keys[0]['uids']:"  ,public_keys[0]['uids'])

print("type(private_keys)", type(private_keys) )


#print("aantal keys in dict private_keys", private_keys.key )
#for e in private_keys:
#    print("element: ", e)