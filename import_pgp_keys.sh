# file: import_pgp_keys.sh
# functie: import public en private pgp keys
# doc: https://access.redhat.com/solutions/2115511

# import de secret private key
gpg --import private_key.asc

# import de public key
gpg --import public_key.asc

# list public keys
gpg -k

# list de secret private keys
gpg -K
