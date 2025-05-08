
def CesarCripto(Word, Number):
    CesarWord = ''
    Alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    Word = Word.upper()
    for i in Word:
        if i in Alfabet:
            NewLetter = (Alfabet.index(i) + Number) % len(Alfabet)
            CesarWord += Alfabet[NewLetter]
        else:
            CesarWord += i
    return CesarWord


def NumberCripto(Word):
    NumberWord = ''
    Alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    Word = Word.upper()

    for i in Word:
        if i in Alfabet:
            NumberWord += str(Alfabet.index(i) + 1) + '.'
        else:
            NumberWord += i
    return NumberWord


def BinarieCripto(Word):
    BinarieWord = ''
    Last = 0
    for i in range(len(Word)):
        if Word[i] == '.':
            Number = Word[Last:i]
            Last = i
            BinarieWord += str(bin(int(Number))[2:])
    return BinarieWord


def allCripto(Word, Num):

    CesarWord = ''
    Alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    Word = Word.upper()
    for i in Word:
        if i in Alfabet:
            NewLetter = (Alfabet.index(i) + Num) % len(Alfabet)
            CesarWord += Alfabet[NewLetter]
        else:
            CesarWord += i
    NumberWord = ''

    for i in CesarWord:
        if i in Alfabet:
            NumberWord += str(Alfabet.index(i) + 1) + '|'
        else:
            NumberWord += i

    BinarieWord = ''
    BinParts = NumberWord.split('|')
    for i in BinParts:
        if i:
            BinarieWord += str(bin(int(i))[2:]) + '|'

    return BinarieWord

# LAZY
# def allCripto(Word):
#    Word = CesarCripto(Word)
#    Word = NumberCripto(Word)
#    Word = BinarieCripto(Word)
#   return Word
#
