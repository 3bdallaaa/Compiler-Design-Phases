import re

file = open("read1.py")

operators = {'=' : 'Assignment op','+' : 'add op','-' : 'sub op','/' : 'div op','*' : 'Multi op' }
operators_key = operators.keys()

key_word = {'int' : 'key word', 'float': 'key word' , 'char' : 'key word', 'switch' : 'key word', 'case' : 'key word','break' : 'key word','default' : 'key word' }
key_word_key = key_word.keys()

punctuators = { ':' : 'punc', ';' : 'punc', '.' : 'punc' , ',' : 'punc','(' : 'punc',')' : 'punc','{' : 'punc','}' : 'punc' }
punctuators_key = punctuators.keys()

identifier = { 'c' : 'id', 'y' : 'id' }
identifier_key = identifier.keys()

literal={ "'X'" : 'literal', "'N'" : 'literal' }
literal_key = literal.keys() #displays a list of all the keys in the dictionary

constant= {'0' : 'constant', '30' : 'constant','60' : 'constant' }
constant_key = constant.keys()


f=file.read()
#i=0

c=0
program = f.split("\n")
for line in program:
    c += 1
    print("line#" , c, "\n" , line)

    tokens=line.split(' ')
    print("Tokens are " , tokens)
    print("Line#", c, "properties \n")
    for token in tokens:
        if token in operators_key:
            print(token,"-> operator ")
        if token in key_word_key:
            print(token,"-> KEY_WORD")
        if token in punctuators_key:
            print (token, "-> Punctuation ")
        if token in identifier_key:
            print (token, "-> Identifier " )
        if token in constant_key:
            print (token, "-> constant " )
        if token in literal_key:
            print (token, "-> literal " )
