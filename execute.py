from lxml import html
import requests
import challonge

class Player:
    def __init__(self):
        self.wins = 0;
        self.losses = 0;
        self.elo = 0;
        self.matches = [];
            
    def addMatch(match):
        matches.append[match];

class Match:
    def __init__(self):
        self.winner = ""
        self.loser = ""
        self.score = ""
        
    def setWinner(winner):
        self.winner = winner;
        
    def setLoser(loser):
        self.loser = loser;

    def setScore(score):
        self.score = score;
        
def main():
    user = raw_input("Enter your challonge username: ");
    user = "uiblis";
    api_key = raw_input("Enter your api_key: ");
    api_key = "GqEWndsdFiH7JhkIc3l6Ezf8eg3VyxHkACjQN5Pa"

    challonge.set_credentials(user, api_key)

    print("Begin");

    listPlayers = [];

    
        
    while True:
    
        url = raw_input("Enter a challonge url (eg. challonge.com/ladulite1): ");

        if (url[:4] == "www."):
            url = url[4:];
        
        if ("challonge.com" not in url):
                print ("please enter a valid url");

        elif (url[:13] != "challonge.com"):
            x, y, z = url.split(".");
            a, b = z.split("/");
            url = x + "-" + b;
            break;
    
        else:
            a, b = url.split("/")
            url = b;
            break;
    
        tournament = challonge.tournaments.show(url)

        print ""
        print "Tournament: " + tournament["name"];
        print "Date: ",
        print tournament["started-at"];
        print ""
        decision = raw_input("Compile data from this tournament? (y/n) ");

        while True:
            if (decision == "n"):
                exit;

            elif (decision == "y"):
                participants = compileData(url);
                print participants;
                break;
    
            else:
                print("Please enter 'y' or 'n'. ");

def compileData(url):
    participants = challonge.participants.index(url);
    return participants;

if __name__ == "__main__":
    main()

    
    
                    
