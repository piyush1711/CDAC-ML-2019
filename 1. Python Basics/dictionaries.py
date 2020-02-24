
countries=["India","China","US","Indonesia"]
pop=[1339180127,1409517397,324459463,263991379]

#### Calling by Index
ch_ind=countries.index("China")
pop_ch=pop[ch_ind]
pop_ch

populations={ "India":1339180127,
             "China":1409517397,
                "US":324459463,
                "Indonesia":263991379
        }

populations['China']

populations['Brazil']=209288278
populations

### Deletion
del(populations['Brazil'])

# Dictionary of dictionaries
demog = { 'India': { 'capital':'Delhi', 'population':1339180127 },
           'China': { 'capital':'Beijing', 'population':1409517397 },
           'US': { 'capital':'Washington', 'population':324459463 },
           'Indonesia': { 'capital':'Jakarta', 'population':263991379 } }

demog['US']['capital']

data={
    'capital':'Brasilia',
    'population':209288278
}

demog['Brazil']=data

demog

## Adding multiple Dicts
data2 = {
     'Pakistan':{  'capital':'Islamabad',
        'population':212742631},

      'Nigeria':{  'capital':'Abuja',
        'population':198577125
        }
      }

demog.update(data2)
