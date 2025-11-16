import pandas as pd
import sqlite3
import os

DB_PATH = 'cta_ridership.db'
FILE_PATH = 'data/'
FILE_EXT = '.csv'

def db_connect():
    conn = sqlite3.connect(DB_PATH)
    with open('schemas.sql', 'r') as f:
        conn.executescript(f.read())
    return conn

def get_file_names():
    files = [for f in os.listdir(FILE_PATH) if f.endswith(FILE_EXT) and os.path.isfile(os.path.join(f))]
    return files

def extract_and_load(file, conn):
    # Ideally, for repeataility with other data sources, i'd like for this function to take the file name and create & populate tables using the file name. 
    # However, since I lack the authority to ask the city of Chicago to change the naming convention of their files, I've altered the file names myself.
    cur = conn.cursor()
    table_name = file.replace(FILE_EXT, '')

    # read file into pandas dataframe. In a reusable ETL framework, I'd have else statements for reading other file types like .json, .xlsx, etc.
    # But for the purpose of this exercise (and for meeting time constraints), I'm only implementing .csv reading.
    if FILE_EXT == '.csv':
        df = pd.read_csv(FILE_PATH+'/'+file)

    # drop duplicate rows (probably not necessary for this dataset, but good practice)
    df.drop_duplicates(inplace=True)

    # create staging table from dataframe
    df.to_sql(f'temp_{table_name}', conn, if_exists='replace', index=False)

    # insert data from staging table into target table, ignoring duplicates (based on primary key constraints)
    cols = ",".join(df.columns)
    conn.execute(f"""INSERT OR IGNORE 
                    INTO {table_name} ({cols}) 
                    SELECT {cols} FROM temp_{table_name};""")
    
    # drop staging table
    conn.execute(f'DROP TABLE temp_{table_name};')


def main():
    # establish SQLite database connection and creating tables
    print("Connecting to SQLite database...")
    conn = db_connect()
    print("Database connected and tables created.")

    # get list of source files
    file_list = get_file_names()

    # load tables from CSV files
    print("Loading data into tables...")
    for file in file_list:
        extract_and_load(file, conn)
        print(f"Loaded data from {file} into database.")
    print("Data loading complete.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()