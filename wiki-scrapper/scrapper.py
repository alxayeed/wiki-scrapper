from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# configure bs4
url = 'https://en.m.wikipedia.org/wiki/List_of_largest_Internet_companies'
response = requests.get(url).text
bs_object = BeautifulSoup(response, 'html.parser')

data = bs_object.find('table', class_='wikitable sortable mw-collapsible')
all_rows = data.find_all('tr')


# this list will contain each row of the table as inner list
table_data = []
for tr in all_rows[1:11]:
    row = []
    for t in tr.select('td')[:-1]:
        row.extend([t.text.strip()])
    table_data.append(row)


@app.route('/')
def home():
    return render_template('index.html', table_data=table_data)


if __name__ == "__main__":
    app.run(debug=True)
