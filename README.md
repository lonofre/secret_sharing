# Shamir's Secret Sharing 

A cryptographic algorithm that securely splits a secret into multiple parts (shares), requiring a minimum number (threshold) to reconstruct the original secret.

## Requirements

Python 3 is required to run the app and the following packages are needed:

* pycryptodomex
* click
* pytest

Also you can use [Poetry](https://python-poetry.org/) to install the dependencies.

## Usage

### Encryption
To encrypt is necessary to run:
```bash
python3 -m secret_sharing c [N] [T] [FILENAME]
```
Where:
* `[N]` is an integer that indicates the total points the program will create and store.
* `[T]` is an integer that indicates the minimum number of points required in order to decrypt the file.
* `[FILENAME]` is the file the program will encrypt.

Consider:
- The program will ask you a password to encrypt the file.
- The program will store the encrypted file (.ss)  and points file (.csv) in the same directory of `[FILENAME]`.

### Decryption
To decipher it is necessary to run:
```bash
python3 -m secret_sharing d [FILENAME] [POINTS_FILE]
```

Where:

* `[FILENAME]` is the encrypted file with extension .ss .
* `[POUNST_FILE]` is a csv file with only the necessary points to decrypt.

## Tests

To run the test, execute:

```bash
pytest ./tests
```

