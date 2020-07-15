from pandas import DataFrame

data = {'Product': ['Desktop Computer','Tablet','iPhone','Laptop'],
        'Price': [700,250,800,1200]
        }

df = DataFrame(data, columns= ['Product', 'Price'])

df.to_json (r'data/Export_DataFrame.json')