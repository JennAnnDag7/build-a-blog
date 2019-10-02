from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:PleaseHelpMe7@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

                                                                                                                                                                                                                                                                                        
class Blogpost(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1000))
    
    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/', methods=['POST', 'GET'])
def index():
    return redirect('/blog')


@app.route('/blog', methods=['POST', 'GET'])
def blog():
    blogposts = Blogpost.query.all()
    return render_template('blog.html', title="Build a Blog", blogposts=blogposts)

   


@app.route('/newpost', methods=['POST', 'GET'])
def newpost():
    if request.method == 'POST':
        blogpost_title = request.form['title']
        blogpost_body = request.form['body']
        new_blogpost = Blogpost(blogpost_title, blogpost_body)
        if blogpost_title == "" and blogpost_body == "":
            return render_template('newpost.html', title_error = 'Please fill in the title.', 
            body_error = 'Please fill in the body.')
        if blogpost_title == "":
            return render_template('newpost.html', title_error = 'Please fill in the title.')
        if blogpost_body == "":
            return render_template('newpost.html', body_error = 'Please fill in the body.')
        db.session.add(new_blogpost)
        db.session.commit()
        return redirect('/blog')
    return render_template('newpost.html')




if __name__ == '__main__':
    app.run()