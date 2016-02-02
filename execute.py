from lxml import html
import requests
import challonge

user = raw_input("Enter your challonge username: ");
user = "uiblis";
api_key = raw_input("Enter your api_key: ");
api_key = "GqEWndsdFiH7JhkIc3l6Ezf8eg3VyxHkACjQN5Pa"

challonge.set_credentials(user, api_key)

print("Begin");

while True:
    
    url = raw_input("Enter a challonge url (eg. challonge.com/ladulite1): ");

    if ("challonge" not in url):
        print ("please enter a valid url");

    elif (url[:9] != "challonge"):
        x, y, z = url.split(".");
        a, b = z.split("/");
        url = x + "-" + b;
        break;
        
    else:
        a, b = url.split("/")
        url = b;
        print url;
        break;
    
tournament = challonge.tournaments.show(url)

print ""
print "Tournament: " + tournament["name"];
print "Date: ",
print tournament["started-at"];
print ""
decision = raw_input("Compile data from this tournament? (y/n) ");

if (decision == "n"):
    exit


    
    
                    
