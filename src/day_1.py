def fizzbuzz(n: int) -> None:
    """
    O(n), or close to O(log(n) * n) with the check statement of Python
    """
    for i in range(n):
        if (i % 3 == 0) & (i % 5 ==0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    fizzbuzz(100)