# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
  row = 1
  s_pattern = ""
  while row <= n:
    if n == 1:
      return "*"
    if row == 1:
      s_pattern += "*" * n + "\n"
    if row > 1 and row < n:
      s_pattern += "*" + " " * (n-2) + "*\n"
    if row == n:
      s_pattern += "*" * n
      return s_pattern
    row += 1

# 1
# 12
# 123
# 1234
def number_pattern(n):
  row = 1
  full_pattern = ""
  while row <= n:
    num = 1
    pattern = ""
    while num <= row:
      pattern += str(num)
      num += 1
    full_pattern += pattern
    if row < n:
      full_pattern += "\n"
    row += 1
  return full_pattern

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
  numbers = 1
  sum = 0
  while numbers <= n:
    sum += numbers
    numbers += 1
  return sum

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
  pyramid = ""
  for i in range(1, n + 1):
     row=""
     spaces = " " * (n-i)
     stars = "*" * (2 * i - 1)
     if i < n:
       row += spaces + stars + "\n"
     else:
       row += spaces + stars
     pyramid += row
  return pyramid