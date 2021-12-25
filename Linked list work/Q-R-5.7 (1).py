def findRepeated(Arr=[], n=2):
    sum_numbers = 0
    sum_square = 0
    for i in Arr:
        sum_numbers = sum_numbers + i       # TOTAL OF NUMBERS
        sum_square = sum_square + i * i     # TOTAL OF NUMBER^2

    x = (n * (n - 1)) / 2
    y = (n * (n - 1) * (2 * n - 1)) / 6
    A = x - sum_numbers
    B = (y - sum_square) / A
    print("The number it was replaced with is",(B - A) / 2)
    print("The number which was removed is: ", (B - A) / 2)


findRepeated([1, 3, 2, 3, 4, 5], 6)
findRepeated([0, 1, 1, 2, 3, 5], 6)