from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

user = "root"
password = "root"
host = "localhost"
port = 3306
database = "empdept"
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
df = pd.read_sql("select * from stms",engine)



def display_records():
    return df.reset_index(drop=True)

def display_charts():
    x=df['name']
    y=df['marks']
    fig, ax = plt.subplots()
    ax.bar(x,y)
    ax.set_title("Student vs Marks")
    ax.set_xlabel("Student Name")
    ax.set_ylabel("Marks")

    return fig

