from app import db
from models import db, Users
import os
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv

load_dotenv()

def create_admin():
    """
    This function creates the admin user and adds it to the database.
    """
    try:
        hashed_password = generate_password_hash(os.getenv("ADMIN_PASSWORD"), method="sha256")
        admin = Users(username=os.getenv("ADMIN_USERNAME"), password=hashed_password, email=os.getenv("ADMIN_EMAIL"), is_admin=True)
        db.session.add(admin)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print("Error: " + str(e))
    finally:
        db.session.close()

def main():
    """
    The main function is the entry point for the program.
    It creates a new database session and invokes the function that populates
    the database.

    """
    db.drop_all()
    db.create_all()
    create_admin()
    print("Database created.")


if __name__ == "__main__":
    main()
