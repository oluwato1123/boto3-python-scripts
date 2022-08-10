import boto3

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')

table = dynamodb.Table('Top_10_moviess')

#adding 10 Items to the table
table.put_item(
    Item = { 
        'movieID': "imdb-01",
        'Title': "The Godfather",
        'Year': "1972",
        'OscarNomination': '11'
    },
)
table.put_item(
    Item = { 
        'movieID': "imdb-02",
        'Title': " The Shawshank Redemption",
        'Year': "1994",
        'OscarNomination': '7'
    },
)
table.put_item(
    Item = { 
        'movieID': "imdb-03",
        'Title': "Schindler's List",
        'Year': "1993"
        'OscarNomination': '12'
    },
)
table.put_item(
    Item = { 
        'movieID': "imdb-04",
        'Title': "The Raging bull",
        'Year': "1980",
        'OscarNomination': '8'
    }
    
)
table.put_item(
    Item = { 
        'movieID': "imdb-05",
        'Title': "Casablanca",
        'Year': "1942",
        'OscarNomination': '8'
    },
)
table.put_item(
    Item = { 
        'movieID': "imdb-06",
        'Title': "Citizen Kane",
        'Year': "1941",
        'OscarNomination': '9'
    },
)
table.put_item(
    Item = { 
        'movieID': "imdb-07",
        'Title': "Gone with the Wind",
        'Year': "1939",
        'OscarNomination': '13'
    },
)
table.put_item(
    Item = { 
        'movieID': "imdb-08",
        'Title': "The Wizard of Oz",
        'Year': "1939",
        'OscarNomination': '6'
    },
)
table.put_item(
    Item = { 
        'movieID': "imdb-09",
        'Title': "One flew over the Cuckoo's Nest",
        'Year': "1975",
        'OscarNomination': '9'
    },
)
table.put_item(
    Item = { 
        'movieID': "imdb-10",
        'Title': " Lawrence of Arabia",
        'Year': "1962",
        'OscarNomination': '10'
    },
)
