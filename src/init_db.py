from app import db

def main():
    db.create_all()
    print("Database created.")
    
if __name__ == "__main__":
    main()
    
    