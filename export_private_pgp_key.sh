# file: export_private_pgp_key.sh
# functie: Export de private pgp key vanuit Ubuntu met het command
#          Laatst getest met ubuntu 20.04 20210130
gpg --export-secret-key -a > private_key.asc