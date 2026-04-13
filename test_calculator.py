from calculator import Calculator

calc = Calculator()

def test_add(): 
	result = calc.add(10, 5)
	print(f"Add Result: {result}")
	assert result == 15

def test_subtract(): 
	result = calc.subtract(12, 6)
	print(f"Subtract Result: {result}")
	assert result == 6

def test_multiply(): 
	result = calc.multiply(3, 4)
	print(f"Multiply Result: {result}")
	assert result == 12

def test_divide():
	result = calc.divide(18, 2)
	print(f"Divide Result: {result}")
	assert result == 9
