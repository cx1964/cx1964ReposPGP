# filename: 100_install_libs_cx1964ReposPGPpublic.sh
# functie:  install libraries tbv plot

export HomeDir="/home/test01/Documents/sources/pgp/cx1964ReposPGPpublic"
#export HomeDir="/c/sources/sources-prive-experiment/cx1964ReposPlot"
cd $HomeDir
echo $HomeDir

# maak virtuele python environment voor python libraries
# Uitvoeren in linux shell of in mingw64 shell op een Windows machine
python3 -m venv env_python3_pgp

# Activeren virtuele env tbv Windows machine met mingw64
#source /$HomeDir/env_python3_plot/Scripts/activate
# Activeren virtuele env tbv Linux shell 
source ./env_python3_pgp/bin/activate

# upgrade pip uitvoeren in Linux shell of Windows machine met mingw64
python -m pip install --upgrade pip

# importeer alle benodigde libraries
pip install python-gnupg

# toon geinstalleerde python libraries
pip list