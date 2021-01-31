# filename: install_pgp.sh
# functie : install gnuPGP packages for ubuntu 20.04

sudo apt-get install gnupg2

# install seahorse
# SeaHorse is a graphical application for managing GPG keys and encryption on GNOME 3 desktop environment. 
sudo sudo apt-get install seahorse

# install SeaHorse Nautilus File Manager plugin
sudo apt-get install seahorse-nautilus

# install SeaHorse Nemo File Manager plugin for Cinnamon filemanager Nemo
# voor geval cinnamon is geinstalleerd
#sudo add-apt-repository ppa:wasta-linux/cinnamon-testing
#sudo apt-get update
#sudo apt-get install nemo-seahorse

# toDo
4. python script testen of werkt