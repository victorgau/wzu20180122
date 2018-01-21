from flask import Flask, render_template, request
import random

app = Flask(__name__)

numbers = range(1, 14)
colors = ['S', 'H', 'C', 'D']

@app.route('/')
def index():
    try:
        guess = ""
        result= ""
        poker = ""
        guess = request.args.get('guess')
    except Exception as e:
        print('Error occurs:', e.args)
    
    if guess:
        color = random.choice(colors)
        number = random.choice(numbers)
        poker = color + str(number)

        if number > 7:
            if guess=='big':
                result = '你贏了！'
            else:
                result = '你輸了！'
        elif number < 7:
            if guess=='small':
                result = '你贏了！'
            else:
                result = '你輸了！'
        else:
            result = '平手！'

        return render_template('index.html', result=result, poker=poker)
    else:
        return render_template('index.html', result=result, poker=poker)

if __name__=="__main__":
    app.run(debug=True)