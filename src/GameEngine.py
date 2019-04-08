import random

class GameEngine:
    def getCombination(self):
        combination = "";
        randomList = ['A','B','C','D','E','F'];
        for x in range(0,4):
            combination += random.choice(randomList)
        return combination;
    def hint(self, input, answer):
        try:
            output = "";
            for x in range(0,4):
                if input[x] == answer[x]:
                    output += "+";
                elif input[x] in answer:
                    output += "-";
                else:
                    output += " ";
        except:
            pass;
        return output
    def endReached(self, limit):
        return limit == 8;
    def equals(self, input, answer):
        return input == answer;