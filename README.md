# Calculator Application

## Features
- **Basic Operations**: Supports addition, subtraction, multiplication, and division.
- **Advanced Operations**: Square, square root, cube, cube root, negate, and absolute value.
- **History Mechanism**: Maintains a history of operations that can be invoked to repeat previous operations.
- **Error Handling**: Handles common calculation errors, such as division by zero, gracefully.
- **Precision Control**: Results are rounded to 10 decimal places to avoid common floating-point inaccuracies.

## Usage

To run the calculator:
```
$ python calculator.py
```

**Commands**:
- `add [value]`: Adds the value to the current total.
- `subtract [value]`: Subtracts the value from the current total.
- `multiply [value]`: Multiplies the current total by the value.
- `divide [value]`: Divides the current total by the value.
- `sqr`: Squares the current total.
- `sqrt`: Takes the square root of the current total.
- `cube`: Cubes the current total.
- `cubert`: Takes the cube root of the current total. Returns the real cube root for negative numbers.
- `neg`: Negates the current total.
- `abs`: Returns the absolute value of the current total.
- `repeat [n]`: Repeats the last `n` operations.
- `cancel`: Resets the calculator to zero and clears history.
- `exit`: Exits the calculator.

## Testing

Unit tests have been provided in the file `calculator_test.py`

To run the tests:
```
$ python calculator_test.py
```
