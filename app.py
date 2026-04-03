from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name1 = request.form['name1']
    desc1 = request.form['desc1']
    name2 = request.form['name2']
    desc2 = request.form['desc2']
    # Add your FLAMES logic here
    return render_template('result.html', name1=name1, name2=name2)

if __name__ == '__main__':
    app.run(debug=True)
