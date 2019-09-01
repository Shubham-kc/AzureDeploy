from flask import Flask, request, render_template
import csv

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form-csv.html')

@app.route('/save-comment', methods=['POST'])
def saveComment():
    # This is to make sure the HTTP method is POST and not any other
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        fieldnames = ['name', 'comment']

        with open('./nameList.csv','w') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)

            # writerow() will write a row in your csv file
            writer.writerow({'name': name, 'comment': comment})

        return 'Thanks for your input!'
