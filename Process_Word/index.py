import itertools
import enchant


#Initialize dictionairy


d = enchant.Dict("en_US")



#importantletter = "L"




#all letters in the alphabet



letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z" ]


#initialize length of word(s)


numbers = [1,2,3,4,5,6,7,8]
words = []


#produce every combination
for x in numbers:
    words.extend( [''.join(y) for y in itertools.product(letters, repeat=int(x))])
#spellcheck each word
words = list(filter(lambda x:d.check(x) , words))


#and importantletter in x
from contextlib import redirect_stdout
#export result to a file
with open('out.txt', 'w') as f:
   with redirect_stdout(f):
        print(words)
import itertools   
   
