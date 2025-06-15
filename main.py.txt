import cv2
import numpy as np
import os

def encrypt_image(image_path, key, output_path="encrypted.png"):
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found.")
        return

    encrypted = (image + key) % 256
    cv2.imwrite(output_path, encrypted)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, key, output_path="decrypted.png"):
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found.")
        return

    decrypted = (image - key) % 256
    cv2.imwrite(output_path, decrypted)
    print(f"Image decrypted and saved to {output_path}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Simple Image Encryption Tool")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("image", help="Path to the input image")
    parser.add_argument("key", type=int, help="Numeric key for encryption/decryption")
    parser.add_argument("--output", default=None, help="Optional output file name")
    args = parser.parse_args()

    if args.mode == "encrypt":
        encrypt_image(args.image, args.key, args.output or "encrypted.png")
    else:
        decrypt_image(args.image, args.key, args.output or "decrypted.png")

if __name__ == "__main__":
    main()
