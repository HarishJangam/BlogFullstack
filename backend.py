from flask import Flask,request,jsonify,redirect,render_template,url_for,session,Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import json


app=Flask(__name__)
app.secret_key = 'secret_key' 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db=SQLAlchemy(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.app_context().push()
# connection = sqlite3.connect('your_database.db')


"""
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    notes = db.relationship('Note', backref='user', lazy=True)

# Define the Note model for the database
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
"""
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(60),unique=True,nullable=False)
    password=db.Column(db.String(20),nullable=False)
    confirm_password=db.Column(db.String(20),nullable=False)
    post = db.relationship('Note', backref='user', lazy=True)
    def __repr__(self):
        return f"User('{self.email}','{self.password}','{self.confirm_password}','{self.post}')"


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"User('{self.title}','{self.content}','{self.user_id}')"



@cross_origin() 
@app.route("/api/register",methods=["POST"])
def register():
    email=request.json.get('email')
    password=request.json.get('password')
    confirm_password=request.json.get('confirm_password')
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'error': f'{email } email already taken.'}), 400
    
    new_user = User(email=email, password=password,confirm_password=confirm_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': f'{email }User created successfully.'}), 200 

@cross_origin() 
@app.route("/api/login/post",methods=["POST"])
def post():
    title=request.json.get("title")
    content=request.json.get("content")
    # user_id=User.query.filter_by(id=id).first()
    user_id=request.json.get("user_id")
    new_post=Note(title=title,content=content,user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'message': f'{title } post created successfully.'}), 200 


@cross_origin() 
@app.route("/api/login",methods=["POST"])
def login():
    """
    user={
        "email":"harish",
        "password":"harish"
        
    }
    """
    email = request.json.get('email')
    password = request.json.get('password')
    user = User.query.filter_by(email=email).first()
    session["email"]=email
    session["logined_in"]=True
    resp=json.dumps({
        "error":"",
        "data":"err"
    })
    if user:
        psw=User.query.filter_by(password=password).first()
        # return jsonify({'': f'{email }User created successfully.'}), 200 
        return Response(response=resp.encode(),content_type="application/json", status=200)

    
    return jsonify({'error': 'Check email or password.'}), 400
    
    
@cross_origin()
@app.route("/api/login/Account",methods=["GET"])
def Account():
    """
    user:{
        "user_id":"1i383091",
        "password":"9jjk"
    }
    """
    # if "logined_in" in session and session["logined_in"]:
    data=session["email"]
    body = {
    "username": "harish",
    "email": "harish@gmail.com"
}
    print(body)
    err_msg="Success"
    status = 200
    resp =  json.dumps({
        "error": err_msg,
        "data": body
    })
    return jsonify({'': f'{"email" }User created successfully.'}), 200 
    # result = Response(response=resp.encode(),content_type="application/json", status=status)
    # return result 



@cross_origin() 
@app.route("/home",methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/logout")
def logout():
    data=session["email"]
    print(data)
    session.pop("email",None)
    session["logined_in"]=False
    return data


@app.route("/login/posts",methods=["GET"])
@cross_origin() 
def getAllPosts():
    res="select * from Note"
    print(res)
    return ""

if __name__=="__main__":
    app.run(debug=True)