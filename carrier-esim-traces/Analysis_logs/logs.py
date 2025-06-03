import re
import binascii
from pyasn1.codec.der import decoder

# Define the input and output file paths
input_file_path = "/mint_esim_installation_QRcode_rooted.log"  # Replace with your input file path
output_file_path = "output_apdu_commands.txt"  # Replace with your output file path

# Open the input and output files
with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    # Iterate through each line in the input file
    for line in input_file:
        # Check if the line contains "Send: ApduCommand"
        if "Send: ApduCommand" in line:
            # Extract the content inside parentheses using regular expressions
            match = re.search(r'\((.*?)\)', line)
            if match:
                apdu_content = match.group(1).strip()  # Get content inside parentheses

                # Search for "cmd=" and extract its value
                cmd_match = re.search(r'cmd=([0-9A-Fa-f]+)', apdu_content)
                output_file.write(f"{apdu_content}\n\n")
                if cmd_match:
                    cmd_hex = cmd_match.group(1)
                    try:
                        # Decode the hexadecimal value and convert it to a string
                        cmd_decoded = binascii.unhexlify(cmd_hex).decode("utf-8", errors="ignore")
                        output_file.write(f"Decoded CMD: {cmd_decoded}\n\n")
                        
                        cmd_der = bytes.fromhex(cmd_hex)
                        #decoded_data, _ = decoder.decode(cmd_der, errors="ignore")
                        #output_file.write(f"Decoded ASN.1 DER: {decoded_data}\n\n")
                        
                        output_file.write("---------------------------\n")
                    except Exception as e:
                        # Handle decoding errors
                        output_file.write(f"Error decoding CMD: {str(e)}\n\n")
                else:
                    output_file.write("No 'cmd=' found in the extracted content\n\n")

print("Apdu commands extracted, decoded, and saved to", output_file_path)
