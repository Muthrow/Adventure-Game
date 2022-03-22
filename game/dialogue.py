import arcade
import arcade.gui

class Dialogue():
    def __init__(self, text, answers, correct, manager, score):
        self.correct = correct
        self.score = score
        self.message = arcade.gui.UIMessageBox(
            width=500,
            height=350,
            message_text=(text),
            callback=self.onAnswer,
            buttons=answers
        )        

        manager.add(self.message)



    def onAnswer(self, button):
        if button == self.correct:
            self.score += 100
        else:
            pass