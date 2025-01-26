#magic8.py#

import random

name = "Sarah"
question = "Will it be warm today?"
answer = ""
random_number = random.randint(1,11)


if name == "":
  print("Question " + answer)
elif question == "":
  print("Please ask question to " + answer)
else:
  print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)

if random_number == 1:
  print("Yes - definately")
elif random_number == 2:
  print("It is decidedly so")
elif random_number == 3:
  print("Without a doubt")
elif random_number == 4:
  print("Reply hazy, try again")
elif random_number == 5:
  print("Better not tell you now")
elif random_number == 6:
  print("Better not tell you now")
elif random_number == 7:
  print("My sources say no")
elif random_number == 8:
  print("Outlook not so good")
elif random_number == 9:
  print("Very doubtful")
elif random_number == 10:
  print("The answer is No")
elif random_number == 11:
  print("It is likely")
else:
  print("Error")

