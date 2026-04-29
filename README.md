You will need to set up your Raspberry Pi. If you don’t know how to set up a pi, look at their website for basic instructions. The SD card should have a Linux OS already installed. We found Raspberry Pi Connect was the easiest to use, but you can choose how to connect after the basic setup.

You will need to set up an Apache web server. We followed a tutorial from Tom’s Hardware: https://www.tomshardware.com/news/raspberry-pi-web-server,40174.html. There are other instructions on the internet if you want to find a different way to set up.

Connect your git repository to your Pi. We already had this knowledge, but again, you can find lots of tutorials on the internet if you need more information on how to complete this task.

Run setup.sh. This script does three things. First, it clears any old garbage in /var/www/html. Second, it installs the necessary Python libraries to operate the color sensor. Third, it copied all web server files to /var/www/html. If this fails, you will need to look into what errors you’re getting. Usually, they were fairly descriptive and you might have to download installs. Feel free to contact us, but also Google is a thing.

Go to localhost on the Pi.

Setup the marbles to run. Look at main.py for more information.

Frequencies must be one of 5 options: ThirtySeconds, TwoMinutes, TwelveHours, Daily, or Weekly. These run at the time intervals you would expect based on their names.
Start Day can be any of the days of the week. Spell it using the full name of the day with a capital letter, i.e. Wednesday.
Start time is done in military time, so anything from 0:00 to 23:59. 

Click submit when all are filled in. 

Check the debug on the php page. If the json file was not successfully created, the first thing you should check is the file permissions for connect.php and marbles.json. The user www-data needs to have execute and write permission. Google was really helpful with this if you’re not confident about changing permissions. 

If the JSON file was successfully created, the marble machine should now be running successfully. If the hardware is connected and the marbles are in the run, they should be dropped at the proper time. The color sensor is also run off main.py, so everything is good from here. See the Hardware Demo section for a demonstration of proper functionality and information on debugging the hardware.

There will be a log script in logs/* in case you are still trying to debug the code after executing. The log file only reads from the python’s stderr output stream. Note this if you are trying to debug any code executed within main.py.
Have fun! Do things! You’ve got this, there are many ways to expand on this project, do something cool and tell us what you did if you’re proud of it! 