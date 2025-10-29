import qrcode
import argparse
import sys
import os

def create_qr_code(data, output_filename):
    """
    Generates a QR code from the given data and saves it to a file.
    """
    try:
        # Generate the QR code object
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_L, # Error correction level
            box_size=10, # Size of each "box" in pixels
            border=4,    # Thickness of the border
        )
        
        # Add the data to the QR code
        qr.add_data(data)
        qr.make(fit=True)
        
        # Create an image from the QR code object
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the image
        img.save(output_filename)
        
        print(f"Successfully generated QR code and saved it to: {output_filename}")
        
    except Exception as e:
        print(f"An error occurred while generating the QR code: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """
    Main function to parse command-line arguments and run the QR code generator.
    """
    # Initialize the argument parser
    parser = argparse.ArgumentParser(
        description="Generate a QR code from a given link or text."
    )
    
    # Add the required 'data' argument
    parser.add_argument(
        "data",
        type=str,
        help="The link or text you want to encode into the QR code."
    )
    
    # Add the optional 'output' argument
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="qrcode.png",
        help="The output filename for the generated QR code. (default: qrcode.png)"
    )
    
    # Parse the arguments from the command line
    args = parser.parse_args()
    
    # Validate output filename
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"Created directory: {output_dir}")
        except OSError as e:
            print(f"Error: Could not create directory '{output_dir}'. {e}", file=sys.stderr)
            sys.exit(1)
            
    # Call the function to create the QR code
    create_qr_code(args.data, args.output)

if __name__ == "__main__":
    main()
