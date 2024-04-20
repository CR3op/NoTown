

import pandas as pd
import sqlite3
import csv

path = '/workspaces/NoTown/no_town.csv'

csv_file = pd.read_csv(path)
print(csv_file.to_string())

