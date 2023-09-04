class Calculator:

    def __init__(self):
        self.total = 0.0
        self.history = []

    @staticmethod
    def main():
        calc = Calculator()

        # Main loop to continuously take user inputs
        while True:
            command = input("> ")
            if command == "exit":
                break
            print(calc.execute(command))

    def _handle_precision(self, value):
        """
        Handle precision of float numbers to avoid common floating point inaccuracies.
        This function will round to 10 decimal places.
        """
        return round(value, 10)

    def add(self, value):
        self.total = self._handle_precision(self.total + value)
        self.history.append(("add", value))
        return self.total

    def subtract(self, value):
        self.total = self._handle_precision(self.total - value)
        self.history.append(("subtract", value))
        return self.total
    
    def divide(self, value):
        if value == 0:
            return "Division by zero is not allowed!"
        self.total /= value
        self.total = self._handle_precision(self.total)
        self.history.append(("divide", value))
        return self.total

    def multiply(self, value):
        self.total = self._handle_precision(self.total * value)
        self.history.append(("multiply", value))
        return self.total

    def repeat(self, n):
        """
        Repeats the last 'n' operations.
        For each operation, reconstruct the command string and then execute it.
        """
        for operation, *values in self.history[-n:]: # take only the last 'n' commands
            self.execute(f"{operation} {' '.join(map(str, values))}")
        return self.total

    def neg(self):
        self.total = self._handle_precision(-self.total)
        self.history.append(("neg",))
        return self.total

    def abs(self):
        self.total = self._handle_precision(abs(self.total))
        self.history.append(("abs",))
        return self.total

    def sqr(self):
        self.total = self._handle_precision(self.total ** 2)
        self.history.append(("sqr",))
        return self.total

    def sqrt(self):
        self.total = self._handle_precision(self.total ** 0.5)
        self.history.append(("sqrt",))
        return self.total

    def cube(self):
        self.total = self._handle_precision(self.total ** 3)
        self.history.append(("cube",))
        return self.total

    def cubert(self):
        if self.total < 0:
            self.total = self._handle_precision(-abs(self.total) ** (1/3))
        else:
            self.total = self._handle_precision(self.total ** (1/3))
        self.history.append(("cubert",))
        return self.total
    
    def cancel(self):
        self.total = 0.0
        self.history.clear()
        return self.total
    
    def execute(self, command):
        # Split the command and initialize default values
        parts = command.split()
        operation = parts[0]
        value = None if len(parts) < 2 else parts[1]

        # Dictionary to map commands to their functions
        operations_map = {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide,
            'repeat': self.repeat,
            'neg': self.neg,
            'abs': self.abs,
            'sqr': self.sqr,
            'sqrt': self.sqrt,
            'cube': self.cube,
            'cubert': self.cubert,
            'cancel': self.cancel
        }

        # Validate the command
        if operation not in operations_map:
            return f"Unrecognized command: {operation}"

        if not value and operation in ['add', 'subtract', 'multiply', 'divide', 'repeat']:
            return f"'{operation}' command requires a numeric value."

        if value and operation in ['neg', 'abs', 'sqr', 'sqrt', 'cube', 'cubert', 'cancel']:
            return f"'{operation}' command doesn't accept a value."

        try:
            if operation in ['add', 'subtract', 'multiply', 'divide']:
                value = float(value)
            elif operation == 'repeat':
                value = int(value)
            
            if value is not None:
                return operations_map[operation](value)
            else:
                return operations_map[operation]()

        except ValueError:
            return f"You must input numbers for the '{operation}' operation."
        except Exception as e:
            return f"Error executing command: {e}"

    def __repr__(self):
        return str(self.total)
    
if __name__ == "__main__":
    # When this script is run directly, it will first run unit tests and then start the calculator
    import unittest

    # Load tests from the current directory matching 'calculator_test.py'
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('.', pattern='calculator_test.py')
    
    # Run the tests
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
    
    # Start the main calculator interface
    Calculator.main()
