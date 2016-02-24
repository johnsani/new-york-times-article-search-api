import requests
import json
'''This program gets articles from The New York Times API2, from 1981 to 
today, retrieving headlines, abstracts, lead paragraphs and links''' 

url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?\
sort=oldest&begin_date=19810918&end_date=20160223&page=' + str(page)

key = '&api-key=e7ee0f929b1ba81db53f39dab63110b6:4:74510157'



for i in range(10):	
	url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?\
    sort=oldest&begin_date=19810918&end_date=20160223&page=' + str(i)
	url += key
	response = requests.get(url)
	json_obj = response.json()
	if json_obj['response']['docs'][i]:
		for articles in json_obj['response']['docs']:
			print "Publication Date:", articles['pub_date']
			print "Lead Paragraphs: ", articles['lead_paragraph']
			if articles['web_url'] == None:
				print "\n"
    		if articles['web_url']:
    			print "Links: ", articles['web_url']
    		elif articles['headline'] == None:
    			print "\n"
    			print "HeadLines: ", articles['headline']
    		elif articles['abstract'] == None:
    			print "\n"
    		if articles['abstract']:
    			print "Abtract: ", articles['abstract'] + "\n"
    		else:
    			print "\n"
