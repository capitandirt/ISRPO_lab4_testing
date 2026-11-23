import rectangle

def RunTests():
    failed_tests = 0
    #area tests
    small_values = rectangle.area(6,7)
    if small_values != 42:
        print("Failed test small_values")
        failed_tests += 1
    big_values = rectangle.area(2**32, 2**32)
    if big_values != 2**64:
        print("Failed test big_values")
        failed_tests += 1
    small_values = rectangle.perimeter(6,7)
    if small_values != 26:
        print("Failed test small_values perimeter")
        failed_tests += 1
    big_values = rectangle.perimeter(2**32, 2**32)
    if big_values != 2**34:
        print("Failed test big_values perimeter")
        failed_tests += 1
    print("Complete testing. Failed ", failed_tests, " tests.")
    
RunTests()