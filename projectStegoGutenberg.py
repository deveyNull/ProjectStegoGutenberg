"""
Welcome to Project StegoGutenberg
by deveyNull
"""

print("What would you like to encrypt?\n")
string = input()

print("\nOriginal Text\n_____________________\n")
print(string)

#This is just some example file if you wanna use it
#import randomguesses_made = 0name = raw_input('Hello! What is your name?\n')number = random.randint(1, 20)print 'Well, {0}, I am thinking of a number between 1 and 20.'.format(name)while guesses_made < 6:`guess = int(raw_input('Take a guess: '))`guesses_made += 1`if guess < number:``print 'Your guess is too low.'`if guess > number:``print 'Your guess is too high.'`if guess == number:``breakif guess == number:`print 'Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made)else:`print 'Nope. The number I was thinking of was {0}'.format(number)"


#easiest way is to use an ascii table
#copy it into word, delete all collumns but the first
#copy table from http://textalyser.net/ into word doc
#copy first column into original table
#copy into notepadd++, which deletes table, retains formatting
#Shift+alt+Down arrow selects everything, then edit that column

#This is the default Moby Dick column

MobyDictionary = {
' ': ' a',
'!': ' of',
'"': ' and',
'#': ' in',
'$': ' to',
'%': ' ant',
'&': ' that',
'\'': ' is',
'(': ' it',
')': ' but',
'*': ' by',
'+': ' as',
',': ' at',
'-': ' his',
'.': ' with',
'/': ' whale',
'0': ' for',
'1': ' all',
'2': ' their',
'3': ' from',
'4': ' this',
'5': ' are',
'6': ' was',
'7': ' they',
'8': ' so',
'9': ' one',
':': ' be',
';': ' s',
'<': ' he',
'=': ' fish',
'>': ' on',
'?': ' which',
'@': ' had',
'A': ' or',
'B': ' what',
'C': ' whales',
'D': ' not',
'E': ' when',
'F': ' these',
'G': ' now',
'H': ' like',
'I': ' have',
'J': ' then',
'K': ' some',
'L': ' were',
'M': ' i',
'N': ' tail',
'O': ' them',
'P': ' we',
'Q': ' upon',
'R': ' other',
'S': ' more',
'T': ' you',
'U': ' if',
'V': ' him',
'W': ' into',
'X': ' fast',
'Y': ' an',
'Z': ' up',
'[': ' time',
'\\': ' been',
']': ' those',
'^': ' seemed',
'_': ' there',
'`': ' still',
'a': ' our',
'b': ' no',
'c': ' her',
'd': ' us',
'e': ' the',
'f': ' line',
'g': ' two',
'h': ' though',
'i': ' only',
'j': ' any',
'k': ' boat',
'l': ' would',
'm': ' will',
'n': ' most',
'o': ' after',
'p': ' has',
'q': ' its',
'r': ' last',
's': ' long',
't': ' away',
'u': ' such',
'v': ' sperm',
'w': ' flukes',
'x': ' very',
'y': ' might',
'z': ' great',
'{': ' may',
'|': ' yet',
'}': ' between',
'~': ' lord',
'\n': ' whatever',
'`': ' moby'
}

#get rid of all carriage returns and newlines
#replace all tabs with `
newString = ""
print("\nEncoding...\n")
for i in string:
    
    newString = newString + str(MobyDictionary[i])
print("\nEncoded Text\n_____________________\n")
print(newString)
print("\n")
print("Decoding...\n")

MobyDictionaryDecoder = {
'a': ' ',
'of':	'!',
'and':	'"',
'in':	'#',
'to':	'$',
'ant':	'%',
'that':	'&',
'is':	'\'',
'it':	'(',
'but':	')',
'by':	'*',
'as':	'+',
'at':	',',
'his':	'-',
'with':	'.',
'whale':	'/',
'for':	'0',
'all':	'1',
'their':	'2',
'from':	'3',
'this':	'4',
'are':	'5',
'was':	'6',
'they':	'7',
'so':	'8',
'one':	'9',
'be':	',',
's':	';',
'he':	'<',
'fish':	'=',
'on':	'>',
'which':	'?',
'had':	'@',
'or':	'A',
'what':	'B',
'whales':	'C',
'not':	'D',
'when':	'E',
'these':	'F',
'now':	'G',
'like':	'H',
'have':	'I',
'then':	'J',
'some':	'K',
'were':	'L',
'i':	'M',
'tail':	'N',
'them':	'O',
'we':	'P',
'upon':	'Q',
'other':	'R',
'more':	'S',
'you':	'T',
'if':	'U',
'him':	'V',
'into':	'W',
'fast':	'X',
'an':	'Y',
'up':	'Z',
'time':	'[',
'been':	'\\',
'those':	']',
'seemed':	'^',
'there':	'_',
'still':	'`',
'our':	'a',
'no':	'b',
'her':	'c',
'us':	'd',
'the':	'e',
'line':	'f',
'two':	'g',
'though':	'h',
'only':	'i',
'any':	'j',
'boat':	'k',
'would':	'l',
'will':	'm',
'most':	'n',
'after':	'o',
'has':	'p',
'its':	'q',
'last':	'r',
'long':	's',
'away':	't',
'such':	'u',
'sperm':	'v',
'flukes':	'w',
'very':	'x',
'might':	'y',
'great':	'z',
'may':	'{',
'yet':	'|',
'between':	'}',
'lord':	'~',
'whatever':	'\n',
'moby':	'`',
'':	''
} 

newerString = ""
for word in newString.split(" "):

    newerString = newerString + str(MobyDictionaryDecoder[word])
print("Final:\n_____________________\n")
print(newerString)
print("\n\nOriginal, for comparison:\n_____________________\n")
print(string)
