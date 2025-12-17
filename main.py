import pandas as pd
from visuals.performance_visuals import generate_visuals

df = pd.read_csv("data/operations_data.csv")
generate_visuals(df)
