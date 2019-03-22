from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:w>/<int:h>/')
def bmi(w, h):
    height = h/100
    bmi = int(w/(height*height))
    notice = [
        'Severely underweight',
        'Underweight',
        'Normal',
        'Overweight',
        'Obese'
    ]
    if bmi < 16:
        conditional = notice[0]
    elif bmi < 18.5:
        conditional = notice[1]
    elif bmi < 25:
        conditional = notice[2]
    elif bmi < 30:
        conditional = notice[3]
    else:
        conditional = notice[4]
    
    return render_template('bmi.html', conditional=conditional)

    

if __name__ == '__main__':
  app.run(debug=True)