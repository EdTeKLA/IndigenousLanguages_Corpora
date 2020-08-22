import sys
import argparse
import re

class Preprocess:
    def __init__(self, filename, output_filename, mode):
        self.filename = filename
        self.output_filename = output_filename

        if mode == "cr":
            self.new_lines = preprocessCree()
            writeResult()
        else:
            self.new_lines = preprocessEn()
            writeResult()

        return
        
    def preprocessCree(self):
        new_lines = []
        lines = open(self.filename, 'r').readlines()

        for line in lines:
            line = line.strip()

            # Lowercase everything
            line = line.lower()

            # Convert all accents to hat accents instead of bar
            line = re.sub(r"ā", r"â", line)
            line = re.sub(r"ē", r"ê", line)
            line = re.sub(r"ī", r"î", line)
            line = re.sub(r"ō", r"ô", line)

            # Put a space before punctuation
            line = re.sub(r"([':,!.?])", r" \1", line)

            # Remove ellipsis
            line = re.sub(r'(\.){2}}', '', line)
            
            # Remove double quotes
            line = re.sub(r'“', '', line)  
            line = re.sub(r'”', '', line)  
            line = re.sub(r'"', '', line)  

            # If vowel on either side of the hyphen, insert an 'h'
            line = re.sub(r'([aioâêîô])\s*[‐-]\s*([aioâêîô])', r'\1h\2', line)

            # Remove hyphen and replace with nothing because two parts should be together
            line = re.sub(r'\s*[‐—]\s*', r'', line)

            # Remove numbers
            line = re.sub(r'[0-9]', '', line)

            # Remove extra spaces
            line = re.sub(r'\s+', r' ', line)

            # Remove anything other than essential characters
            line = re.sub(r"[^a-zA-Zâêîô.!?:,']+", r' ', line)
            new_lines.append(line)

        return new_lines

    def preprocessEn(self):
        new_lines = []
        lines = open(self.filename, 'r').readlines()

        for line in lines:
            line = line.strip()

            # Lowercase everything
            line = line.lower()

            # Put spaces before punctuation
            line = re.sub(r"([':,!.?])", r" \1", line)

            # Remove ellipsis
            line = re.sub(r'(\.){2}}', '', line)

            # Remove double quotes
            line = re.sub(r'“', '', line)  
            line = re.sub(r'”', '', line)
            line = re.sub(r'"', '', line)  

            # Remove hyphen and replace with space because two words can standalone mostly in English
            line = re.sub(r'\s*[‐—]\s*', r' ', line)

            # Remove numbers
            line = re.sub(r'[0-9]', '', line)

            # Remove extra spaces
            line = re.sub(r'\s+', r' ', line)

            # Remove anything other than essential characters
            line = re.sub(r"[^a-zA-Z.!?:,']+", r' ', line)
            new_lines.append(line)

        return new_lines

    def writeResult(self):
        f = open(self.output_filename, 'w')
        for line in self.new_lines:
            f.write(line + '\n')
        f.close()
        return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-filename",help="Name of text file to preprocess.")
    parser.add_argument("-output_filename",help="Name of output processed file.")
    parser.add_argument("-mode",help="Cree (cr) or English (en).")

    args = vars(parser.parse_args())
    filename = args['filename']
    output_filename = args['output_filename']
    mode = args['mode']

    Preprocess(filename, output_filename, mode)