import pandas as pd


_episodes=[{"Title": ":______", "Guest": ":___", "Main_topic": ":__________"},
          {"Title": ":______", "Guest": ":___", "Main_topic": ":__________"},
          {"Title": ":______", "Guest": ":___", "Main_topic": ":__________"},
          {"Title": ":______", "Guest": ":___", "Main_topic": ":__________"}]

class Templet():
    def __init__(self,episodes=_episodes):
        self.episodes= episodes
        self.index_name=[f"Number{i+1}" for i in range(len(self.episodes)) ]
        self.df = pd.DataFrame(self.episodes, index= self.index_name)
        
    
    '''Updater'''
    @property
    def update_all(self):
        titles= self.df.columns
        for row in range(len(self.df)):
            for col in range(len(titles)):
                self.df.iloc[row][col]= input(f"Enter {titles[col]}: ")
            print(f"{self.df.iloc[row][1]}'s info updated")
        print("Data updated")
        return self.df
    
    '''file_overrider'''




def main():
    "Update file and make it an api"
    templet=print(Templet().update_all)

    
if __name__ == "__main__":
    main()