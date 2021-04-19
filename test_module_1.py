from module_1 import StringCalculator

def testCalculator():
    calculator = StringCalculator('1,2').addition()
    assert calculator == 3