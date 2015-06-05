#steGutEncoder
 
import random
print("What would you like to encrypt?\n")
string = input()
 
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
' ': ' alter',
'!': ' of',
'"': ' and',
'#': ' in',
'$': ' to',
'%': ' ant',
'&': ' that',
'\'': ' cow',
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
';': ' so',
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
'\t': ' tab',
'`': ' moby'
}
 
 
#get rid of all carriage returns and newlines
#replace all tabs with `
newString = ""
for i in string:
   
    number = random.random()
    if number < .05:
         newString = newString + "."
         a = str(MobyDictionary[i]).title()
         newString = newString + a
        
    #elif number > .05 and number < .3:
         #newString = newString + " SECRETWORD"
    else:
        newString = newString + str(MobyDictionary[i])
        
newString = newString + "."
 
print("\nEncoded Text\n_____________________\n")
print(newString)
print("\n_____________________\n")
 
print("Now all you have to do is visit https://www.gutenberg.org/files/2701/2701-h/2701-h.htm#link2HCH0001 and copy the text into a notepad file. Delete a chapter (or two) in the middle, specifically one where Melville rants about whales. Noone cares you old loon. Then, replace that chapter(s) you just deleted with the text ouputted by this program.\nVoila! You now have a text document that can beat any egress filter in the world. To decode, just copy and paste your chapter(s) into the SteGutenberg Decoder.")
