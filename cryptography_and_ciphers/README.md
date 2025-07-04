# Caesar Cipher

The Caesar Cipher is one of the oldest and simplest encryption techniques, named after Julius Caesar who reportedly used it for secure communication. It operates as a **substitution cipher**, where each letter in the plaintext is shifted by a fixed number (the *key*) down or up the alphabet.

## How It Works

### Encryption
For a given key (e.g., `3`), each letter is replaced by the letter `3` positions later in the alphabet:
- Example: `A → D`, `B → E`, ..., `Z → C` (wrapping around)

### Decryption 
The reverse process shifts letters backward by the same key.

### Key Space
Only 25 possible shifts (since `key=26` or `0` leaves text unchanged), making it vulnerable to brute-force attacks.

## Limitations & Modern Use

While not secure for modern cryptography, the Caesar Cipher serves as a foundational concept for understanding:
- **Symmetric encryption** (same key for encryption/decryption)
- **Frequency analysis** attacks (exploiting letter patterns)
- **Modular arithmetic** in cryptography (wrapping around the alphabet)

Today, it's primarily used in:
- Education
- Puzzles
- As a building block for more complex algorithms

![Animation Preview](preview.png)