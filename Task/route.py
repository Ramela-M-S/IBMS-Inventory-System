from flask import render_template, redirect,url_for,request,flash
from Task import app,db,login_manager
from Task.models import Item, User, Purchase, Feedback
from flask_login import login_user,logout_user, login_required, current_user



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def home_page():
    return render_template("home.html")




#REGISTER PAGE
@app.route("/register", methods = ["GET","POST"])
def register_page():
    if request.method == "POST":
        u_name=request.form["username"]
        email=request.form["email"]
        passwd=request.form["password"]
        
        # for admin
        user = User.query.filter_by(email=email).first()
        if user and user.password == passwd:
            login_user(user)
            flash("You had already logged in. Welcome!","success")
            return redirect(url_for("items_page"))
        
        #creating users
        with app.app_context():
            user1=User(username=u_name,password=passwd,email=email)
            
            db.session.add(user1)
            db.session.commit()
        flash("Account created successfully!",category="success")
        return redirect(url_for("login_page"))
    return render_template("register.html")





#LOGIN PAGE
@app.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        if email=="admin@gmail.com" and password=="admin":
            user=User.query.all()
            return render_template("admin.html",users=user)

        # find user by email
        user = User.query.filter_by(email=email).first()
        

        # simple password check (plain text)
        if user and user.password==password:
            login_user(user)
            return redirect(url_for("items_page"))
        else:
            flash("Login failed. Check email and password", category="danger")

    return render_template("login.html")




#ITEMS PAGE FROM LOGIN PAGE
@app.route("/items")
@login_required
def items_page():
    items = Item.query.all()
    return render_template("items.html",items=items,user_id=current_user.id)


#IF BUY BUTTON TOUCHED
@app.route("/buy",methods=["POST"])
def buy():
    item_id=int(request.form["item_id"])
    price=int(request.form["price"])
    quant=int(request.form["quantity"])
    u_id = int(request.form["user_id"])
    tot= price*quant
    purchase = Purchase(item_id = item_id, user_id=u_id, quantity=quant, Tot_price=tot)
    db.session.add(purchase)
    db.session.commit()
    
    return redirect(url_for("my_purchase"))
    
    
#SHOWS PURCHASED ITEMS BY THE USER
@app.route("/purchase")
@login_required
def my_purchase():
    purchases = Purchase.query.filter_by(user_id=current_user.id).all()
    return render_template("purchase.html",purchases=purchases)




#LOGOUT CODE
@app.route("/logout")
def logout_page():
    logout_user()
    flash("You had logged out",category="success")
    return redirect(url_for("home_page"))




    