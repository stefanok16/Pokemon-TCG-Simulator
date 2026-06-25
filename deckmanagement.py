#The deck management (create, delete, edit). Pandas for csv handling

import pandas as pd 
import os
import glob

#load in decks folder 
path = os.getcwd()
decks = glob.glob(os.path.join(path, "*.csv"))

#loop through continues to load csv into memory

try:
    for deck in decks:
        deck = pd.read_csv(deck)

except:
    AttributeError(" 'decks' folder may have been deleted")