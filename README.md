![Better BT](https://i.imgur.com/6EWnYH4.png)

# Better BT
A python transportation communication system that utilizes the phone service provided by Blacksburg Transit that ensures students and residents in Blacksburg accurate upcoming bus times.

### Technologies Used
- Selenium
- Python
- Twilio
- Flask
- Ngrok

### P.S.
If anybody would want to try this personally, they would need to clone the git repo and ensure that they have all the required python packages (can be installed through pip) such as selenium, flask, twilio. As well as downloading and setting up ngrok and making a personal Twilio account along w/ personalized auth/identification keys.


## Inspiration
Virginia Tech students rely on an app called Blacksburg Transit(BT) to look at nearby buses and bus routes.  BT is bug-ridden as it commonly crashes and malfunctions on older phones.  Furthermore, it is a pain to use the mobile app to look at what buses come to a particular stop.  We created an application to solve this problem.
## What it does
It smoothens the process of getting transportation info for Virginia Tech students by automating bus route information in advance.  The user texts our SMS service the specific bus (optional), location and/or stop number, time (in 24 hr format).  Our application texts back the information about incoming buses and approximated arrivals about 10 minutes before the specified time.  This removes the need for using the app and saves several minutes of searching bus routes on the app to determine the potential buses to take.  

Example Text Message:
To (903) 289-7385:
TOM, Torgersen Hall, 1114, 21:33
The user wants to ride the TOM's creek bus, departing from Torgersen Hall, at Stop #1114 at approximately 21:33.
The application queries the Blacksburg transit website at 21:23 and texts back data regarding TOM buses running to Torgersen Hall at Stop #1114 within the next few hours.

Squires Ebnd, 22:30
The user wants to depart from Squires Eastbound, at approximately 22:30.
The application queries the Blacksburg transit website at 22:20 and texts back data regarding all buses departing from Squires Eastbound within the next few hours.
 
## How we built it
We used Twilio to create an SMS service that users can text and receive messages from.  It accepts a text from the user, converts it to a String format, and parses the String to determine how many arguments were specified and which arguments were specified.  The program then waits until it is 10 minutes before the specified time.  Then, we used Selenium to web-scrape the blacksburg transit website and obtain relevant data.   Finally, the application  texts back this information to the user in a readable format.
## Challenges we ran into
We struggled to find a proper SMS service.  Most of the ones we looked at required an initial premium fee, but we were skeptical to pay them in case the service did not fit our project's requirements.  However, we found Twilio to be the perfect service for us since it provided a free trial.  

We all had minimal experience in using selenium and web-scraping.  It was a new experience for all 4 of us to utilize this technology.  It was initially difficult to understand but we were persevered and learned how to incorporate it into our project.  

## What we learned
We learned how to use Twilio to make an efficient SMS service and learned how to use Selenium to automate the gathering of information from websites.  Most of us also did not have much experience with python so we had to pick up on the syntax in a short duration of time.  
## What's next for Better BT
Currently, we're using the free trial for Twilio that has a watermark on each text.  This increases the length of our text and we plan on upgrading out of the free trial when it ends so we can produce a more presentable message.

Another aspect that we hope to implement is a graphical way of relaying bus information.  We plan on making a map based on the data that we procure and sending it as a screenshot to the texter.  This gives the current locations of all the buses which allows the user to better understand what buses they can take.

Furthermore, our application only works with the Blacksburg Transit system.  We hope to expand our application to more bus systems in the nation.  Our technology will be incredibly useful to Virginia Tech students and we hope to make transportation systems across the nation more accessible and easier to use.

Some images that show our application's results:
### 2 Arguments with Location, no Stopcode:
![BetterBT_2_Arguments_Location](https://github.com/kaneru-soju/BetterBT/blob/master/Images/BetterBT_2_Arguments_Location.jpg)

### 2 Arguments with Stopcode, no Location:
![BetterBT_2_Arguments_Stopcode](https://github.com/kaneru-soju/BetterBT/blob/master/Images/BetterBT_2_Arguments_Stopcode.jpg)

### 3 Arguments:
![BetterBT_3_Arguments](https://github.com/kaneru-soju/BetterBT/blob/master/Images/BetterBT_3_Arguments.jpg)

### 4 Arguments:
![BetterBT_4_Arguments](https://github.com/kaneru-soju/BetterBT/blob/master/Images/BetterBT_4_Arguments.jpg)
