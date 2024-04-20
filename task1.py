

import pandas as pd
import sqlite3
import csv

path = '/workspaces/NoTown/no_town.csv'

csv_file = pd.read_csv(path)
print(csv_file.to_string())

#create database file called 'original_db.db'
con = sqlite3.connect('original_db.db')

#create a cursor to help create sql statements by creating the table and so on
cursor = con.cursor()

