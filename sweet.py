!pip install sweetviz
import pandas as pd
df = pd.read_csv('Advertising.csv')
df.head()
import sweetviz as sv
advert_report = sv.analyze(df)
advert_report.show_html('Advertising.html')
advert_report.show_notebook()
