import os
#os.system("start \"\" https://www.google.com")

square = lambda val1: val1*val1

sum = lambda val1,val2: val1 + val2

product = lambda val1,val2 : val1*val2

absolute_diff = lambda val1,val2 : (val1-val2) if val1>val2 else (val2-val1)

def status():
    print("Function Imported !")