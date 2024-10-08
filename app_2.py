from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])  #to render home page
def home_page():
    return render_template('home.html')

@app.route('/math', methods=['POST'])   #this will be called from UI
def math_operation():
    if(request.method == 'POST'):
        operation=request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if(operation=='add'):
            r = num1 + num2
            result = 'the sum of ' + str(num1) = ' and ' + str(num2)  + ' is ' + str(r)
        

        return render_template('results.html', result = result)

if __name__ == '__main__':
    app.run(debug=True)