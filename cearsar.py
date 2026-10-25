import argparse
from cryplib import encrypt, decrypt


def main():
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt a message using a Caesar cipher."
    )

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        "-e", "--encrypt",
        action="store_true",
        help="Encrypt the message"
    )

    group.add_argument(
        "-d", "--decrypt",
        action="store_true",
        help="Decrypt the message"
    )

    parser.add_argument(
        "-m", "--message",
        required=True,
        help="The message to encrypt or decrypt"
    )

    args = parser.parse_args()

    shift = 3

    if args.encrypt:
        result = encrypt(args.message, shift)
    else:
        result = decrypt(args.message, shift)

    print(result)


if __name__ == "__main__":
    main()