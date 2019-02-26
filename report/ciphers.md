# ciphers

## previously tested requirements

- `affine_cipher`
  * `encryptMessage`
    - Returns expected ciphertext given a key and non-empty plaintext
- `base64_cipher`
  * Encoding and then decoding returns the original input
- `brute_force_caesar_cipher`
  * `decrypt`
    - Prints expected output (function just dumps several decryption results)
- `onepad_cipher`
  * Encoding and then decoding returns the original input
- `rabin_miller`
  * `generateLargePrime`
    - The returned number passes the `isPrime` function
- `rot13`
  * `dencrypt`
    - A single application on non-empty plaintext returns expected ciphertext
    - Two applications returns the original plaintext
- `simple_substitution_cipher`
  * `encryptMessage`
    - Returns expected ciphertext given non-empty plaintext
  * `decryptMessage`
    - Returns expected plaintext given non-empty ciphertext
- `transposition_cipher`
  * `encryptMessage`
    - Returns expected ciphertext given non-empty plaintext
  * `decryptMessage`
    - Returns expected plaintext given non-empty ciphertext
- `vigenere_cipher`
  * `encryptMessage`
    - Returns expected ciphertext given non-empty plaintext
  * `decryptMessage`
    - Returns expected plaintext given non-empty ciphertext
- `xor_cipher`
  Encoding and then decoding returns the original input string as a list of characters
  Encoding and then decoding, both as a string, returns the original input string
  * `XORCipher().encrypt_file`
    - Given a text file, doesn't crash
  * `XORCipher().decrypt_file`
    - Given a text file, doesn't crash

Untested modules: `base16`, `base32`, `base85`, `caesar_cipher`, `cryptomath_module`, `elgamal_key_generator`, `hill_cipher`, `playfair_cipher`, `rsa_cipher`, `rsa_key_generator`, and `transposition_cipher_encrypt_decrypt_file` 


## coverage

Coverage before refactor:
```
Name                                    Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------
ciphers/affine_cipher.py                   59     24     24      7    55%
ciphers/base64_cipher.py                   45      3     18      4    86%
ciphers/brute_force_caesar_cipher.py       22      6     10      1    78%
ciphers/cryptomath_module.py               13      1      6      1    89%
ciphers/onepad_cipher.py                   24      0     10      1    97%
ciphers/rabin_miller.py                    38      2     22      4    90%
ciphers/rot13.py                           18      3      8      2    73%
ciphers/simple_substitution_cipher.py      46     21     16      1    55%
ciphers/transposition_cipher.py            36     11     14      1    68%
ciphers/vigenere_cipher.py                 41     12     20      3    69%
ciphers/xor_cipher.py                      59     51     20      0    10%
-------------------------------------------------------------------------
TOTAL                                     401    134    168     25    64%
```

Coverage after refactor:
```
Name                                    Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------
ciphers/affine_cipher.py                   59     33     24      6    41%
ciphers/base64_cipher.py                   45      6     18      4    81%
ciphers/brute_force_caesar_cipher.py       22      6     10      1    78%
ciphers/cryptomath_module.py               13      8      6      0    37%
ciphers/onepad_cipher.py                   24      3     10      1    88%
ciphers/rabin_miller.py                    38      5     22      3    87%
ciphers/rot13.py                           18      9      8      2    50%
ciphers/simple_substitution_cipher.py      46     21     16      1    55%
ciphers/transposition_cipher.py            36     11     14      1    68%
ciphers/vigenere_cipher.py                 41     12     20      3    69%
ciphers/xor_cipher.py                      59      8     20      4    85%
-------------------------------------------------------------------------
TOTAL                                     401    122    168     26    68%
```
