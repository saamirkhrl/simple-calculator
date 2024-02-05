firstInput = int(input('enter your first number: '))
operator = input('operator: [+, -, *, /] ')
secondInput = int(input('enter your second number: '))

if operator == '+':
  print(firstInput + secondInput)

if operator == "-":
  print(firstInput - secondInput)

if operator == "*":
  print(firstInput * secondInput)

if operator == "/":
  print(firstInput / secondInput)