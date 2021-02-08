# Filenaam:       encrypt_file_py35_v001.py
# Functie:        Encrypt een file met gpg obv de python library python-gnupg
# python versie:  3.x
#
# Opmerking:      Onder Ubuntu 20.04 installeer python3 library python-gnupg
#                 zie https://pypi.org/project/python-gnupg/
#                  
# Uitgangspunt:   Om dit script te laten werken moet gpg zijn geinstalleerd
#                 en de public en private keys aanwezig zijn.

# Voorbeeld code zie:
# https://stackoverflow.com/questions/19298171/python-gnupg-encrypt-no-errors-but-not-encrypting-data-or-files
# http://pythonhosted.org/gnupg/gnupg.html
# http://pythonhosted.org/python-gnupg/
# https://www.saltycrane.com/blog/2011/10/python-gnupg-gpg-example/

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



# zie https://www.saltycrane.com/blog/2011/10/python-gnupg-gpg-example/
# Toon gpg informatie van het platform
# letop de module python-gnupg is een wraper 
# Zie: https://pythonhosted.org/python-gnupg/
# tbv windows
# maar werkt niet
# gpg = gnupg.GPG(gpgbinary='C:\Program Files\WinGPG\x64')


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
  gnupgHOME = "C:\\Users\\fontacx\\.gnupg\\"
  print("gnupgHOME", gnupgHOME)

gpg = gnupg.GPG(gnupghome=gnupgHOME)

public_keys = gpg.list_keys()
private_keys = gpg.list_keys(True)

print ('public keys:')
pprint(public_keys)
print ('private keys:')
pprint(private_keys)
print ('\n\n')



my_un_encrypted_file = 'my-unencrypted.txt'
my_encrypted_file = my_un_encrypted_file+'.gpg'

# Maak een dummy file my-unencrypted.txt aan met test data om te encrypten
open('my-unencrypted.txt', 'w').write('Dit is test data voor de file.')


# Encrypt de file
afile=open(my_un_encrypted_file, 'rb')
# inlezen van de ID van private key
rkeys = input("Enter key ID from private key: ") 
status = gpg.encrypt_file( afile
                          ,rkeys.split()
                          ,always_trust=True
                          ,output=my_encrypted_file)
    
print ('ok: ', status.ok)
print ('status: ', status.status)
print ('stderr: ', status.stderr)


print ("Klaar")
print ("Unencrypyted file: "+my_un_encrypted_file )
print ("Encrypted file: "+my_encrypted_file )
