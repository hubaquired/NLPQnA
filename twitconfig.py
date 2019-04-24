import configparser

config = configparser.ConfigParser()
config['twit_cred'] = {}
config['twit_cred']['consumer_key'] = 'Piw4UyGioCKDrohQ5YNzGmPfM'
config['twit_cred']['consumer_secret'] = 'rwMyIEuHUA8EJrqZZPneAm1RZejhUvNYbn0348d5IVez1G7pUu'
config['twit_cred']['access_token'] = '1120610131178414081-DY59F82vGEpX8pJfMn0kHJTyr7iAsE'
config['twit_cred']['access_token_secret'] = 'ubSqXUCHwGoex4yBWP3q2BTiK52CCtaxyXese8tqMemcx'
config['twit_cred']['lastrepliedmentionid'] = '0'

with open('twit_cred.ini', 'w') as configfile:
	config.write(configfile)