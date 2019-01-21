from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'me',
        'title': 'Blog post 1',
        'content': 'first content',
        'date_posted': '8.12.2018'
    },
    {
        'author': 'you',
        'title': 'Blog post 2',
        'content': 'second content',
        'date_posted': '7.12.2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)