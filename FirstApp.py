def HasRemainder (number1,number2):
    if (number1%number2 == 0):
        return False
    else:
        return True

def apply_thrust(force_value, unit):
  # unit expected to be either 'N' (newtons) or 'lbf' (pounds-force)
    if not isinstance(force_value, (int, float)):
        raise ValueError("force_value must be a number.")
    if unit == 'lbf':
        # convert to newtons: 1 lbf ≈ 4.4506 N
        force_in_newtons = force_value * 4.4506
    elif unit == 'N':
        force_in_newtons = force_value
  # MISSING LINE
    return force_in_newtons


prime_range = int(input('Enter the range you want to find prime number :  '))

if (prime_range == 1 | prime_range == 2):
    print('Please enter something greater than 2')
else:
    for i in range (1,prime_range):
        if (i%2 == 0):
            continue
        else:
            if (i==2):
                print (i)
            else:
                flag = True
                for j in range (2,i):
                    #print ('H ' + str(j))
                    if (HasRemainder(i,j) == False):
                        flag = False
                if (flag == True):
                    print (i)
