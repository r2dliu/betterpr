import urllib2
import requests
import challonge
import json
from trueskill import Rating, quality_1vs1, rate_1vs1

class Player:
    def __init__(self, name):
        self.name = name;
        self.wins = 0;
        self.losses = 0;
        self.elo = 0;
        self.matches = [];
        self.rating = Rating();
        self.rank = -1;

    def addMatch(match):
        matches.append[match];

    def updateRating(self, rating):
        self.rating = rating;

    def showInfo(self):
        print (self.name),
        print ("%dW - %dL" %(self.wins, self.losses));
        print ("Rating:"),
        print self.rating,
        print ("Rank: %d" %(self.rank));
        

class Match:
    def __init__(self):
        self.winner = ""
        self.loser = ""
        self.score = ""
        self.tourney = "";
        self.Round = 0;

    def __eq__(self, other):
        return self.__dict__ == other.__dict__;

    def setTourney(self, tourney):
        self.tourney = tourney;

    def setRound(self, Round):
        self.Round = Round;

    def setWinner(self, winner):
        self.winner = winner;
        
    def setLoser(self, loser):
        self.loser = loser;

    def setScore(self, score):
        self.score = score;

    def showInfo(self):
        print (self.tourney + " Round"),
        print (self.Round),
        print (": " + self.winner + " " + self.score + " " + self.loser);
        
def main():

    
    listPlayers = [];
    ranking = [];
    user = raw_input("Enter your challonge username: ");
    user = "uiblis";
    api_key = raw_input("Enter your api_key: ");
    api_key = "GqEWndsdFiH7JhkIc3l6Ezf8eg3VyxHkACjQN5Pa"

    challonge.set_credentials(user, api_key)

    print("Welcome to BetterPR!")
    print("")
        
    while True:
        print("Choose an option: ")
        print("1) Input a tournament URL ")
        print("2) Add a match ")
        print("3) View players ")
        print("4) Exit ")

        while True:
            choice = raw_input();
            if (choice == "1"):
                url = getURL();
                tournament = loadURL(url);
                print ""
                print "Tournament: " + tournament["name"];
                print "Date:",
                print tournament["started-at"];
        
                decision = raw_input("Compile data from this tournament? (y/n) ");
        
                while True:
                    if (decision == "n"):
                        break;
            
                    elif (decision == "y"):
                        tourneyPlayers = [];
                        tourneyMatches = [];
                        compileParticipants(url, tourneyPlayers, listPlayers);
                        compileMatches(url, tourneyMatches, tourneyPlayers, tournament, listPlayers);
                        for match in tourneyMatches:
                            match.showInfo();
                            listPlayers.sort(key = lambda x: x.rating.mu, reverse = True)
                            index = 1;
                        for player in listPlayers:
                            player.rank = index;
                            index +=1;
                            player.showInfo();
                        break;
                        
                    else:
                        print ("Please enter 'y' or 'n'. ");
                break;

def getURL():
    while True:
        url = raw_input("Enter a challonge url (eg. challonge.com/ladulite1): ");
        if (url[:4] == "www."):
            url = url[4:];
            
        
        if (url[:13] != "challonge.com"):
            try:
                x, y, z = url.split(".");
                a, b = z.split("/");
                url = x + "-" + b;
                return url;
            except ValueError:
                print ("Invalid url.");
                
        else:
            try:
                a, b = url.split("/")
                url = b;
                return url;
            except (ValueError):
                print ("Invalid url.");

def loadURL(url):
    while True:
        
        try:
            tournament = challonge.tournaments.show(url);
            return tournament;
        except (urllib2.HTTPError, urllib2.URLError):
            print "Invalid url."
            url = getURL();
    
def compileParticipants(url, tourneyPlayers, listPlayers):
    participants = challonge.participants.index(url);
    for participant in participants:
        flag = 0;
        tourneyPlayers.append((participant["id"], participant["name"]));
        for player in listPlayers:
            if player.name == participant["name"]:
                flag == 1;
                break;
        if (flag == 0):
            listPlayers.append(Player(participant["name"]));
        else:
            break;
                
    print "all players added";

def compileMatches(url, tourneyMatches, tourneyPlayers, tournament, listPlayers):
    matches = challonge.matches.index(url);
    counter = 0;
    for match in matches:
        for person in listPlayers:
            if match in person.matches:
                print ("Match already in database, skipping:");
                break;
                 
        tourneyMatches.append(Match());
        print "Counter: ",
        print counter;
        tourneyMatches[counter].setTourney(tournament["name"]);
        for player in tourneyPlayers:
            if match["winner-id"] == player[0]:
                tourneyMatches[counter].setWinner(player[1]);
                for person in listPlayers:
                    if person.name == player[1]:
                        winner = person;
                        print "winner defined"
            if match["loser-id"] == player[0]:
                tourneyMatches[counter].setLoser(player[1]);
                for person in listPlayers:
                    if person.name == player[1]:
                        loser = person;
        
        tourneyMatches[counter].setScore(match["scores-csv"]);
        tourneyMatches[counter].setRound(match["round"]);

        #update players
        new_r1, new_r2 = rate_1vs1(winner.rating, loser.rating)
        winner.updateRating(new_r1);
        loser.updateRating(new_r2);
        winner.wins = winner.wins + 1;
        loser.losses = loser.losses + 1;
        winner.matches.append(match);
        loser.matches.append(match);
        counter = counter + 1;
         
if __name__ == "__main__":
    main();

    
