# Not the Weather you need, but the Weather I will give ya!

## Weather from a random city around the world

### - The Idea
This program will pull a random city from the 'city.list.json' file, insert it into
the **OpenWeatherMap Current Weather API**, and then receive the weather data of said
random city. The relevant pieces of information are pulled out into several variables,
all of which will be used to format the body of an email. That email will be sent on
my behalf to my brother once every day using OAuth2 for Gmail. 

### TODO
- [ ] Create the formatted message body with relevant weather information
- [ ] Learn OAuth2
- [ ] Use OAuth2 to authenticate with Gmail and send the email.
- [ ] Create a bash script and cron job to automate the execution of the program daily.
- [ ] Deploy to the raspberry pi
- [ ] Watch Brother get random emails he doesn't want.
