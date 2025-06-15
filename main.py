import cv2
import argparse
import os

def encrypt(image_path, key):
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found. Check the path.")
        return

    encrypted = (image + key) % 256
    new_name = "encrypted_" + os.path.basename(image_path)
    cv2.imwrite(new_name, encrypted)
    print(f"Encrypted image saved as {new_name}")

def decrypt(image_path, key):
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found. Check the path.")
        return

    decrypted = (image - key) % 256
    new_name = "decrypted_" + os.path.basename(image_path)
    cv2.imwrite(new_name, decrypted)
    print(f"Decrypted image saved as {new_name}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="What to do: encrypt or decrypt")
    parser.add_argument("image_path", help="Path to your image")
    parser.add_argument("key", type=int, help="A number between 0 and 255")

    args = parser.parse_args()

    if args.key < 0 or args.key > 255:
        print("Key must be between 0 and 255")
        return

    if args.action == "encrypt":
        encrypt(args.image_path, args.key)
    else:
        decrypt(args.image_path, args.key)

if __name__ == "__main__":
    main()
