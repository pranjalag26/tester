variable = "Hello"

def greeting_function():
  name = input(f"{variable}, what is your name?\n")
  name = name.capitalize()
  
  print(f"{variable}, {name}. I'm pleased to meet you!\n")
  
greeting_function()
