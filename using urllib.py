
# since HTTP is so common ,we have a library that does all the socket work for us and makes Web pages look like a file
import urllib.request

# Open the URL and treat it as a file
hand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# Loop through each line of the response
for line in hand:
    print(line.decode().strip())  # Decode and strip whitespace from each line

