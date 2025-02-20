from flask import Flask,render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#creamos una ruta que solo es accesible por post (si la escribimos directamente en el navegador nos dara error)
@app.route('/calcular', methods=['POST'])
def calculo():
    data = {
        
        "dia": int(request.form.get("dia", 0)),  # Convertir a entero
        "mes": int(request.form.get("mes", 0)),  # Convertir a entero    
    }

    
    resp1= None
    if (data["mes"] == 12 and data["dia"] in range(22, 32)) or (data["mes"] == 1 and data["dia"] in range(1, 20)):
            resp1 = "Tu signo Zodiacal es Capricornio"
    elif (data["mes"] == 1 and data["dia"] in range(20, 32)) or (data["mes"] == 2 and data["dia"] in range(1, 19)):
        resp1 = "Tu signo Zodiacal es Acuario"
    elif (data["mes"] == 2 and data["dia"] in range(19, 30)) or (data["mes"] == 3 and data["dia"] in range(1, 21)):
        resp1 = "Tu signo Zodiacal es Piscis"
    elif (data["mes"] == 3 and data["dia"] in range(21, 32)) or (data["mes"] == 4 and data["dia"] in range(1, 20)):
        resp1 = "Tu signo Zodiacal es Aries"
    elif (data["mes"] == 4 and data["dia"] in range(20, 31)) or (data["mes"] == 5 and data["dia"] in range(1, 21)):
        resp1 = "Tu signo Zodiacal es Tauro"
    elif (data["mes"] == 5 and data["dia"] in range(21, 32)) or (data["mes"] == 6 and data["dia"] in range(1, 21)):
        resp1 = "Tu signo Zodiacal es Géminis"
    elif (data["mes"] == 6 and data["dia"] in range(21, 31)) or (data["mes"] == 7 and data["dia"] in range(1, 23)):
        resp1 = "Tu signo Zodiacal es Cáncer"
    elif (data["mes"] == 7 and data["dia"] in range(23, 32)) or (data["mes"] == 8 and data["dia"] in range(1, 23)):
        resp1 = "Tu signo Zodiacal es Leo"
    elif (data["mes"] == 8 and data["dia"] in range(23, 32)) or (data["mes"] == 9 and data["dia"] in range(1, 23)):
        resp1 = "Tu signo Zodiacal es Virgo"
    elif (data["mes"] == 9 and data["dia"] in range(23, 31)) or (data["mes"] == 10 and data["dia"] in range(1, 23)):
        resp1 = "Tu signo Zodiacal es Libra"
    elif (data["mes"] == 10 and data["dia"] in range(23, 32)) or (data["mes"] == 11 and data["dia"] in range(1, 22)):
        resp1 = "Tu signo Zodiacal es Escorpio"
    elif (data["mes"] == 11 and data["dia"] in range(22, 31)) or (data["mes"] == 12 and data["dia"] in range(1, 22)):
        resp1 = "Tu signo Zodiacal es Sagitario"
    
    return render_template('calculo.html', resp=resp1)