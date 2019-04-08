import sys
import unittest
from src.GameEngine import GameEngine 
from src.MasterMind import MasterMind

class MasterMindTest(unittest.TestCase):
	def test_should_load_class(self):
		masterMind = MasterMind(GameEngineStub(), InputSpyStub(), OutputSpy());
	def test_should_run(self):
		inputSpy = InputSpyStub();
		outputSpy =  OutputSpy();
		masterMind = MasterMind(GameEngineStub(), inputSpy, outputSpy);
		masterMind.run();
		self.assertEqual(4, len(outputSpy.outputWritten));
		self.assertEqual(2, inputSpy.asked);
		self.assertEqual('+++-', outputSpy.outputWritten[1]);
		self.assertEqual('++++', outputSpy.outputWritten[3]);

class InputSpyStub:
	asked = 0;
	def ask(self):
		self.asked += 1;
		if self.asked == 1:
			return "ABCA";
		else:
			return "ABCD";

class OutputSpy:
	outputWritten = [];
	def write(self, question):
		self.outputWritten.append(question);

class GameEngineStub(GameEngine):
    def endReached(self, limit):
        return limit == 2;
    def getCombination(self):
        return "ABCD";
