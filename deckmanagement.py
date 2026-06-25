#The deck management (create, delete, edit). Pandas for csv handling

import pandas as pd 

try:
    pd.read_csv("./decks")
    
except:
    AttributeError(" 'decks' folder may have been deleted.")