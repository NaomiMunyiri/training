#tuples declared with ()
#tuples-immutable(cannot be changed)

# dimensions=(50,100)
# print(dimensions[0])
# print(dimensions[1])

"""
A buffet style restaurant offers five basic foods. Think of five simple foods
and store them in a tuple
a) for loop to print each food offered
b) try and modify/change the items
c) the restaurant wants to change 2 items in the menu. write a line of code
     that rewrites the tuple and then use a for loop to print each item.
"""

menu=("rice","beans","chicken","beef","veg")

for food in menu:
    print(food)

new_menu=list(menu)
#print(new_menu)
new_menu.append("chapati")
print(new_menu)

new_menu[2]="fish"
new_menu[3]="ugali"

for food in new_menu:
    print(food)