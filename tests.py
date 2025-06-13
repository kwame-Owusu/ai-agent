from functions.run_python import run_python_file


def test():
    result = run_python_file("calculator",  "main.py")
    print(result)

    result = run_python_file("calculator",  "tests.py")
    print(result)

    result = run_python_file("calculator",  "../main.py") #should return error
    print(result)
    
    result = run_python_file("calculator",  "nonexistent.py") #should return error
    print(result)


if __name__ == "__main__":
    test()
