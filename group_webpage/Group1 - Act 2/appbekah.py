"""@app.route('/infix_postfix', methods=["GET", 'POST'])
def if_pf():
    result = None
    if request.method == 'POST':
        infix = request.form.get('alphanumericInput', '')
        result = stack.infix_to_postfix_step_by_step(infix)
    return render_template('infix_postfix.html', result=result)

@app.route('/infix_postfix', methods=["GET", 'POST'])
def if_pf():
    result = None
    infix_expression = None

    if request.method == 'POST':
        infix_expression = request.form.get('alphanumericInput', '')
        result = stack.infix_to_postfix_step_by_step(infix_expression)

    return render_template('infix_postfix.html', result=result, infix_expression=infix_expression)"""

@app.route('/infix_postfix', methods=["GET", 'POST'])
def if_pf():
    result = None
    steps = []  # New list to store steps
    if request.method == 'POST':
        infix = request.form.get('alphanumericInput', '')
        steps = stack.infix_to_postfix_step_by_step(infix)
        result = steps[-1]  # Set result to the final postfix expression
    return render_template('infix_postfix.html', infix=infix, result=result, steps=steps)