class MasterMind:
	def __init__(self, gameEngine, input, output):
		self.gameEngine = gameEngine;
		self.input = input;
		self.output = output;
	def run(self):
		combination = self.gameEngine.getCombination();
		answer = "";
		count = 0;
		while not self.gameEngine.endReached(count) and not self.gameEngine.equals(combination, answer):
			self.output.write("Try")
			answer = self.input.ask();
			self.output.write(self.gameEngine.hint(answer, combination));
			count += 1;