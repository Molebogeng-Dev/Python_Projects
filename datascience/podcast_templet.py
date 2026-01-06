import pandas as pd

episodes=[{"Title": ":______", "Guest": ":___", "Main_topic": ":__________"},
          {"Title": ":______", "Guest": ":___", "Main_topic": ":__________"},
          {"Title": ":______", "Guest": ":___", "Main_topic": ":__________"},
          {"Title": ":______", "Guest": ":___", "Main_topic": ":__________"}]

index_name=[f"Number{i+1}" for i in range(len(episodes)) ]

df = pd.DataFrame(episodes, index= index_name)

