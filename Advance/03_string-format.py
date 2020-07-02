price = 40
str = "The price is {:.2f} dolors"
print(str.format(price))

str = "{:4d}\n{:4d}\n{:4d}\n{:4d}\n"
print(str.format(20, 300, 2002, 4))

#Use index number
age = 17
name = "Sueka"
txt = "Her name is {1}. {1} is {0} years old."
print(txt.format(age, name))
