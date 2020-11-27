from flask import Flask, render_template, url_for, request
from math import sin, cos, tan, sqrt, exp, log, acosh, asinh, atanh, asin, acos

app = Flask(__name__)
my_list_simple = []
my_list_advanced = []
@app.route('/')
def main():
    return render_template('index.html',home=True)

@app.route("/advanced")
def advanced():
    my_list_advanced = []
    return render_template("advanced.html")


@app.route("/simple")
def simple():
    my_list_simple = []
    #my_list_advanced = []
    return render_template("simple.html")

# @app.route("/clearSimplehistory", methods=["get"])
# def clearSimpleHistory():
#     #my_list_simple = []
#     return render_template("simple.html")


# @app.route("/clearAdvancedhistory", methods=["get"])
# def clearAdvancedHistory():
#     #my_list_advanced = []
#     return render_template("advanced.html")


@app.route("/calculate", methods=["post"])
def calculate():
    #request.method
    first_number = int(request.form["firstNumber"])
    operation = request.form["operation"]
    second_number = int(request.form["secondNumber"])
    note = ""
    color = "alert-success"
    if operation == "plus":
        result = first_number + second_number
        note = "Addition was performed successfully"
    elif operation == "minus":
        result = first_number - second_number
        note = "Subtraction was performed successfully"
    elif operation == "multiply":
        result = first_number * second_number
        note = "Multiplication was perfromed successfully"
    elif operation == "divide":
        result = first_number / second_number
        note = "Division was performed successfully"
    else:
        note = "There is an error, please try again"
        color = "alert-warning"
        return render_template("simple.html", note=note, color=color)

    if operation == 'plus':
        operation = '+'
    elif operation == 'minus':
        operation = '-'
    elif operation == 'multiply':
        operation = '*'
    elif operation == 'divide':
        operation = '/'
    
    store = str(first_number) + operation + str(second_number) + ' = '+str(result)
    if len(my_list_simple) >= 10:
        my_list_simple.pop()
    my_list_simple.insert(0, store)
    
    return render_template("simple.html",result=result, note=note, color=color, list = my_list_simple)


@app.route("/calculate_advanced", methods=["post"])
def calculate_advanced():
    first_number = int(request.form["firstNumber"])
    operation = request.form["operation"]
    color="alert-success"
    note=""
    if operation == "sin":
        result = sin(first_number)
        note="sin has been calculated"
    elif operation == "cos":
        result = cos(first_number)
        note="cosine has been calculated"
    elif operation == "tan":
        result = tan(first_number)
        note="tan has been calculated"
    elif operation == "log":
        result = log(first_number)
        note="log of a number has been calculated"
    elif operation == "exp":
        result = exp(first_number)
        note = "exp has been calculated"
    elif operation == "squr":
        result = sqrt(first_number)
        note = "square root has been calculated"
    else:
        note="no function has been selected"
        color="alert-danger"
        return render_template("advanced.html", note=note, color=color)

    if operation == 'sin':
        operation = 'sin'
    elif operation == 'cos':
        operation = 'cos'
    elif operation == 'tan':
        operation = 'tan'
    elif operation == 'log':
        operation = 'log'
    elif operation == 'exp':
        operation = 'exp'
    elif operation == 'squr':
        operation = 'sqrt'
    
    store = operation + '(' + str(first_number) + ')' + ' = ' + str(result)
    if len(my_list_advanced) >= 10:
        my_list_advanced.pop()
    my_list_advanced.insert(0, store)

    return render_template("advanced.html",result=result, note=note, color=color, list=my_list_advanced)


if __name__ == "__main__":
    app.run(debug=True)


