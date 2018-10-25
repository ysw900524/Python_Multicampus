# draw triangle with for

# 삼각형 1
for i in range(1, 10, 2):
    mark = "*" * i
    print(mark)


    # *
    # ***
    # *****
    # *******
    # *********


# 삼각형 2
for i in range(1, 10, 2):
    mark = " " * int((10-i)/2) + "*" * i
    print(mark)


    #     *
    #    ***
    #   *****
    #  *******
    # *********