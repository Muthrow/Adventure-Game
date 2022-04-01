import arcade
import arcade.gui

class Dialogue():
    def __init__(self, text, answers, correct, manager, score):
        self.correct = correct
        self.paused = True
        self.message = arcade.gui.UIMessageBox(
            width=500,
            height=350,
            message_text=(text),
            callback=self.onAnswer,
            buttons=answers
        )
        self.score = score
        self.wrong = False
        manager.add(self.message)

    def onAnswer(self, button):
        if button != self.correct:
            self.wrong = True  
        else:
            self.score += 100
        self.paused = False

    def getScore(self):
        return self.score
