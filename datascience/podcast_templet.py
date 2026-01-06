import pandas as pd

class 
'''ToDo: finish this function that will update everything in the df '''
def update_all(df):
    titles= df.columns
    for row in range(len(df)):
        for col in range(len(df.columns)):
            df.iloc[row][col]= input(f"Enter {titles[col]}: ")
        print(f"{df.iloc[row][1]}'s info updated")
    print("Data updated")

             
episodes=[{"Title": ":______", "Guest": ":___", "Main_topic": ":__________"},
          {"Title": ":______", "Guest": ":___", "Main_topic": ":__________"},
          {"Title": ":______", "Guest": ":___", "Main_topic": ":__________"},
          {"Title": ":______", "Guest": ":___", "Main_topic": ":__________"}]

index_name=[f"Number{i+1}" for i in range(len(episodes)) ]

df = pd.DataFrame(episodes, index= index_name)

print(df)