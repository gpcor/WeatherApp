# Weather Script for MacOS

## Your weather forecast on a platter

### - The Idea
The idea is to get my daily forecast presented to me every morning between 7-9am via a command-line window that displays the results of the script. The weather information will be pulled using the **OpenWeather One Call API**, which can provide everything from the current weather to a minutely, hourly, and daily forecast. More information about this particular API [on the One Call API page](https://openweathermap.org/api/one-call-api)

### - How it works
The execution is as follows: A cronjob that is set up on my local machine will point to the location of the shell script and execute it between 7-9am. The shell script will be executed, navigating to my python script's location, activating the virtual environment and running weather.py. Weather.py will pull my API key from my text document, insert it and the other variables into the URL, submit the API request, and store the JSON response inside a text document. The script will then pull the pertinent information out of the text document and display a nicely formatted weather forecast on the screen via the terminal. Done!

### - Details regarding usage of the script
The script can be edited to include information specific to the user. The following variables are currently used in this iteration of the script:
  * **api_key:** _This is your API key for openweathermap. It is recommended that don't put the key directly into the code, but place it in a text file in the same directory and read it into a variable._
  * **lat:** _This is the latitude of the location you want the weather for._
  * **lon:** _This is the longitude of the location you want the weather for._
  * **units:** _This allows you to choose your measurement of choice from* **Kelvin**, **Metric**, or **Imperial**._    
  * **timezone:** _This is your current timezone so that the Epoch time properly displays your current time._

### - TODO
- [ ] Figure out how to take the formatted JSON and turn it into a readable forecast.
  * I either need to iterate through the JSON and separate the different forecast blocks (Current, Hourly, Daily) into sections and strip unimportant info and characters, or figure out if there's a package that'll translate it into plaintext for me.
- [ ] Translate the Epoch time in each forecast to human readable time. Python's Datetime module should be able to handle that.
- [ ] Create the shell script that'll handle the navigating to/running of **Weather.py**
- [ ] Figure out how to create a cronjob that will run at a certain time interval each day.
- [ ] A "Nice to have", but once the damn thing is working I'd like to transition from a command line script to a GUI popup that nicely presents itself every morning with my weather forecast. TKinter should be able to handle that.
