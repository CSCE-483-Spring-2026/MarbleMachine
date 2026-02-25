import time
import yaml
import datetime

# Gets the frequency from the user
def getFrequency():
    print("Enter Frequency in hours:")
    freq = input()
    return freq

# Gets the day of the week for weekly tasks
def getDayOfWeek():
    print("Enter day of the week [Mon, Tue, Wed, Thu, Fri, Sat, Sun]:")
    day = input()
    return day

# Gets the time of the day for the task
def getTimeOfDay():
    print("Enter a time of day HH:MM:SS --> ")
    tod = input()
    return tod

def printCurrConf(reply, freq, day, timeOfDay):
    print("Does this look good to you? y/n \n ----------------")
    print(reply, freq, day, timeOfDay)
    print("----------------")
    r = input()
    return r

def updateMarbles(reply, freq, day, timeOfDay):
    time.sleep(3)
    print("DONE!!!!!!")


# Basic idea of the program:

# Print out the current marbles
reply = "N"
# Loop:
while (True):
    # Prompt user to select marble or quit
    print("Select a marble to edit, or quit: \n" +
           "    Red     - 'r'\n" +
           "    Green   - 'g'\n" +
           "    Yellow  - 'y'\n" +
           "    Blue    - 'b'\n" +
           "    QUIT    - 'q'\n")
    reply = input()

    if (reply == "Q" or reply == "q"):
        break

    # User choose frequency
    freq = getFrequency()

    # If weekly frequency:
    period = 24
    if (freq == "weekly"):
        period = 24 * 7
        # User choose a day of the week
        day = getDayOfWeek()
    else:
        day = "every"
    # User chooses time of day
    timeOfDay = getTimeOfDay()

    # User Confirms/Cancels
    if (printCurrConf(reply, freq, day, timeOfDay) == "n"):
        print("Okay! Canceling...")
        continue

    # yaml updated
    print("Updating marbles.yaml...")
    updateMarbles(reply, freq, day, timeOfDay)


print("THANKS FOR USING THE MARBLE MACHINE PROGRAMMER\N" +
      "AODKNFGAPODFGNPADFKNVPOADHGJPOAERNGPOAIDNGPVOADNIFAO")