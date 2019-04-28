import tweepy
import tkinter
import requests
import os
import configparser


lastid = '0'
replyflag = 0

def main():
	api = twitter_api()
	user = api.me()
	global lastid
	global replyflag

	for mention in reversed(list(tweepy.Cursor(api.mentions_timeline).items())):
		#Question Text
		print('before' + str(lastid) + ' ' + str(replyflag))
		print(str(mention.id) + mention.text)

		#Determine Response
		#no replies yet or has started replying
		if lastid == '0' or replyflag == 1:
			print('conf')
			replyflag = 1
			lastid = str(mention.id)
		#reached last reply point, allow replying
		elif lastid == str(mention.id):
			print('reached')
			replyflag = 1
			continue
		#still on old replies so skip
		else:
			print('else')
			continue

		#Answer Text - put response and links in these variables

		mentioner = mention.user.screen_name
		answer = answerQuery(mention.text)
		link = 'https://www.youtube.com/watch?v=PV3_UHG73oQ'
		response = "@%s %s\n%s" % (mentioner, answer, link)

		#Options for with image attachment or without
		api.update_status(response, in_reply_to_status_id=mention.id)
		#filename = 'imagetest.jpg'
		#api.update_with_media(filename, status=response, in_reply_to_status_id=mention.id)

		print('after' + str(lastid) + ' ' + str(replyflag))
	save_last_id()


def save_last_id():
	global lastid
	config = configparser.ConfigParser()
	config.read('twit_cred.ini')
	config['twit_cred']['lastrepliedmentionid'] = lastid

	with open('twit_cred.ini', 'w') as configfile:
		config.write(configfile)


def twitter_api():
	config = configparser.ConfigParser()
	config.read('twit_cred.ini')

	access_token = config.get('twit_cred', 'access_token')
	access_token_secret = config.get('twit_cred', 'access_token_secret')
	consumer_key = config.get('twit_cred', 'consumer_key')
	consumer_secret = config.get('twit_cred', 'consumer_secret')
	global lastid
	lastid = config.get('twit_cred', 'lastrepliedmentionid')

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	return api

main()