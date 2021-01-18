import twint
import schedule
import time

# you can change the name of each "job" after "def" if you'd like.
def jobtwo():
	print ("[proceso automático]... Fetching tweets.")
	c = twint.Config()
	# choose username (optional)
	c.Username = "nayibbukele"
	# choose search term (optional)
	# c.Search = "insert search term here"
	# choose beginning time (narrow results)
	c.Since = "2021-01-17"
	# set limit on total tweets
	c.Limit = 1000
	# no idea, but makes the csv format properly
	c.Store_csv = False
	# format of the csv
	c.Custom = ["username", "date", "time", "tweet", "link", "likes", "retweets", "replies", "mentions", "hashtags"]
	# change the name of the csv file
	c.Output = "filename2.json"
	twint.run.Search(c)

# run once when you start the program

# jobone()
jobtwo()

# run every minute(s), hour, day at, day of the week, day of the week and time. Use "#" to block out which ones you don't want to use.  Remove it to active. Also, replace "jobone" and "jobtwo" with your new function names (if applicable)

# schedule.every(1).minutes.do(jobone)
# schedule.every().hour.do(jobone)
# schedule.every().day.at("10:30").do(jobone)
# schedule.every().monday.do(jobone)
# schedule.every().wednesday.at("13:15").do(jobone)

# schedule.every(1).minutes.do(jobtwo)
schedule.every(5).seconds.do(jobtwo)
# schedule.every().day.at("10:30").do(jobtwo)
# schedule.every().monday.do(jobtwo)
# schedule.every().wednesday.at("13:15").do(jobtwo)

while True:
  schedule.run_pending()
  time.sleep(1)
