#calculator build in python, needs use of terminal
#purpose of exercise is to see what is best to build the calculator
#visual representation with python is best done using Jupyter notebooks vs hardcoding this program here or using tkinter
#much easier to get visuals and see errors using vanilla JS

def add(a,b):
  result=a+b 
  print("a+b= ",result)

def sub(a,b):
  result=a-b
  print("a-b= ",result)

def mul(a,b):
  result=a*b
  print("a*b= ",result)

def div(a,b):
  result=a/b 
  print("a/b=", result)

  a=int(input("Enter the first number: "))
  b=int(input("Enter the second number: "))
  op=input("Enter the operator: ")

  if op=="+":
    add(a,b)
  elif op=="-":
    sub(a,b)
  elif op=="*":
    mul(a,b)
  elif op=="/":
    div(a,b)
  else: 
    print("Invalid!")


