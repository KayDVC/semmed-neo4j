import os, getpass
from dotenv import load_dotenv

"""
A set of functions to generate a .env file for use with Neo4j Server hosting database.
"""
ENV_FILE = os.path.join(os.path.dirname(__file__), ".env")

def read_env_file() -> tuple[str, str]:
    
    # if env file not yet created, create
    if not os.path.exists(ENV_FILE):
        print(f"Env file '{ENV_FILE}' not found. Creating...")
        create_env_file()
    
    # read in new env file.
    load_dotenv()

    user = os.getenv("NEO4J_USER")
    pw = os.getenv("NEO4J_PW")

    return user, pw


def create_env_file():
    
    user = input("Username: ")
    pw = getpass.getpass("Password: ")

    creds = f"NEO4J_USER={user}\nNEO4J_PW={pw}"

    with open(ENV_FILE, 'w') as f:
        f.write(creds)

    return 