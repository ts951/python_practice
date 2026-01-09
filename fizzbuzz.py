def fizzbuzz(N):
    fizzCount = 1
    buzzCount = 1
    for i in range(1, N+1):
        if i/fizzCount == 3 and i/buzzCount == 5:
            print("fizzbuzz")
            fizzCount += 1
            buzzCount += 1
        elif i/fizzCount == 3:
            print("fizz")
            fizzCount += 1
        elif i/buzzCount == 5:
            print("buzz")
            buzzCount += 1
        else:
            print(i)

fizzbuzz(50)