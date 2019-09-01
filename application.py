from flask import Flask, request, render_template
import csv

app = Flask(__name__)
pth = 'https://hacknightdiag981.blob.core.windows.net/apppython/storage.csv?sp=rcwd&st=2019-09-01T00:58:30Z&se=2019-09-01T08:58:30Z&spr=https&sv=2018-03-28&sig=fTCwk5PsTzpBDA9DvQ0Sd1j8VgR7GN9uJ38miZKhi7I%3D&sr=b'

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

        with open(pth,'w') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)

            # writerow() will write a row in your csv file
            writer.writerow({'name': name, 'comment': comment})

        return 'Thanks for your input!'
