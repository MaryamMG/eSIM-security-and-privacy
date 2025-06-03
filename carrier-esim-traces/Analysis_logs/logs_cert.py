import re
import binascii
from pyasn1.codec.der import decoder

# Define the input and output file paths
input_file_path = "/mint_esim_installation_QRcode_rooted.log"  # Replace with your input file path
output_file_path = "output_certs.txt"  # Replace with your output file path

# Open the input and output files
with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    # Iterate through each line in the input file
    for line in input_file:
        # Check if the line contains "Send: ApduCommand"
        if "cert" in line:
            # Extract the content inside parentheses using regular expressions
            match = re.search(r'\((.*?)\)', line)
            if match:
                output_file.write(f"Decoded CMD: {line}\n\n")
                

print("Certs extracted, decoded, and saved to", output_file_path)
