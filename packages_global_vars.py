"""All import packages and global const are added here"""
import random
import os
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style, init
from zxcvbn import zxcvbn
from getpass import getpass
from tabulate import tabulate
from password_generator import PasswordGenerator

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
leaderboard_sheet = SHEET.worksheet("leaderboard")
