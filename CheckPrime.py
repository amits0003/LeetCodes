

def checkPrimeNumber(num):
    if num in [1,2,3,5,7]:
        return True

    if num >3:
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 ==0:
            return False
        else :
            return True


def validatePrimeNumbers(num2):
    if checkPrimeNumber(num2):
        newNum = num2 - 2
        if checkPrimeNumber(newNum):
            return True
        else:
            return False
    else:
        return "Not a Prime Number"


print(validatePrimeNumbers(13))

def checkPrime(n):
   if n<=1:
      return False

   for i in range(2, int(n**0.5) +1): 
       if n%i == 0:
          return False
   return True

