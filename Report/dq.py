# load data from postgresql database
import psycopg2
import pandas as pd
from pandas import DataFrame


def loadFromPostgres():
    frames = []
    columnsList = ['incident', 'shooter', 'victim']
    conn = psycopg2.connect(database="DWProject", user="postgres",
                            password="root", host="127.0.0.1", port="5432")
    print("Opened database successfully")

    cur = conn.cursor()
    for column in columnsList:
        cur.execute("SELECT * from " + column)
        rows = cur.fetchall()
        print("Operation done successfully")
        # save the name of the attributes with the dataframe
        df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
        frames.append([df, column])
    conn.close()
    return frames


def quality_check(df: DataFrame):
    return f"Checking {df[1]}: \n" \
        + "################## \n" + \
        "Checking for % of null values: \n" + str(df[0].isnull().sum() / len(df[0]) * 100) + "\n\n" \
        + "Checking for % of duplicated values: \n" + str(df[0].duplicated().sum() / len(df[0]) * 100) + "\n\n" \
        + "Checking for % of unique values: \n" + str(df[0].nunique() / len(df[0]) * 100) + "\n" \



dataFrames = loadFromPostgres()
results = []

for df in dataFrames:
    results.append(quality_check(df))

# save the results in a file
with open('results.txt', 'w') as f:
    for item in results:
        f.write("%s \n" % item)
