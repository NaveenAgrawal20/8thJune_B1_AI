from tkinter import *
from tkinter import messagebox as MSG
from PIL import Image, ImageTk


class TicTac():
    def __init__(self):
        self.app = Tk()
        self.app.geometry('315x400')
        self.app.resizable(False, False)
        self.app.title('Tic Tac Toe')
        self.__INF = -999
        self.clicked = True
        self.bot = 'X'
        self.player = 'O'
        self.playerX = 0
        self.playerO = 0
        self.playerX_var = StringVar()
        self.playerO_var = StringVar()
        self.btnFont = ('verdana', 18)
        self.pBtnStyle = {"text": " ", "font": "Helvetica 20", "height": 3, "width": 6, "bg": "#9effe7"}
        self.rBtnStyle = {"font": "Helvetica 20", "height": 3, "width": 10, "bg": "#b8fcf6"}
        self.reset()
        self.resetBtn = Button(self.app, text="RESET", command=self.reset).place(x=0, y=360, relwidth=1, relheight=0.1)
        self.playerX_var.set('Player X: ' + str(self.playerX))
        self.playerO_var.set('Player O: ' + str(self.playerO))
        self.app.mainloop()

    def checkForWin(self):
        if self.board[1] == self.board[2] and self.board[1] == self.board[3] and self.board[1] != ' ':
            return True
        elif self.board[4] == self.board[5] and self.board[4] == self.board[6] and self.board[4] != ' ':
            return True
        elif self.board[7] == self.board[8] and self.board[7] == self.board[9] and self.board[7] != ' ':
            return True
        elif self.board[1] == self.board[4] and self.board[1] == self.board[7] and self.board[1] != ' ':
            return True
        elif self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[2] != ' ':
            return True
        elif self.board[3] == self.board[6] and self.board[3] == self.board[9] and self.board[3] != ' ':
            return True
        elif self.board[1] == self.board[5] and self.board[1] == self.board[9] and self.board[1] != ' ':
            return True
        elif self.board[7] == self.board[5] and self.board[7] == self.board[3] and self.board[7] != ' ':
            return True
        else:
            return False

    def checkWhichMarkWon(self, mark):
        if self.board[1] == self.board[2] and self.board[1] == self.board[3] and self.board[1] == mark:
            return True
        elif self.board[4] == self.board[5] and self.board[4] == self.board[6] and self.board[4] == mark:
            return True
        elif self.board[7] == self.board[8] and self.board[7] == self.board[9] and self.board[7] == mark:
            return True
        elif self.board[1] == self.board[4] and self.board[1] == self.board[7] and self.board[1] == mark:
            return True
        elif self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[2] == mark:
            return True
        elif self.board[3] == self.board[6] and self.board[3] == self.board[9] and self.board[3] == mark:
            return True
        elif self.board[1] == self.board[5] and self.board[1] == self.board[9] and self.board[1] == mark:
            return True
        elif self.board[7] == self.board[5] and self.board[7] == self.board[3] and self.board[7] == mark:
            return True
        else:
            return False

    def checkDraw(self):
        for val in self.board.values():
            if val == ' ':
                return False
        return True

    def disableAll(self):
        self.b1.config(state=DISABLED)
        self.b2.config(state=DISABLED)
        self.b3.config(state=DISABLED)
        self.b4.config(state=DISABLED)
        self.b5.config(state=DISABLED)
        self.b6.config(state=DISABLED)
        self.b7.config(state=DISABLED)
        self.b8.config(state=DISABLED)
        self.b9.config(state=DISABLED)

    def reset(self):
        self.board = {
            1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' ',
        }
        self.b1 = Button(self.app, self.pBtnStyle, command=lambda: self.btn_click(self.b1, 1))
        self.b2 = Button(self.app, self.pBtnStyle, command=lambda: self.btn_click(self.b2, 2))
        self.b3 = Button(self.app, self.pBtnStyle, command=lambda: self.btn_click(self.b3, 3))
        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)

        self.b4 = Button(self.app, self.pBtnStyle, command=lambda: self.btn_click(self.b4, 4))
        self.b5 = Button(self.app, self.pBtnStyle, command=lambda: self.btn_click(self.b5, 5))
        self.b6 = Button(self.app, self.pBtnStyle, command=lambda: self.btn_click(self.b6, 6))
        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)

        self.b7 = Button(self.app, self.pBtnStyle, command=lambda: self.btn_click(self.b7, 7))
        self.b8 = Button(self.app, self.pBtnStyle, command=lambda: self.btn_click(self.b8, 8))
        self.b9 = Button(self.app, self.pBtnStyle, command=lambda: self.btn_click(self.b9, 9))
        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)
        self._cpuMove()

    def btn_click(self, b, num):
        if b['text'] == ' ' and self.clicked:
            b['text'] = self.player
            self.board[num] = self.player
            self.clicked = False
            if self.checkDraw():
                self.disableAll()
                MSG.showinfo('AI TIC TAC TOE', 'Match Draw')
                self.clicked = True
            else:
                self._cpuMove()
        else:
            MSG.showinfo('AI TIC TAC TOE', 'Choose another option')

    def __insert(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.bot
            if position == 1: self.b1.config(text=self.bot)
            if position == 2: self.b2.config(text=self.bot)
            if position == 3: self.b3.config(text=self.bot)
            if position == 4: self.b4.config(text=self.bot)
            if position == 5: self.b5.config(text=self.bot)
            if position == 6: self.b6.config(text=self.bot)
            if position == 7: self.b7.config(text=self.bot)
            if position == 8: self.b8.config(text=self.bot)
            if position == 9: self.b9.config(text=self.bot)

            if self.checkDraw():
                print(self.board)
                MSG.showinfo('AI TIC TAC TOE', 'DRAW')
                self.disableAll()
            else:
                if self.checkWhichMarkWon(self.player):
                    MSG.showinfo('AI TIC TAC TOE', 'Player is the winner')
                    self.disableAll()
                if self.checkWhichMarkWon(self.bot):
                    MSG.showinfo('AI TIC TAC TOE', 'Computer is the winner')

    def _cpuMove(self):
        self.clicked = True
        bestScore = self.__INF
        for key in self.board.keys():
            if self.board[key] == ' ':
                self.board[key] = self.bot
                score = self.__minimax(0, False)
                self.board[key] = ' '
                if score > bestScore:
                    bestScore = score
                    bestMove = key
        self.__insert(bestMove)

    def __minimax(self, depth, isMaximizer):
        # terminating conditions
        if self.checkWhichMarkWon(self.bot):
            return 1
        elif self.checkWhichMarkWon(self.player):
            return -1
        elif self.checkDraw():
            return 0
        # otherwise game continues
        # for cpu ( maximizer)
        if isMaximizer:
            bestScore = self.__INF
            for key in self.board.keys():
                if self.board[key] == ' ':
                    self.board[key] = self.bot
                    score = self.__minimax(depth + 1,not isMaximizer)
                    bestScore = max(score,bestScore)
                    self.board[key] = ' '
            return bestScore

        # minimizer move (player)
        else:
            bestScore = 999
            for key in self.board.keys():
                if self.board[key] == ' ':
                    self.board[key] = self.player
                    score = self.__minimax(depth+1,not isMaximizer)
                    bestScore = min(bestScore,score)
                    self.board[key] = ' '
            return bestScore



if __name__ == '__main__':
    TicTac()
