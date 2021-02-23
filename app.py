from flask import Flask, render_template, url_for, request, redirect, abort, flash, jsonify, session, make_response
import biasChecker


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == 'POST':
    
        try:
            jobInput2 = request.form['jobInput2']

            bias, words, malePercent, femalePercent, raciallyInsensitivePercent = biasChecker.examineTextInput(jobInput2)

            results= {'bias': bias, 'words': words, 'malePercent': malePercent, 'femalePercent': femalePercent, 'raciallyInsensitivePercent': raciallyInsensitivePercent}

        except:
            errors.append("error")

    return render_template("index.html", errors=errors, results=results)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(403)
def page_forbidden(e):
    return render_template("403.html"), 403


@app.route('/background_process')
def background_process():
    try:
        jobDescription = request.args.get('jobInput', 0, type=str)

        bias, words, malePercent, femalePercent, raciallyInsensitivePercent = biasChecker.examineTextInput(jobDescription)

        return jsonify(result= {'bias': bias, 'words': words, 'malePercent': malePercent, 'femalePercent': femalePercent, 'raciallyInsensitivePercent': raciallyInsensitivePercent})


    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)
