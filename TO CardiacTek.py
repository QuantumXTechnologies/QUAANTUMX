# import turtle
#
# # Set up the turtle
# t = turtle.Turtle()
# t.speed(0)
# t.color("red", "yellow")
#
# # Draw the petals of the flower
# for i in range(50):
#     t.begin_fill()
#     t.circle(100)
#     t.left(50)
#     t.end_fill()
#
# # Move the turtle to the center of the flower
# t.penup()
# t.goto(0, 0)
# t.pendown()
#
# # Write the message
# t.write("Merry Christmas and Happy New Year", font=("Arial", 24, "normal"))
#
# # Display the turtle
# turtle.done()



#
#
# import turtle
#
# # Set up the turtle
# t = turtle.Turtle()
# t.speed(0)
# t.color("red", "yellow")
# t.pensize(4)
# # Draw the petals of the flower
# for i in range(50):
#     t.circle(100)
#     t.left(50)
# # Move the turtle to the center of the flower
# t.penup()
# t.goto(0, 0)
# t.pendown()
# # Set the font size and style
# t.color("black")
# t.write("To The Team Happy Holidays", font=("Arial", 24, "normal"))
# # Display the greeting message
# t.penup()
# t.goto(-250, -200)
# t.pendown()
# t.write("Cardiac Tek Team,", font=("Arial", 20, "normal"))
# t.penup()
# t.goto(-250, -230)
# t.pendown()
# t.write("I hope this message finds you well. As the holiday begins, I wanted to take a moment to wish you and your loved ones a very merry Christmas and a happy new year.", font=("Arial", 10, "normal"))
# t.penup()
# t.goto(-250, -270)
# t.pendown()
# t.write("Thank you for all your hard work. I am grateful to have such a talented and dedicated team. Looking forward to continuing to work with all of you in the new year.", font=("Arial", 10, "normal"))
# t.penup()
# t.goto(-250, -310)
# t.pendown()
# t.write("Wishing you a festive holiday season and a successful and fulfilling new year.", font=("Arial", 10, "normal"))
# t.penup()
# t.goto(-250, -350)
# t.pendown()
# t.write("Best regards,", font=("Arial", 10, "normal"))
# t.penup()
# t.goto(-250, -380)
# t.pendown()
# t.write("Computer Wizard", font=("Arial", 10, "normal"))
# # Display the turtle
# turtle.done()


def greet(name):
  print(f"Hello, {name}!")

def confirm_sent_code():
  print("Yes, it was ChatGPT who sent the code.")
  print("We hope you find it helpful and easy to use.")

greet("Longnus Gilbert")
confirm_sent_code()


import turtle

def draw_sun():
  t = turtle.Turtle()
  t.speed(0)
  t.color("yellow", "yellow")
  t.begin_fill()
  t.circle(50)
  t.end_fill()

def print_message():
  print("Some of the few are for the many.")
  print("It should be the enjoyment of the few.")
  print("After all, it's the little things in life that bring us the most joy.")
  print("So go ahead, indulge in the pleasures that bring you happiness.")
  print("Life is too short to miss out on the things that bring us joy.")
  print("Embrace the moment and make the most of it.")

draw_sun()
print_message()

turtle.done()
print("This is for you Engineer Godson")

#ENJOY THE HOLIDAY
print("TO TEXTILE ENGINEERS")
def greet(name):
  print(f"Hello, {name}!")

def wish_happy_holidays(name):
  print(f"Wishing you a happy holiday, {name}!")
  print("May it be filled with joy, love, and all the things that bring you happiness.")
  print("Take time to relax and enjoy the company of your loved ones.")
  print("Remember to be grateful for all the good things in your life.")
  print("Here's to a festive holiday season and a successful new year!")

classmates = ["Kidamabi", "Feva", "Delphine", "Obedi", "Abduli",
              "Chacha", "BajuBoi", "Mwamboli", "Avitus", "King Muttah", "Mgasa"]

for classmate in classmates:
  greet(classmate)
  wish_happy_holidays(classmate)
  print()
