def multiply_student(*numbers,**student):
    numb = 1
    for w in numbers:
        numb*=w
        print(numb)
    print(f"Hello {student}")
    