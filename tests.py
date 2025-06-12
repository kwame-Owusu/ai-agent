from functions.write_file  import write_file

def test():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet") #creating a dir that does not exist and writing to it
    print(result)

    result = write_file("calculator", "/temp/temp.txt", "this should not be allowed")
    print(result)


if __name__ == "__main__":
    test()
