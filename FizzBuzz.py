def get_fizz_buzz(num):
   f_fizz = num % 3 == 0
   b_buzz = num % 5 == 0
   if f_fizz and b_buzz:
      return "FizzBuzz"
   elif f_fizz:
      return "Fizz"
   elif b_buzz:
      return "Buzz"
   else:
      return num
for num in range(1, 101):
    print(get_fizz_buzz(num))