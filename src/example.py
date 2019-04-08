from GameEngine import GameEngine 
from MasterMind import MasterMind 
from Input import Input
from Output import Output  

masterMind = MasterMind(GameEngine(), Input(), Output());
masterMind.run();