#Read and open file
f = open('census2021.txt', 'r').readlines()
#Iterate Through file 
for line in f:
    line = line.strip()
    final_str = ''
    words = line.split(' ')
    for word in words:
        final_str += ' '.join(word)
        final_str += ' * '
    print(final_str.lower())
