import random

# написанные гением программирования цепии маркова
# генератор текста примитивный, в зависимости от соурса надо добавлять редактирование с помощью регулярок

class MarkovChain:

    def __init__(self):
        self.worddict = {}


    def add_text(self, text):
        text = text.lower()
        words = text.split()
        for x in range(len(words)-1):
            word = words[x]
            next_word = words[x+1]
            
            if word not in self.worddict:
                self.worddict[word] = {}
            if next_word not in self.worddict[word]:
                self.worddict[word][next_word] = 1
            else:
                self.worddict[word][next_word] += 1

    def _get_word(self, word):
        if not word in self.worddict:
            return False

        n_words = []
        for n_word in self.worddict[word]:
            for x in range(self.worddict[word][n_word]):
                n_words.append(n_word)
                
        return random.choice(n_words)

    def generate_text(self, length):
        word = random.choice(list(self.worddict.keys()))
        text = word[0].upper() + word[1:]
        for x in range(length):
            word = self._get_word(word)
            if not word:
                text += '.'
                word = random.choice(list(self.worddict.keys()))
                word = word[0].upper() + word[1:]
            text += ' ' + word

        return text
    
mc = MarkovChain()
    
def main():
    f = open("D:\GitHub/adgvkty\Python\MarkovChains/text.txt")
    text = f.read()
    mc.add_text(text)
        
    print(mc.generate_text(30))
        
    
main()
        
