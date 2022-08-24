def check_for_float(input1, exit = True):
    try:
        val = float(input1)                 
        return val
    except (ValueError, TypeError):
        print('Error, please enter numeric input')
        if exit:
            quit()
        return False
count = 0                                
total = 0.0
average = 0.0
while True:                            
  input_number = input('Enter a number: ')
  if input_number == 'exit':
    break                             

  number = check_for_float(input_number, False)
  if not number:
    continue

  count += 1                           
  total = total + number         

  if count:
    average = total / count            

print(total, count, average)   
