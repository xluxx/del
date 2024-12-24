from fake_math import divide
from true_math import divide1

if __name__ == "__main__":
    result1 = divide(69, 3)
    result2 = divide(3, 0)
    result3 = divide1(49, 7)
    result4 = divide1(15, 0)

    print(result1)
    print(result2)
    print(result3)
    print(result4)
