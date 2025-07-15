# Program ini berisi cara kerja dari sorting hat yang ada pada film terkenal harry potter.

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

question1 = int(input('''Q1) Do you like Dawn or Dusk?
1) Dawn
2) Dusk
Answer [1/2]: '''))

if question1 == 1:
  Gryffindor = Gryffindor + 1
  Ravenclaw = Ravenclaw + 1
elif question1 == 2:
  Hufflepuff = Hufflepuff + 1
  Slytherin = Slytherin + 1
else:
  print("Wrong input.")

question2 = int(input('''When I'm dead, I want people to remember me as: 
1.) The Good
2.) The Great
3.) The Wise
4.) The Bold
Answer [1-4]: '''))

if question2 == 1:
  Hufflepuff = Hufflepuff + 2
elif question2  == 2:
  Slytherin = Slytherin + 2
elif question2  == 3:
  Ravenclaw = Ravenclaw + 2
elif question2 == 4:
  Gryffindor = Gryffindor + 2
else:
  print("Wrong input.")

question3 = int(input('''Which kind of instrument most pleases your ear?
1.) The violin
2.) The trumpet
3.) The piano
4.) The drum
  Answer [1-4]: '''))

if question3 == 1:
  Slytherin = Slytherin + 4
elif question3 == 2:
  Hufflepuff = Hufflepuff + 4
elif question3 == 3:
  Ravenclaw = Ravenclaw + 4
elif question3 == 4:
  Gryffindor = Gryffindor + 4
else:
  print("Wrong input.")

print(f'''
🦁 Gryffindor :{Gryffindor}
🦅 Ravenclaw  :{Ravenclaw}
🦡 Hufflepuff :{Hufflepuff}
🐍 Slytherin :{Slytherin}
''')

if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
  print("Most point: 🦁 Gryffindor")
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
  print("Most point: 🦅 Ravenclaw")
elif Hufflepuff >= Slytherin:
  print("Most point: 🦡 Hufflepuff")
else:
  print("Most point: 🐍 Slytherin")