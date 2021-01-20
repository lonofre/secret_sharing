# Shamir's Secret Sharing 

## Requirements

Python 3 is required to run the app and the following packages are needed:

* pycryptodomex
* click

You can install those packages with:

```bash
pip3 install pycryptodomex
pip3 install -U click 
```

Also, if you want to run the tests, you have to install pytest:

```bash
pip3 install pytest
```
## Tests

To run the test, execute:

```bash
.../secret_sharing$ pytest ./tests
```

## Usage

## Encryption
To encrypt is necessary to run:
'''bash
.../secretsharing$ python3 -m secret_sharing c N T [FILENAME]
'''
Where:
* N is the total points the program will store.
* T it the minimum number of points required in order to decrypt the file.
* FILENAME is the file the program will encrypt.

## Decryption
To decipher it is necessary to run:
'''bash
.../secret_sharing$ python3 -m secret_sharing d [FILENAME] [POINTS_FILE]
'''

Where:
*FILENAME is the encrypted file with extension .ss .
*POUNST_FILE is a csv file with only the necessary points to decrypt.
