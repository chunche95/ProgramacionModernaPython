def clear():
    print("\033[2J")

def locate(line,column):
    print("\033[{};{}H".format(line,column), end="")
  
  


clear()
locate(5,4)
print("*")