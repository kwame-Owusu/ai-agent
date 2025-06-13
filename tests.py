from functions.run_python import run_python


def test():
    result = run_python("calculator",  "main.py")
    print(result)


if __name__ == "__main__":
    test()
