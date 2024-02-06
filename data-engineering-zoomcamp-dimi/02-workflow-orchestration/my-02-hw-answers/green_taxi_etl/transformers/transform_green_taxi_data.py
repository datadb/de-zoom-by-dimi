import re

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

@transformer
def transform(data, *args, **kwargs):

    print("Rows with zero passengers:", data['passenger_count'].isin([0]).sum())
    print("Rows with zero trip distance:", data['trip_distance'].isin([0.0]).sum())

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date 

    print(data['VendorID'].unique()) # Q4

    new_cols=[]
    count = 0
    for column in data.columns:

        if any(char.isupper() for char in column): 
            column = camel_to_snake(column)
            count+=1
        new_cols.append(column)
    print('No of camelcase columns:' , count) # Q5
    data.columns = new_cols
    
    return data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0.0)]

@test
def test_passengers(output, *args):
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'

@test
def test_trip(output, *args):
    assert output['trip_distance'].isin([0]).sum() == 0.0, 'There are rides with zero trip distance'

@test
def test_vendorid(output, *args):
    assert 'vendor_id' in (output.columns), 'The vendor_id column is not here'
