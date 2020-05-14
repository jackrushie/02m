from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_contacts_to_TXT(info):
    email = str(info['email'])
    subject = str(info['subject'])
    message = str(info['message'])
    DB = open("contacts.txt", "a")
    DB.write(f'\n{email}, {subject}, {message} |')


def write_contacts_to_CSV(info):
    with open('contacts.csv', newline='', mode='a') as database:
        email = str(info['email'])
        subject = str(info['subject'])
        message = str(info['message'])
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@ app.route('/contact_me', methods=['POST', 'GET'])
def contact_me():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_contacts_to_TXT(data)
            write_contacts_to_CSV(data)
            return(redirect('contact.html'))
        except:
            return('did not save')
    else:
        return('error')
