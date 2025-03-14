def encrypt(text):
    words = text.upper().split()  # Split text into words
    encrypted_words = [
        ".".join(str(ord(char) - ord('A') + 1) for char in word if char.isalpha())
        for word in words
    ]
    return " ".join(encrypted_words)  # Join words with a space

def decrypt(text):
    words = text.split(" ")  # Split words by space
    decrypted_words = [
        "".join(chr(int(num) + ord('A') - 1) for num in word.split(".") if num.isdigit())
        for word in words
    ]
    return " ".join(decrypted_words)  # Restore spaces between words

def main():
    while True:
        print("\nChoose an option:")
        print("1: Encrypt text")
        print("2: Decrypt text")
        print("3: Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            text = input("Enter text to encrypt: ")
            print("Encrypted:", encrypt(text))

        elif choice == "2":
            text = input("Enter numbers to decrypt (letters separated by dots, words by spaces): ")
            print("Decrypted:", decrypt(text))

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
