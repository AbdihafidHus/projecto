name = input("TYpe your name")
print("Welcome", name, "to this adventure!")

answer = input(
  "You are on a dirt road, it has come to an end and you can go left and right. Which way would you like to go ").lower()

if answer == "left":
  answer = input(" You come to a river, you can walk around it or swim across? type walk to walk around and swim to swim across")
  
  if answer == "swim":
    print("You swam across and were eaten by a whale")
    elif answer == "walk":
      pribt("You walked for many miles and ran out of water, starved ")
     else:
  print('Not a valid option. You lose')

 elif answer == "right":
  answer = input("You come to a bridge, it looks wobbly, do you wann cross it or head back? (cross/back)")

 if answer == "back":
    print("You go back to the main street and a monster has showwed up, You lose, you re doomed")
    elif answer == "cross":
      pribt("You cross the bridge and meet and stranger, do you talk to them? yes say yes no say no")
     else:
  print('Not a valid option. You lose')
 if answer == "yes":
    print("You have been killed by that stranger")
    elif answer == "no":
      pribt("You saw the strangers knife and u escaped his attempt to stab you. you have cross the bridge! YOu Won!")
     else:
  print('Not a valid option. You lose')

else:
  print('Not a valid option. You lose')
