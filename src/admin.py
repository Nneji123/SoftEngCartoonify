from models import Users, db
from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import LoginManager, current_user, login_required
from werkzeug.security import generate_password_hash
import sqlalchemy


admin = Blueprint("admin", __name__, template_folder="./frontend")
login_manager = LoginManager()
login_manager.init_app(admin)


@login_required
@admin.route("/admin", methods=["POST","GET"])
def show():
    if current_user.is_authenticated and current_user.is_admin:
        return redirect(url_for("admin.show_users"))
    else:
        flash("User is not authorised to view this page")
        return redirect(url_for("login.show"))
    
@login_required
@admin.route("/admin/adduser", methods=["POST"])
def add_user():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        is_admin = request.form["is_admin"]
        
        hashed_password = generate_password_hash(password, method="sha256")
        if is_admin == "True":
            is_admin = True
        else:
            is_admin = False
        try:
            user = Users(username=username, password=hashed_password, email=email, is_admin=is_admin)
            db.session.add(user)
            db.session.commit()
            flash("User registered successfully!")
            redirect(url_for("admin.show_users"))
        except sqlalchemy.exc.IntegrityError as e:
            db.session.rollback()
            print("Error: " + str(e))
            flash("User already exists!")
            return redirect(url_for("admin.show_users"))
        finally:
            db.session.close()
        return redirect(url_for("admin.show_users"))
    
@login_required
@admin.route("/admin/users", methods=["GET","POST"])
def show_users():
    if current_user.is_authenticated and current_user.is_admin:   
        users = Users.query.all()
        return render_template("/admin/users.html", users=users)
    else:
        return redirect(url_for("login.show"))

        
@login_required
@admin.route("/admin/deleteuser/<user_id>")
def delete_user(user_id):
    if current_user.is_authenticated and current_user.is_admin:   
        user_id = Users.query.filter(Users.id == user_id).first()
        try:
            db.session.delete(user_id)
            db.session.commit()
            flash("User deleted")
            return redirect(url_for("admin.show_users"))
        except Exception as e:
            db.session.rollback()
            print(str(e))
        finally:
                db.session.close()
        return redirect(url_for("admin.show_users"))
    else:
        return redirect(url_for("login.show"))
    
    
 
    
@login_required
@admin.route("/admin/edituser/", methods=["POST"])
def edit_user():
    if current_user.is_authenticated and current_user.is_admin:     
        if request.method == "POST":   
            user = request.form["id"]
            new_username = request.form["new_username"]
            new_email = request.form["new_email"]
            new_is_admin = request.form["new_is_admin"]
            try:
                nameToBeEdited = Users.query.filter(Users.id == int(user)).first()
                if nameToBeEdited:
                    nameToBeEdited.username = str(new_username)
                    nameToBeEdited.email = str(new_email)
                    if new_is_admin == "True":
                        new_is_admin = True
                    else:
                        new_is_admin = False
                    nameToBeEdited.is_admin = bool(new_is_admin)
                    db.session.flush()
                    db.session.commit()
                    flash("User edited successfully") 
                    return redirect(url_for("admin.show_users"))     
            except Exception as e:
                db.session.rollback()
                print('[edit_user]' + str(e))
            finally:
                db.session.close()
        else:
            return redirect(url_for("admin.show_users"))
    flash("User not authenticated")
    return redirect(url_for("login.show"))

@login_required
@admin.route("/admin/search", methods=["POST", "GET"])
def search_show():
    if current_user.is_authenticated and current_user.is_admin:   
        return render_template("/admin/search.html")
    else:
        flash("User is not authorised to view this page")
        return redirect(url_for("login.show"))




@login_required
@admin.route("/admin/searched", methods=["POST", "GET"])
def search_users():
    if current_user.is_authenticated and current_user.is_admin:   
        if request.method == "POST":
            search = request.form["username"]
            print(search)
            try:
                if search == "":
                    flash("Please enter a search term")
                else:
                    search = "%{}%".format(search)
                    users = Users.query.filter(Users.username.like(search)).all()
                    print(users)
                    return render_template("/admin/search.html", users=users)
            except Exception as e:
                print(str(e))
            finally:
                db.session.close()
        else:
            return redirect(url_for("admin.show_users"))
    else:
        return redirect(url_for("login.show"))