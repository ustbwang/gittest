import pandas as pd
columns = ['idea_id', 'pv', 'title', 'pro-id', 'idea_url', 'url']
data = pd.read_csv('extra_ES_candidate.txt', header=None, sep='\t', names=columns)

data = data[['idea_id', 'pv', 'idea_url', 'url', 'title']]

data.to_csv('qnm.txt', index=False, header=None, sep='\t')
print("dev branch test 2!")
