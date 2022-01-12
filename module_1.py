class StringCalculator(object):
    def __init__(self, addends=None):
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


