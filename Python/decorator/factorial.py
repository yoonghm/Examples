from clockdeco import clock

@clock
def factorial(n):
  return 1 if n < 2 else n*factorial(n-1)

if __name__ == '__main__':
  factorial(30)
