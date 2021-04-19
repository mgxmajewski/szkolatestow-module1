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
#             result = 0;
#
#             for (number in numbers)
#             {
#                 result += getIntFrom(number);
#             }
#             return result;
#         }
#     }
# }

class StringCalculator(object):
    def __init__(self, addends):
        self.addends = addends

    def addition(self):
        if self.addends is None:
            return 0
        else:
            numbers = self.addends.split(',')
            result = 0
            for number in numbers:
                result += int(number)
            return result


calculator = StringCalculator('1,2').addition()

print(calculator)


