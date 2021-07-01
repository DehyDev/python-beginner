import random

leet_sheet = {
    "a" : ["4", "@"],
    "b" : ["6", "8"],
    "c" : ["(", "{", "[", "<"],
    "e" : "3",
    "g" : ["6", "9"],
    "h" : ["5", "#"],
    "i" : ["1", "!", "/", "\\", "|"],
    "j" : "]",
    "l" : "[",
    "o" : "0",
    "q" : "9",
    "s" : ["5", "$"],
    "t" : ["7", "+"],
    "u" : ["v", "V"],
    "v" : ["u", "U"],
    "z" : "2",
    " " : ["_", "-"]
}

print("""
█▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄ █ ▀█ █▀▀ █
█▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀ █ █▄ ██▄ ▄

Generate a beast password from the given word!!!

""")

while True:
  word = input("Enter a word to passwordize: ")

  passwordizer = lambda p : word[:i] + p + word[i + 1:]

  for i, char in enumerate(word):
      char = char.lower()
      
      if char in leet_sheet:
          if type(leet_sheet[char]) == list:
              if random.randint(0, 1):
                  char = random.choice(leet_sheet[char])
              else:
                  char = char.upper()
          else:
              char = leet_sheet[char]
              
          word = str(passwordizer(char))
          
  print(word,"\n")