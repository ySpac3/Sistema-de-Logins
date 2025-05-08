def BinarieDesripto(Word):
    IntWord = ''
    for i in Word:
        if i == '.':
            Number = Word[:Word.index(i)]
            IntWord += str(int(Number, 2)) + '.'
    return IntWord


def NumberDescripto(Word):
    Last = 0
    AlphabetWord = ''
    Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    Word = Word.upper()

    for i in range(len(Word)):
        if Word[i] == '.':
            Number = Word[Last:i]
            Last = i+1
            AlphabetWord += str(Alphabet[int(Number)]) + '.'

    return AlphabetWord


def CesarDescripto(Word, Number):
    CorrectWord = ''
    Last = 0
    Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    Word = Word.upper()

    for i in range(len(Word)):
        if Word[i] == '.':
            Letter = Word[Last:i]
            if Letter in Alphabet:
                # Eu nn sei pq to tendo q por menos 1 aqui mas funcionou então ok
                CorrectWord += Alphabet[Alphabet.index(
                    Word[Last:i]) - Number - 1]
            else:
                CorrectWord += Word[Last:Word[i]]
    return CorrectWord


def AllDescripto(Word, Num):

    BinParts = Word.split('|')
    IntWord = ''
    for i in BinParts:
        if i:
            IntWord += str(int(i, 2)) + '|'
    AlphabetParts = IntWord.split('|')
    AlphabetWord = ''
    Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

    for i in AlphabetParts:
        if i:
            AlphabetWord += Alphabet[int(i)] + '|'
    
    CorrectWord = ''
    CorrectParts = AlphabetWord.split('|')
    for i in CorrectParts:
        if i:
            if i in Alphabet:
                CorrectWord += Alphabet[Alphabet.index(i)-Num-1]
            else:
                CorrectWord += Alphabet[Alphabet.index(i)-Num-1]
    return CorrectWord


