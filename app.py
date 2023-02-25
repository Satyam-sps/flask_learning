from flask import Flask , render_template , request , jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/math')
def mathematical_operations():
    return render_template('math.html')

@app.route('/ops',methods = ['POST'])
def operations():
    if request.method == 'POST':
        print(request.form)
        operations = request.form['Operations']
        num1 = int(request.form['Num1'])
        num2 = int(request.form['Num2'])
        if operations == 'add':
            result = num1 + num2 
            r = f"The Result of Addition of {num1} {num2} is {result}"
            

        if operations == 'sub':
            result = num1 - num2
            r = f"The Result of Subtraction of {num1} {num2} is {result}"

        if operations == 'mul':
            result = num1 * num2
            r = f"The Result of Multiplication of {num1} {num2} is {result}"
        
        if operations == 'div':
            result = num1 / num2
            r = f"The Result of Division of {num1} {num2} is {result}"

        return render_template('result.html', result = r)        
    

@app.route('/postman_api',methods = ['POST'])
def postmanoperations():
    if request.method == 'POST':
        print(request.form)
        operations = request.json['Operations']
        num1 = int(request.json['Num1'])
        num2 = int(request.json['Num2'])
        if operations == 'add':
            result = num1 + num2 
            r = f"The Result of Addition of {num1} {num2} is {result}"
            

        if operations == 'sub':
            result = num1 - num2
            r = f"The Result of Subtraction of {num1} {num2} is {result}"

        if operations == 'mul':
            result = num1 * num2
            r = f"The Result of Multiplication of {num1} {num2} is {result}"
        
        if operations == 'div':
            result = num1 / num2
            r = f"The Result of Division of {num1} {num2} is {result}"

        return jsonify(r)   

if __name__ == '__main__':
    app.run()


    