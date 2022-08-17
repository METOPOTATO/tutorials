from distutils.log import debug
from flask import Flask
from flask_app.db import create_table
app = Flask(__name__)

def foo(num1: int, num2: int):
    """
    `foo` takes two integers and returns their sum
    
    Args:
      num1 (int): int - This is the first parameter, and it's a positional parameter.
      num2 (int): int - This is the second parameter, and it's a positional parameter.
    
    Returns:
      The sum of num1 and num2
    """
    return num1 + num2

@app.route('/', methods=['GET', 'POST'])
def index():
    # create_table()
    return "Hello Nuclear Geeks"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
