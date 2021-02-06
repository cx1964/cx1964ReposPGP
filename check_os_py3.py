# file: check_os_pr3.py
# functie: check OS waarop het python3 script draait 
import platform
system = platform.system().lower()

# Bepaal OS
is_windows = system == 'windows'
is_linux = system == 'linux'
is_mac = system == 'darwin'

# Doe iets afhankelijk van het OS
if is_linux:
    print("Het draait op Linux")
elif is_windwos:
    print("Het is Windows") 
elif is_mac:
    print("Het is MacOS")
else:
    print("OS onbekend")           