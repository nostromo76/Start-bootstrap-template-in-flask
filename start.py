from flask import Flask, render_template, url_for,request
app = Flask(__name__)



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')

@app.route("/post")
def post():
    return render_template('post.html', title='Posts')


@app.route('/contact'methods=['POST'])
def contact():
    name=request.contact.get('name')
    email=request.contact.get('email')
    phone=requst.contact.get('phone')
    messsage=request.contact.get('message')
    return render_template("contact.html",title=title,name=name,emai=email,message=message")


if __name__ == '__main__':
    app.run(debug=True)



