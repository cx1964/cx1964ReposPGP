rem Filenaam: project_pgp_python3.win.cmd
rem Functie: script voor het starten van het project pgp
rem Opmerking: 
rem            copy deze file naam ~/bin
rem
rem            start dit script mbv:
rem            source project_pgp_python3.win.cmd

cd \
set HomeDir="C:\sources\sources-prive-experiment\cx1964ReposPGPpublic"
cd %HomeDir%
echo %HomeDir%

rem activate python env
.\env_python3_pgp\Scripts\activate.bat