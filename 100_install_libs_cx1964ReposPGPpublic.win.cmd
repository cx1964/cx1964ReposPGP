rem filename: 100_install_libs_cx1964ReposPGPpublic.win.cmd
rem functie:  install libraries tbv PgP in windows

cd \
set HomeDir="C:\sources\sources-prive-experiment\cx1964ReposPlot"
cd %HomeDir%
echo %HomeDir%

rem maak virtuele python environment voor python libraries
python3 -m venv env_python3_pgp

rem activate python env
.\env_python3_pgp\Scripts\activate.bat

rem upgrade pip
python3 -m pip install -U pip

rem importeer alle benodigde libraries
pip install python-gnupg

rem toon geinstalleerde python libraries
pip list
