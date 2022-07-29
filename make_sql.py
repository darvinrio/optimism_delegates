import pandas as pd 

dele_df = pd.read_csv('op_delegates.csv')

for dele in dele_df.iterrows() :

    # Bullet List 
    # print("* `"+dele[1].Address+"` - "+dele[1].Name+"")

    # List of Names
    # print("'"+dele[1].Name+"',")

    # SQL case statement 
    print("when lower('"+dele[1].Address+"') then '"+dele[1].Name+"'")

    # SQL where in statement
    # print("lower('"+dele[1].Address+"'), --"+dele[1].Name)
    # break