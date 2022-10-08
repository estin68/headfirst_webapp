from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


# function decorator - adjusts the behavior of an existing function
""" @app.route('/')
def hello() -> '302':
    return redirect('/entry') """


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form.get('phrase')
    letters = request.form.get('letters')
    result = str(search4letters(phrase, letters))
    title = "Here are your results: "
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=result,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title="Welcome to search4letters on the web!")


app.run(debug=True)
