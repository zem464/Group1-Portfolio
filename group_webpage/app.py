import timeit
from flask import Flask, send_file, render_template, request, jsonify
from exponential_search import exponential_search, exponential_search_wrapper
from binary_search import binary_search, binary_search_wrapper
from interpolation_search import interpolation_search, interpolation_search_wrapper
from jump_search import jump_search, jump_search_wrapper
from linear_search import linear_search, linear_search_wrapper
from ternary_search import ternary_search, ternary_search_wrapper
from infix_postfix import Stack
from queue_dequeue import Queue_Deque
from hash import HashTable
from graph import Graph

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

@app.route('/lab3')
def lab3():
    return render_template('lab3.html')

@app.route('/graph')
def graph():
    return render_template('graph.html')

@app.route('/searchalgoindex')
def searchalgo():
    return render_template('searchalgo.html')

@app.route('/searchalgo1', methods=["GET", 'POST'])
def searchalgo1():
    numbers = range(1, 101)
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
                result = exponential_search_wrapper(exponential_search, array, target)
            elif search_type == "binary":
                execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000 
                result = binary_search_wrapper(binary_search, array, target)
            elif search_type == "interpolation":
                execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000 
                result = interpolation_search_wrapper(jump_search, array, target)                
            elif search_type == "jump":
                execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000 
                result = jump_search_wrapper(interpolation_search, array, target)  
            elif search_type == "linear":
                execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000 
                result = linear_search_wrapper(linear_search, array, target)  
            elif search_type == "ternary":
                execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)", globals={**globals(), "array": array, "target": target, "low": low, "high": high}, number=1) * 1000 
                result = ternary_search_wrapper(ternary_search, array, target, low, high)  

            return render_template("searchalgo1.html", result=result, search_type=search_type, execution_time=execution_time, test_data=test_data)
        except ValueError:
            return render_template("searchalgo1.html", error="Invalid input. Ensure the array and target are integers.")

    return render_template('searchalgo1.html', test_data=test_data)


@app.route('/searchalgo2', methods=["GET", 'POST'])
def searchalgo2():
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
                result = exponential_search_wrapper(exponential_search, array, target)
            elif search_type == "binary":
                execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000 
                result = binary_search_wrapper(binary_search, array, target)
            elif search_type == "interpolation":
                execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000 
                result = interpolation_search_wrapper(jump_search, array, target)                
            elif search_type == "jump":
                execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000 
                result = jump_search_wrapper(interpolation_search, array, target)  
            elif search_type == "linear":
                execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000 
                result = linear_search_wrapper(linear_search, array, target)  
            elif search_type == "ternary":
                execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)", globals={**globals(), "array": array, "target": target, "low": low, "high": high}, number=1) * 1000 
                result = ternary_search_wrapper(ternary_search, array, target, low, high)  

            return render_template("searchalgo2.html", result=result, search_type=search_type, execution_time=execution_time, test_data=test_data)
        except ValueError:
            return render_template("searchalgo2.html", error="Invalid input. Ensure the array and target are integers.")

    return render_template('searchalgo2.html', test_data=test_data)

@app.route('/searchalgo3', methods=["GET", 'POST'])
def searchalgo3():
    numbers = range(1, 10001)
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
                result = exponential_search_wrapper(exponential_search, array, target)
            elif search_type == "binary":
                execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000 
                result = binary_search_wrapper(binary_search, array, target)
            elif search_type == "interpolation":
                execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000 
                result = interpolation_search_wrapper(jump_search, array, target)                
            elif search_type == "jump":
                execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000 
                result = jump_search_wrapper(interpolation_search, array, target)  
            elif search_type == "linear":
                execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000 
                result = linear_search_wrapper(linear_search, array, target)  
            elif search_type == "ternary":
                execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)", globals={**globals(), "array": array, "target": target, "low": low, "high": high}, number=1) * 1000 
                result = ternary_search_wrapper(ternary_search, array, target, low, high)  

            return render_template("searchalgo3.html", result=result, search_type=search_type, execution_time=execution_time, test_data=test_data)
        except ValueError:
            return render_template("searchalgo3.html", error="Invalid input. Ensure the array and target are integers.")

    return render_template('searchalgo3.html', test_data=test_data)

@app.route('/infix_postfix', methods=["GET", 'POST'])
def if_pf():
    result = None
    steps = []
    stack = Stack()
    infix_expression = ''

    if request.method == 'POST':
        infix_expression = request.form.get('infixInput', '')
        result, steps = stack.infix_to_postfix_step_by_step(infix_expression)

    return render_template('infix_postfix.html', result=result, steps=steps, infix_expression=infix_expression)

@app.route('/download')
def download_file():
    p = "results\Group 1-Search_Algorithms.pdf"
    return send_file(p, as_attachment=True)

@app.route('/queue_dequeue_front')
def queue_dequeue_front():
    return render_template('queue_dequeue_front.html')

qdq = Queue_Deque()
@app.route('/queue', methods=['GET', 'POST'])
def queue():
    result = None
    
    if request.method == 'POST':
        input_val = request.form.get('inputEnqueue', '')

        if input_val == 'ENQUEUE':
            x = request.form.get('enqueueValue', '')
            qdq.push_back(x)
            result = f"Enqueued {x} into the queue."
        elif input_val == 'DEQUEUE':
            dequeued_data = qdq.pop_front()
            if dequeued_data is not None:
                result = f"Dequeued {dequeued_data} from the queue."
    
    return render_template('queue.html', result=result, queue_elements=qdq.get_elements())

qdq = Queue_Deque()
@app.route('/deque', methods=['GET', 'POST'])
def deque():
    result = None
    
    if request.method == 'POST':
        input_val = request.form.get('inputEnqueue', '')

        if input_val == 'ADD FRONT':
            x = request.form.get('enqueueValue', '')
            qdq.push_front(x)
            result = f"Enqueued {x} at the front of the deque."
            
        elif input_val == 'ADD BACK':
            x = request.form.get('enqueueValue', '')
            qdq.push_back(x)
            result = f"Enqueued {x} at the end of the queue."
            
        elif input_val == 'DELETE FRONT':
            dequeued_data = qdq.pop_front()
            if dequeued_data is not None:
                result = f"Dequeued {dequeued_data} from the queue."
            
        elif input_val == 'DELETE BACK':
            dequeued_data = qdq.pop_back()
            if dequeued_data is not None:
                result = f"Dequeued {dequeued_data} from the queue."
            
    return render_template('deque.html', result=result, deque_elements=qdq.get_elements())

qdq = Queue_Deque()
@app.route('/queue_deque-IR', methods=['GET', 'POST'])
def queue_deque_IR():
    resultI = None
    
    if request.method == 'POST':
        input_valI = request.form.get('inputIR', '')
        if input_valI == "ENQUEUE-fI":
            x = request.form.get('enqueueValueI', '')
            qdq.push_front(x)
            resultI = f"Enqueued {x} into the front of the deque."
        elif input_valI == "DEQUEUE-fI":
            resultI = f"Dequeued from the front of the deque: {qdq.pop_front()}"
        elif input_valI == "DEQUEUE-rI":
            resultI = f"Dequeued from the rear of the deque: {qdq.pop_back()}"

    return render_template('queue_deque-IR.html', resultI=resultI, queue_elementsI=qdq.get_elements())

qdq = Queue_Deque()
@app.route('/queue_deque-OR', methods=['GET', 'POST'])
def queue_deque_OR():
    resultO = None

    if request.method == 'POST':        
        input_valO = request.form.get('inputOR', '')

        if input_valO == "ENQUEUE-fO":
            x = request.form.get('enqueueValueO', '')
            qdq.push_front(x)
            resultO = f"Enqueued {x} into the front of the deque."
        elif input_valO == "ENQUEUE-rO":
            x = request.form.get('enqueueValueO', '')
            qdq.push_back(x)
            resultO = f"Enqueued {x} into the rear of the deque."
        elif input_valO == "DEQUEUE-fO":
            resultO = f"Dequeued from the front of the deque: {qdq.pop_front()}"
    
    return render_template('queue_deque-OR.html', resultO=resultO, queue_elementsO=qdq.get_elements())

@app.route('/hash', methods=['GET', 'POST'])
def hash():
    result = None
    error = None
    ht = HashTable()

    if request.method == 'POST':
        function = request.form.get('function')
        commands = int(request.form.get('inputComm'))
        key = request.form.get('inputKey')
        key_list = key.split('\r\n')

        try:
            num_commands = int(commands)
            if num_commands < 1:
                raise ValueError("Input is less than 1. Please use an integer greater than or equal to 1.")

            hash_functions = {
                "Division": ht.hash_function_1,
                "Multi": ht.hash_function_2,
                "Default": ht.hash_function_3,
            }

            if function not in hash_functions:
                raise ValueError("Invalid hash function selected.")

            ht.process_command(key_list, hash_functions[function])
            result = ht.display()
            deleted_items = ht.deleted_items
        except ValueError as e:
            error = str(e)

        return render_template('hash.html', function=function, commands=commands, result=result, key=key, error=error, ht=ht, deleted_items=deleted_items)

    return render_template('hash.html', function=None, commands=None, result=result, key=None, error=error, ht=ht)

@app.route('/shortest_path_input', methods=['GET', 'POST'])
def shortest_path_input():
    g = Graph()
    shortest_path = None
    error = None
    distance = None

    g.add_vertex('Antipolo')
    g.add_vertex('Marikina')
    g.add_vertex('Santolan')
    g.add_vertex('Katipunan')
    g.add_vertex('Anonas')
    g.add_vertex('Araneta-Cubao LRT 2')
    g.add_vertex('Betty Go Belmonte')
    g.add_vertex('Gilmore')
    g.add_vertex('J. Ruiz')
    g.add_vertex('V. Mapa')
    g.add_vertex('Pureza')
    g.add_vertex('Legarda')
    g.add_vertex('Recto')

    g.add_vertex('Baclaran')
    g.add_vertex('EDSA LRT 1')
    g.add_vertex('Libertad')
    g.add_vertex('Gil Puyat')
    g.add_vertex('Vito Cruz')
    g.add_vertex('Quirino')
    g.add_vertex('Pedro Gil')
    g.add_vertex('United Nations Avenue')
    g.add_vertex('Central Terminal')
    g.add_vertex('Carriedo')
    g.add_vertex('Doroteo Jose')
    g.add_vertex('Bambang')
    g.add_vertex('Tayuman')
    g.add_vertex('Blumentritt')
    g.add_vertex('Abad Santos')
    g.add_vertex('R. Papa')
    g.add_vertex('5th Avenue')
    g.add_vertex('Monumento')
    g.add_vertex('Balintawak')
    g.add_vertex('Roosevelt')

    g.add_vertex('North Avenue')
    g.add_vertex('Quezon Avenue')
    g.add_vertex('GMA Kamuning')
    g.add_vertex('Araneta-Cubao MRT 3')
    g.add_vertex('Santolan-Anapolis')
    g.add_vertex('Ortigas')
    g.add_vertex('Shaw')
    g.add_vertex('Boni')
    g.add_vertex('Guadalupe')
    g.add_vertex('Buendia')
    g.add_vertex('Ayala')
    g.add_vertex('Magallanes')
    g.add_vertex('Taft')

    # Line 2
    g.add_edge("Recto", "Legarda", 1.05)
    g.add_edge("Legarda", "Pureza", 1.389)
    g.add_edge('Recto', 'Legarda', 1.05)
    g.add_edge('Legarda', 'Pureza', 1.389)
    g.add_edge('Pureza', 'V. Mapa', 1.357)
    g.add_edge('V. Mapa', 'J. Ruiz', 1.234)
    g.add_edge('J. Ruiz', 'Gilmore', 0.928)
    g.add_edge('Gilmore', 'Betty Go', 1.075)
    g.add_edge('Betty Go', 'Cubao LRT Line', 1.164)
    g.add_edge('Cubao LRT Line', 'Anonas', 1.438)
    g.add_edge('Anonas', 'Katipunan', 0.955)
    g.add_edge('Katipunan', 'Santolan', 1.97)
    g.add_edge('Santolan', 'Marikina Pasig', 1.66)
    g.add_edge('Marikina Pasig', 'Antipolo', 2.35)

    # Line 1
    g.add_edge('Baclaran', 'Edsa', 0.588)
    g.add_edge('Edsa', 'Libertad', 1.01)
    g.add_edge('Libertad', 'Gil Puyat', 0.73)
    g.add_edge('Gil Puyat', 'Vito Cruz', 1.061)
    g.add_edge('Vito Cruz', 'Quirino', 0.827)
    g.add_edge('Quirino', 'Pedro Gil', 0.794)
    g.add_edge('Pedro Gil', 'United Nations Avenue', 0.754)
    g.add_edge('United Nations Avenue', 'Central Terminal', 1.214)
    g.add_edge('Central Terminal', 'Carriedo', 0.725)
    g.add_edge('Carriedo', 'Doroteo Jose', 0.685)
    g.add_edge('Doroteo Jose', 'Recto', 0.352)
    g.add_edge('Doroteo Jose', 'Bambang', 0.648)
    g.add_edge('Bambang', 'Tayuman', 0.618)
    g.add_edge('Tayuman', 'Blumentritt', 0.671)
    g.add_edge('Blumentritt', 'Abad Santos', 0.927)
    g.add_edge('Abad Santos', 'R. Papa', 0.66)
    g.add_edge('R. Papa', '5th Avenue', 0.954)
    g.add_edge('5th Avenue', 'Monumento', 1.087)
    g.add_edge('Monumento', 'Balintawak', 2.25)
    g.add_edge('Roosevelt', 'Balintawak', 1.42)


    # MRT
    g.add_edge('North Ave', 'Quezon Ave', 0.936)
    g.add_edge('Quezon Ave', 'GMAKamuning', 1.951)
    g.add_edge('GMAKamuning', 'Cubao MRT Line', 1.405)
    g.add_edge('Cubao MRT Line', 'Cubao LRT Line', 0.551)
    g.add_edge('Cubao MRT Line', 'Santolan-Annapolis', 2.334)
    g.add_edge('Santolan-Annapolis', 'Ortigas', 0.797)
    g.add_edge('Ortigas', 'Shaw Boulevard', 0.988)
    g.add_edge('Shaw Boulevard', 'Boni', 0.83)
    g.add_edge('Boni', 'Guadalupe', 1.924)
    g.add_edge('Guadalupe', 'Buendia', 0.886)
    g.add_edge('Buendia', 'Ayala', 1.201)
    g.add_edge('Ayala', 'Magallanes', 1.941)
    g.add_edge('Magallanes', 'Taft Ave', 0.131)
    g.add_edge('Taft Ave', 'Edsa', 0.289)


    if request.method == 'POST':
        start_station = request.form.get('start_station', '')
        end_station = request.form.get('end_station', '')

        try:
            if start_station in g.get_vertices() or end_station in g.get_vertices():
                alternate_routes = g.alternate_routes(start_station, end_station)
                
            shortest_path = g.print_shortest_route(alternate_routes)
            distance = g.print_shortest_route_distance(alternate_routes)

            return render_template('graph.html', start_station=start_station, end_station=end_station, shortest_path=shortest_path, distance=distance)

        except KeyError as e:
            error = str(e)

    # Pass the vertices to the template for autocomplete
    vertices = g.get_vertices()
    return render_template('graph.html', start_station=start_station, end_station=end_station, shortest_path=shortest_path, error=error, vertices=vertices)

@app.route('/sort')
def sorting():
    return render_template('sort_front.html')

@app.route("/bubblesort", methods=["GET"])
def bubblesort():
    return render_template("bubble.html")

@app.route("/mergesort", methods=["GET"])
def mergesort():
    return render_template("merge_sort.html")

@app.route("/insertionsort", methods=["GET"])
def insertionsort():
    return render_template("insertion.html")

@app.route("/selectionsort", methods=["GET"])
def selectionsort():
    return render_template("selection.html")

@app.route("/quick_sort", methods=["GET"])
def quick_sort():
    return render_template("quick_sort.html")

@app.route('/download_sort')
def download_sort():
    p = "results\Group 1-Sorting_Algorithms.pdf"
    return send_file(p, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
    