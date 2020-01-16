def clear():
    print("\033[2J")

def locate(line,column):
    print("\033[{};{}H".format(line,column), end="")
  
def clearLine(line=None, column=None):
    if line is not None and colum is not None:
        locate(line, colum)
    elif line is not None:
        locate(line,1)
        
    print("\033[K", end="")
def processParams(params):
    if 'line' in params:
        line = params['line']
        colum = 1
        if 'column' in params:
            column = params['column']
            
            locate(line, column)
        
        if 'color' in params and params['color'] in colors:
            print("\033[{}m".format(colors[params['color']]), end="")





clear()
locate(5,4)
print("*")