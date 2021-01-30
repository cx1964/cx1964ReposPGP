# file: export_secret_pgp_key.sh
# functie: Export de secret pgp key vanuit Ubuntu met het command
#          Laatst getest met ubuntu 20.04 20210130
gpg --export-secret-key -a > s.asc