import re

#Read and open file
f = open('flanders.txt', 'r').readlines()

#Iterate Through file 
for line in f:
    #Remove spaces at beginning and at end of string
    line = line.strip()
    
    # Lowercase everything
    line = line.lower()
  
    #Change Macrons to match
    line = re.sub(r"ā", r"â", line)
    line = re.sub(r"ē", r"ê", line)
    line = re.sub(r"ī", r"î", line)
    line = re.sub(r"ō", r"ô", line)

    line = re.sub(r"á", r"â", line)
    line = re.sub(r"é", r"ê", line)
    line = re.sub(r"í", r"î", line)
    line = re.sub(r"ó", r"ô", line)

    #Remove Dashes (-)
    line = re.sub(r'\s*[-—]\s*', r'', line)

    # Remove numbers
    line = re.sub(r'[0-9]', '', line)

    # Remove non-word characters
    line = re.sub(r"\W", " ",line, flags=re.I)

    # Remove extra spaces
    line = re.sub(r'\s+', r' ', line)
    
    #new_lines.append(line)
    final_str = ''
    words = line.split(' ')

    #Add * to end of word
    for word in words:
        final_str += ' '.join(word)
        final_str += ' * '
    
    #print lower case
    print(final_str)
