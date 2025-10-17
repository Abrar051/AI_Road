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

#print(apply_thrust(45,unit='N'))

###################################

theta = 0
learning_rate = 0.1
tolerance = 0.0001
def gradient(theta):
       return 2 * (theta - 3) # Example: gradient of (theta - 3)^2
change = float('inf')
while change > tolerance:
       grad = gradient(theta)
       new_theta = theta - learning_rate * grad
       change = abs(new_theta - theta)
       theta = new_theta
       #print (change,tolerance)

#######

n = 1
while True:
  divisible = True
  for i in range(1, 11):
    if n % i != 0:
      divisible = False
      break
  if (divisible == False):
      break
  n += 1
#print(n)

grid = [
    [2, 4, 3, 1],
    [1, 5, 6, 2],
    [7, 8, 9, 3]
]

rows = len(grid)
cols = len(grid[0])
for i in range(rows):
    for j in range(cols):
        print(f"({i},{j})", end=" ")
    print()
print (rows,cols)