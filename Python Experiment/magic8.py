# Program magic 8 ball, atau biasa disebut bola ramalan, digunakan untuk mendapatkan jawaban dari pertanyaan yes no yang kita tanyakan kepada magic 8 ball tersebut.

import random

question = input("Question: ")

answer = random.randint(1, 9)

if answer == 1:
  text = "Yes - definitely."
elif answer == 2:
  text = "It is decidedly so."
elif answer == 3:
  text = "Without a doubt."
elif answer == 4:
  text = "Replz hazy, try again."
elif answer == 5:
  text = "Ask again later."
elif answer == 6:
  text = "Better not tell you now"
elif answer == 7:
  text = "My source say no."
elif answer == 8:
  text = "Outlook not so good."
else:
  text = "Very doubtful."

print(f"Magic 8 ball: {text}")