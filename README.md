# Caesar (Shift) Cipher Decoder

This Python script decodes a Caesar cipher by shifting each letter of a given encoded sentence (in lowercase) through all possible shifts (1-25). The user provides an encoded sentence, and the script will try to decode it by applying different shifts.

## How It Works

1. The script prompts the user to input a sentence to decode (lowercase letters only).
2. The input sentence is converted into its corresponding ASCII values.
3. For each shift from 1 to 25:
   - The script shifts each letter's ASCII value forward by one.
   - If the shifted value exceeds 'z', it wraps around to 'a'.
   - The shifted ASCII values are converted back into characters to form a new sentence.
4. The program prints the sentence for each shift, allowing the user to observe potential decoded results.

## Usage

1. Clone the repository or download the script.
2. Run the script in a Python environment:
    ```bash
    python caesar_cipher_decoder.py
    ```
3. When prompted, enter the encoded sentence (ensure all letters are in lowercase):
    ```
    Enter the sentence you want to decode (lowercase): <your encoded sentence>
    ```
4. The script will output the decoded sentence for each shift.
