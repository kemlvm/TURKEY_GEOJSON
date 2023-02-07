import json
import os.path
import csv
import os
import pandas as pd
import requests
import pandas as pd
from requests.exceptions import Timeout
import math
from keplergl import KeplerGl

map_1 = KeplerGl(height=900)


with open("earthquake_final.csv", 'r') as f:
    csvData = f.read()

map_1.add_data(data=csvData, name='data_1')

print(map_1)
