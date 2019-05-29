
scrapy startproject firstscraper

scrapy genspider gearvnbot gearvn.com
scrapy genspider coinmarketcapbot coinmarketcap.com
scrapy genspider quotes quotes.toscrape.com

#https://brickset.com/sets/year-2016/page-33
scrapy genspider bricksetbot brickset.com
scrapy genspider facebookbot facebook.com




scrapy runspider brickset.py
scrapy crawl gearvnbot
scrapy crawl brickset
scrapy crawl facebookbot
scrapy crawl coinmarketcapbot
scrapy crawl coinmarketcapbot -o coinmarketcap.json



scrapy crawl redditbot


pip install Scrapy


https://github.com/bast/somepackage
https://github.com/kennethreitz/samplemod


#send e-mail
https://www.programcreek.com/python/example/6443/smtplib.SMTP_SSL
https://medium.freecodecamp.org/send-emails-using-code-4fcea9df63f


####################################################################################################
#Web Scraping with Scrapy and MongoDB
https://realpython.com/web-scraping-with-scrapy-and-mongodb/

#LinkedIn Scraper
https://github.com/junekihong/linkedInScraper
####################################################################################################
pip freeze > requirements.txt
####################################################################################################
#Installing Scrapyd (generic way)
pip install scrapyd
pip install git+https://github.com/scrapy/scrapyd-client

#Starting Scrapyd
#To start the service, use the scrapyd command provided in the Scrapy distribution:
#C:\Users\Qing\Anaconda2\Scripts
scrapyd
<!-- scrapyd-deploy -l
scrapyd-deploy -L local -->

scrapyd-deploy local
curl http://localhost:6800/listprojects.json
curl http://localhost:6800/listversions.json?project=firstscraper

scrapyd-deploy local -p firstscraper


sudo firewall-cmd --permanent --add-port=6800/tcp
sudo firewall-cmd --zone=public --add-port=6800/tcp --permanent
sudo firewall-cmd --reload
sudo netstat -lntu
find / -name scrapy.cfg




curl http://localhost:6800/daemonstatus.json


curl http://localhost:6800/listspiders.json?project=firstscraper

curl http://localhost:6800/listjobs.json?project=firstscraper


curl http://localhost:6800/delversion.json -d project=firstscraper -d version=1558625703


curl http://localhost:6800/delversion.json -d project=firstscraper -d version=1558888198
curl http://localhost:6800/delversion.json -d project=firstscraper -d version=1558424784
curl http://localhost:6800/delversion.json -d project=firstscraper -d version=1558425247
curl http://localhost:6800/delversion.json -d project=firstscraper -d version=1558426337
curl http://localhost:6800/delversion.json -d project=firstscraper -d version=1558427012
curl http://localhost:6800/delversion.json -d project=firstscraper -d version=1558427617
curl http://localhost:6800/delversion.json -d project=firstscraper -d version=1558434524



curl http://localhost:6800/delproject.json -d project=firstscraper



curl http://localhost:6800/addversion.json -F project=firstscraper -F version=r23 -F egg=@firstscraper.egg



curl http://localhost:6800/schedule.json -d project=firstscraper -d spider=brickset


curl http://localhost:6900/schedule.json -d project=firstscraper -d spider=brickset



####################################################################################################
#Install Scrapyrt and combine it with our project
pip install scrapyrt
scrapyrt -p 3000


scrapyd-client firstscraper

####################################################################################################
#Store Scrapy crawled data in PostgresSQL
https://medium.com/codelog/store-scrapy-crawled-data-in-postgressql-2da9e62ae272
####################################################################################################
#How To Crawl A Web Page with Scrapy and Python 3 
#'http://brickset.com/
https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3
#Get started with Voice Driven Applications using Node.js
https://medium.com/coinmonks/get-started-with-voice-driven-applications-using-node-js-78902eb6bc44