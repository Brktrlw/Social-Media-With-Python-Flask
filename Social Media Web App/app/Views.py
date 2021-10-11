from flask import Flask,render_template,flash,redirect,url_for,session, request,make_response
from userManager import UserManager
from functools import wraps
import logging
from friendsManager import FriendsManager
from itsdangerous import Signer
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app=Flask(__name__)
app.secret_key = '£#$½3y45#$½#$½74½$½456ju$½$½6u$½$½[$½68$½$½6u4½rtg€₺u$½u3456yu345u3'

# Kullanıcı giriş decaratörü
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Lütfen giriş yapınız")
            return redirect(url_for("homePage"))
    return decorated_function

@app.route("/")
def homePage():   #Ana Sayfaya gider
    response=make_response(render_template("homepage.html"))
    response.set_cookie("name","berkay")
    return response

@app.route("/User/<string:usernickname>")
@login_required
def userPage(usernickname):
    userData=UserManager.getUserDataByUserNickName(usernickname)
    if userData==[]:
        return render_template("errorpage.html")
    else:
        if userData[0].get("UserProfileStatus")==0:
            isFriend=FriendsManager.isFriendByUserId(1,2)
            if isFriend==None or isFriend==[]:
                arkadaslikGondermismi=FriendsManager.getFriendRequestByUsersId(1,2)
                if arkadaslikGondermismi==[]:
                    return render_template("user.html",friendStatus=False,arkadaslikGondermismi=False,userData=userData[0])
                else:
                    return render_template("user.html",friendStatus=False,arkadaslikGondermismi=True,userData=userData[0])
            else:
                return render_template("user.html",friendStatus=True,userData=userData[0])
        else:
            return render_template("user.html",userData=userData[0])

@app.route("/addFriendRequest",methods=["POST"])
def addFriendRequest():
    userId=UserManager.getUserIdByUserNickName(session["username"])
    FriendsManager.addRequestFriendByUsersId(userId[0][0],2)
    return redirect(request.referrer)
########
@app.route("/")
def ignoreFriendRequest():
    pass
########

@app.route("/deleteFriendRequest",methods=["POST"])
def deleteFriendRequest():
    userId=UserManager.getUserIdByUserNickName(session["username"])
    FriendsManager.deleteRequestFriendByUsersId(userId[0][0],2)
    return redirect(request.referrer)


@app.route("/Login",methods=["POST","GET"])
def loginPage():
    if request.method=="POST":
        userNickName=request.form.get("usernickname")
        userPassword=request.form.get("password")
        isLogin=UserManager.isLogin(userNickName,userPassword)
        if isLogin==[]:
            flash("Giriş başarısız,bilgilerinizi tekrar kontrol ediniz")
            return redirect(request.referrer)
        else:
            session["logged_in"]=True
            session["username"]=userNickName
            return render_template("homepage.html")
    else:
        return render_template("login.html")

@app.route("/Logout")
def logout():
    session.clear()
    return render_template("homepage.html")






if __name__=="__main__":
    app.run(debug=True)
