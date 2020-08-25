import argparse
import re

class Bow:
    def __init__(self, filename, output_filename, mode):
        self.filename = filename
        self.output_filename = output_filename
        self.mode = mode

        self.words = self.createBag()
        self.bow = self.countWords()
        self.printBow()
        return  

    def createBag(self):
        '''
        Create a list of words in the text
        '''
        words = []

        lines = open(self.filename, 'r').readlines()
        #punct = ['.', ',', '!', ';', ]
        for line in lines:
            if self.mode == 'en':
                line = re.sub('[^\w\s]', '', line)
            elif self.mode == 'cr':
                line = re.sub('[^\w\sâêîôāēīō-]', '', line)
            parts = line.split()
            words.extend(parts)
        return words
    
    def countWords(self):
        '''
        Create and return a dictionary:
            key = word
            value = count in text
        '''
        word_cnt = {}
        for word in self.words:
            if word not in word_cnt.keys():
                cnt = self.words.count(word)
                word_cnt[word] = cnt

        return word_cnt

    def printBow(self):
        '''
        Print bow with a word and its count per line
        '''
        f = open(self.output_filename, 'w')
        alpha_order = sorted(self.bow.keys(), key=str.lower)
        for word in alpha_order:
            cnt = self.bow[word]
            f.write(word + ' ' + str(cnt) + '\n')
        f.close()
        return

if __name__=="__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-filename",help="Name of text file to create bow.")
    parser.add_argument("-output_filename",help="Name of text file to create bow.")
    parser.add_argument("-mode",help="Cree (cr) or English (en) text.")

    args = vars(parser.parse_args())
    filename = args['filename']
    output_filename = args['output_filename']
    mode = args['mode']
    
    Bow(filename, output_filename, mode)