"""
Caesar Cipher Implementation in Python

Usage:
    python caesar_cipher.py

Author: Susobhida
License: MIT
"""


def encrypt(text: str, shift: int) -> str:
    """
    Encrypt plaintext using Caesar cipher.

    Args:
        text  : The message to encrypt.
        shift : Number of positions to shift (0–25).

    Returns:
        Encrypted ciphertext string.
    """
    result = []
    shift %= 26  # Normalise shift to 0–25

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)  # Non-alpha characters pass through unchanged

    return ''.join(result)


def decrypt(text: str, shift: int) -> str:
    """
    Decrypt ciphertext using Caesar cipher.

    Args:
        text  : The message to decrypt.
        shift : The shift that was used during encryption.

    Returns:
        Decrypted plaintext string.
    """
    return encrypt(text, -shift)  # Decryption is just a negative shift


def brute_force(text: str) -> None:
    """
    Print all 26 possible decryptions of the given ciphertext.
    Useful when the shift is unknown.

    Args:
        text : The ciphertext to brute-force.
    """
    print("\n--- Brute-Force Attack (all 26 shifts) ---")
    for shift in range(26):
        print(f"  Shift {shift:2d}: {decrypt(text, shift)}")

def _get_shift() -> int:
    while True:
        try:
            shift = int(input("Enter shift value (0-25): "))
            if 0 <= shift <= 25:
                return shift
            print("  ⚠  Please enter a number between 0 and 25.")
        except ValueError:
            print("  ⚠  Invalid input. Please enter an integer.")


def main() -> None:
    print("=" * 45)
    print("        Caesar Cipher Tool")
    print("=" * 45)

    while True:
        print("\nOptions:")
        print("  1. Encrypt a message")
        print("  2. Decrypt a message")
        print("  3. Brute-force decrypt (try all shifts)")
        print("  4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == '1':
            text  = input("Enter plaintext : ")
            shift = _get_shift()
            print(f"\n✅ Encrypted: {encrypt(text, shift)}")

        elif choice == '2':
            text  = input("Enter ciphertext: ")
            shift = _get_shift()
            print(f"\n✅ Decrypted: {decrypt(text, shift)}")

        elif choice == '3':
            text = input("Enter ciphertext: ")
            brute_force(text)

        elif choice == '4':
            print("\nGoodbye! 👋")
            break

        else:
            print("  ⚠  Invalid choice. Please enter 1, 2, 3, or 4.")

 def _run_tests() -> None:
    """Quick sanity-check test suite."""
    # Basic encrypt / decrypt round-trip
    assert decrypt(encrypt("Hello, World!", 3), 3) == "Hello, World!"
    assert encrypt("ABC", 1) == "BCD"
    assert encrypt("XYZ", 3) == "ABC"          # wrap-around
    assert encrypt("xyz", 3) == "abc"          # lowercase wrap
    assert encrypt("Hello, World!", 0) == "Hello, World!"  # zero shift
    assert encrypt("ABC", 26) == "ABC"         # shift % 26 == 0
    assert encrypt("abc", -1) == "zab"         # negative shift
    assert encrypt("Hello 123!", 13) == "Uryyb 123!"  # ROT13, digits untouched
    print("✅ All tests passed.")


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        _run_tests()
    else:
        main()
