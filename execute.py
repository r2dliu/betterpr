from lxml import html
import requests
import challonge
import json
from trueskill import Rating, quality_1vs1, rate_1vs1

listPlayers = [];
ranking = [];

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
    user = raw_input("Enter your challonge username: ");
    user = "uiblis";
    api_key = raw_input("Enter your api_key: ");
    api_key = "GqEWndsdFiH7JhkIc3l6Ezf8eg3VyxHkACjQN5Pa"

    challonge.set_credentials(user, api_key)

    print("Begin");
        
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
            tourneyPlayers = [];
            tourneyMatches = [];
            compileParticipants(url, tourneyPlayers);
            compileMatches(url, tourneyMatches, tourneyPlayers, tournament);
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
            print("Please enter 'y' or 'n'. ");

def compileParticipants(url, tourneyPlayers):
    participants = challonge.participants.index(url);
    for participant in participants:
        tourneyPlayers.append((participant["id"], participant["name"]));
        if Player(participant["name"]) not in listPlayers:
            global listPlayers;
            listPlayers.append(Player(participant["name"]));
    print "all players added";

def compileMatches(url, tourneyMatches, tourneyPlayers, tournament):
     matches = challonge.matches.index(url);
     counter = 0;
     for match in matches:
         #make match object, add data
         tourneyMatches.append(Match());
         tourneyMatches[counter].setTourney(tournament["name"]);
         for player in tourneyPlayers:
             if match["winner-id"] == player[0]:
                 tourneyMatches[counter].setWinner(player[1]);
                 for person in listPlayers:
                     if person.name == player[1]:
                         winner = person;
             if match["loser-id"] == player[0]:
                 tourneyMatches[counter].setLoser(player[1]);
                 for person in listPlayers:
                     if person.name == player[1]:
                         loser = person;
        
         tourneyMatches[counter].setScore(match["scores-csv"]);
         tourneyMatches[counter].setRound(match["round"]);

         #update player
         new_r1, new_r2 = rate_1vs1(winner.rating, loser.rating)
         winner.updateRating(new_r1);
         loser.updateRating(new_r2);
         winner.wins = winner.wins + 1;
         loser.losses = loser.losses + 1;
             
         counter = counter + 1;
         
if __name__ == "__main__":
    main();

    
