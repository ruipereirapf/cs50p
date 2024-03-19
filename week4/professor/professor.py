# level 1 -> 0 a 9
# level 2 -> 10 a 99
# level 3 -> 100 a 999

import random
import sys

def main():
    level = get_level()
    i = 0
    score = 0

    while i < 10:#tem que ser 10
        n1, n2 = generate_integer(level)
        result = int(n1 + n2)
        anwser = int(input(f"{n1} + {n2} = "))
        tentativa = 1

        if anwser == result:
            i +=1
            score += 1
            continue
        else:
            while anwser != result:
                if tentativa  <= 2:
                    print("EEE")
                    anwser = int(input(f"{n1} + {n2} = "))
                    tentativa += 1
                    continue
                elif tentativa == 3:
                    print("EEE")
                    print(f"{n1} + {n2} = {result}")
                    i += 1
                    break
            continue
    else:
        print(f"Score: {score}")


def get_level():
    while True:
        level = input("Level: ")
        try:
            level = int(level)
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        n1 = random.randint(0, 9)
        n2 = random.randint(0, 9)
        return n1, n2
    elif level == 2:
        n1 = random.randint(10, 99)
        n2 = random.randint(10, 99)
        return n1, n2
    elif level == 3:
        n1 = random.randint(100, 999)
        n2 = random.randint(100, 999)
        return n1, n2



if __name__ == "__main__":
    main()