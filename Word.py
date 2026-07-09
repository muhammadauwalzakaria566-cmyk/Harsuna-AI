word_bank = {
    'fata' : 'skin',
    'kunne' : 'ear',
    'edo' : 'eye',
    'hanci' : 'nose',
    'harci' : 'tongue'
}

def translate(word):
    if word in word_bank:
        return word_bank[word]
    else:
        return 'word not found'

class WordBankStats:
    def __init__(self, bank):
        self.total = len(bank)
    def summary(self):
        print('the word bank has ' + str(self.total) + ' words')
    
    
print(translate('harci'))
print(translate('kafa'))
stats = WordBankStats(word_bank)
stats.summary()

test_words = ['edo' , 'yatsa', 'kunne']
for w in test_words:
    print(translate(w))
