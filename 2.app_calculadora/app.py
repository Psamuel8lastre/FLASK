from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET','POST'])
def aritmetica():
    if request.method == "POST":
        num1 = float(request.form.get('n1'))
        num2 = float(request.form.get('n2'))
        
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2
        return render_template('index.html',total_suma=suma,
                                            total_resta=resta,
                                            total_multiplicacion=multiplicacion,
                                            total_division=division)
    return render_template('index.html')

@app.route('/divisas', methods=['GET','POST'])
def divisas():
    if request.method == "POST":
        
        dolar = 4.402
        
        num1 = float(request.form.get('d1'))
        divisa_dolar = num1 * dolar
        
        

        return render_template('divisa.html',
                                total_pesos = divisa_dolar)
    return render_template('divisa.html')





if __name__ == "__main__":
    app.run(debug=True)
        
        
