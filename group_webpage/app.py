import timeit
from flask import Flask, render_template, request, jsonify
from exponential_search import exponential_search, exponential_search_wrapper
from binary_search import binary_search, binary_search_wrapper
from interpolation_search import interpolation_search, interpolation_search_wrapper
from jump_search import jump_search, jump_search_wrapper
from linear_search import linear_search, linear_search_wrapper
from ternary_search import ternary_search, ternary_search_wrapper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def work():
    return render_template('works.html')

@app.route('/contacts')
def contact():
    return render_template('contacts.html')

@app.route('/searchalgo', methods=["GET", 'POST'])
def searchalgo():
    numbers = range(1, 1001)
    test_data = ", ".join(map(str, numbers))

    if request.method == "POST":
        array_str = request.form.get("array")
        target_str = request.form.get("target")
        search_type = request.form.get("search_type")

        try:
            array = list(map(int, array_str.split(",")))
            target = int(target_str)
            low, high = 0, len(array) - 1

            result = -1  # Initialize result before the conditional statements
            execution_time = 0  # Initialize execution_time

            if search_type == "exponential":
                execution_time = timeit.timeit("exponential_search_wrapper(exponential_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000 
                result = exponential_search_wrapper(binary_search, array, target)
            elif search_type == "binary":
                execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000 
                result = binary_search_wrapper(binary_search, array, target)
            elif search_type == "interpolation":
                execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000 
                result = interpolation_search_wrapper(interpolation_search, array, target)                
            elif search_type == "jump":
                execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000 
                result = jump_search_wrapper(interpolation_search, array, target)  
            elif search_type == "linear":
                execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000 
                result = linear_search_wrapper(linear_search, array, target)  
            elif search_type == "ternary":
                execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)", globals={**globals(), "array": array, "target": target, "low": low, "high": high}, number=1) * 1000 
                result = ternary_search_wrapper(ternary_search, array, target, low, high)  

            return render_template("searchalgo.html", result=result, search_type=search_type, execution_time=execution_time, test_data=test_data)
        except ValueError:
            return render_template("searchalgo.html", error="Invalid input. Ensure the array and target are integers.")

    return render_template('searchalgo.html', test_data=test_data)


if __name__ == "__main__":
    app.run(debug=True)
