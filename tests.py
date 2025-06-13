from functions.run_python import run_python_file


def test():
    result = run_python_file("calculator",  "main.py")
    print(result)


if __name__ == "__main__":
    test()
