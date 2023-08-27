from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form['data']
        print(request.headers)
        print(data)
        dosyayaYaz(data)
        return  'data dosyaya kaydedildi.'
    else:
        print("test")
        return render_template('index.html')
    
def dosyayaYaz(data):
    with open("data.json", "a") as file:
        file.truncate(0)
        file.write("[\""+data + "\"]\n")
        file.close()    

if __name__ == '__main__':
    app.run(debug=True)