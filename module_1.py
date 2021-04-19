# Assignment 1
# Pseudocode to rewrite in Python
# Plus

# class StringCalculator
# {
#     int add(string input)
#     {
#         if (isEmpty(input))
#         {
#             return 0;
#         }
#         else
#         {
#             numbers = split(intput, ",")
#             sum = 0;
#
#             for (number in numbers)
#             {
#                 sum += getIntFrom(number);
#             }
#             return sum;
#         }
#     }
# }

class StringCalculator(object):
    def __init__(self, addends=None):
        self.addends = addends

    def addition(self):
        if self.addends is None:
            return 0
        else:
            numbers = self.addends.split(',')
            sum = 0
            for number in numbers:
                sum += int(number)
            return sum


calculator = StringCalculator().addition()
calculator2 = StringCalculator('3,2').addition()

print(calculator)
print(calculator2)


