# string concatenation 

word = ''
sentence = ''
print('Please enter some words.')
print('Include a period (.) when you are finished.')
while '.' not in word:
    word = input('next word: ')
    sentence = sentence + ' ' + word
print()
print('Aha! You said:')
print(sentence)