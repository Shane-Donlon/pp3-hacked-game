import gspread
from google.oauth2.service_account import Credentials
import random
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hacked-passwords")
DATA = SHEET.worksheet("passwords")
PASSWORDS_DATA = DATA.col_values(1)
AMER_PASSWORDS = DATA.col_values(2)


def generate_random_word(data):
    """Runs random choice 3 times and returns random word as output"""
    
    i = 0
    while i < 3:
        word = random.choice(data)
        i += 1
    return word

random_word = generate_random_word(PASSWORDS_DATA)
print(random_word)