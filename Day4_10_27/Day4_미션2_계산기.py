class Calculator:
    answer = float()
    input_list = list()
    def add(self):
        for i in range(len(self.input_list)):
            self.input_list[i] += self.input_list[i+1]
            print(self.input_list)
    # def minus(self):
    #
    # def mutiple(self):
    #
    # def divide(self):

mycal = Calculator()
answer1 = Calculator.add([1, 2, 3, 4, 5])
print(answer1)