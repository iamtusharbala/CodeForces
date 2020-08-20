vowels = ['a','e','i','o','u']
word = input()
low = word.lower()
for letter in low:
  for vowel in vowels:
    if letter == vowel:
      print(letter,end="")
      
      #Not complete