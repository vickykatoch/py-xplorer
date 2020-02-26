import pandas as pd
import numpy as np
from os import path

cur_dir = path.abspath(__file__).replace(path.basename(__file__),'')
artist_data_file = path.join(cur_dir,'../../data/artist_data.csv')
df = pd.read_csv(artist_data_file)
print(df.head())