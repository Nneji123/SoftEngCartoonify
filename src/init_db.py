from app import db


def main():
    """
    The main function is the entry point for the program.
    It creates a new database session and invokes the function that populates
    the database.

    """
    db.drop_all()
    db.create_all()
    print("Database created.")


if __name__ == "__main__":
    main()
