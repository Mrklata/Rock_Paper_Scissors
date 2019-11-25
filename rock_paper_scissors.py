from random import randint


class Points:
    def __init__(self):
        self.lst = [1, 2, 3, 1, 2, 3]

    @staticmethod
    def rps():
        lst = [1, 2, 3]
        system_obj = lst[randint(0, 2)]
        return system_obj


def main():
    points = Points()
    check(points)


def check(points):
    system_obj = points.rps()
    user_obj = int(input("\"1\" for paper \n\"2\" for rock \n\"3\" for scissors") or 4)
    x = ["paper", "rock", "scissors"]
    print(f"System chosen {x[system_obj - 1]}")
    if user_obj in [1, 2, 3]:
        if system_obj == user_obj:
            print("Tie!!!")
        elif points.lst[system_obj + 1] == points.lst[user_obj]:
            print("You lost!!!")
        else:
            print("You won!!!")
    else:
        print("Don't cheat ;)")
    check(points)


if __name__ == '__main__':
    main()
