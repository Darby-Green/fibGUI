def fib(numb):
    numb1 = 0
    numb2 = 1
    print(f"0\n1")
    while numb != 0:
        nextNumb = numb1 + numb2
        numb1 = numb2
        numb2 = nextNumb
        print(nextNumb)
        numb -= 1



