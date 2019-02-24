from flask import Flask, render_template
app = Flask(__name__)

blogposts = [
    {
        'author': 'Harry Potter',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Adam Schafer',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 15, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=blogposts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
