#!/usr/bin/env python3
import qrcode
import io
import argparse

def qr_data_input(string_data: str) -> qrcode.QRCode:
    """Generate a QR code object from a string.

    Args:
        string_data: The input string to be encoded as a QR code.

    Returns:
        A QR code object representing the input string.

    """
    qr = qrcode.QRCode()
    qr.add_data(string_data)
    return qr


def print_ascii(data: qrcode.QRCode) -> None:
    """Print the QR code as ASCII art to the terminal.
65
    Args:
        data: The QR code object to be printed as ASCII art.

    """
    f = io.StringIO()
    data.print_ascii(out=f)
    f.seek(0)
    print(f.read())


def gen_png_image(data: qrcode.QRCode, file_name: str, mode: str = "save") -> None:
    """Generate a PNG image of the QR code.

    Args:
        data: The QR code object to be converted into an image.
        file_name: The name of the PNG file to be saved.

    """
    data.make(fit=True)
    img = data.make_image(fill_color="black", back_color="white")
    if mode == "save":
        img.save(f"{file_name}.png")
    if mode == "open":
        return img
    

def main() -> None:
    """The main function to handle command-line arguments and generate QR code."""
    parser = argparse.ArgumentParser(description='QR Code Generator')
    parser.add_argument('value', type=str, nargs='?', default='hello', help='Input string')
    parser.add_argument('-t', '--terminal', action='store_true', help='Print to terminal')
    parser.add_argument('-i', '--image', action='store_true', help='Generate image')
    parser.add_argument('-ti', '--terminal_image', action='store_true', help='Print to terminal and generate image')
    args = parser.parse_args()

    data = qr_data_input(args.value)

    if not (args.terminal or args.image or args.terminal_image):
        args.terminal = True  # Default to print to terminal

    if args.terminal:
        print_ascii(data)

    if args.image:
        gen_png_image(data, args.value)

    if args.terminal_image:
        print_ascii(data)
        gen_png_image(data, args.value)


if __name__ == "__main__":
    main()
