import tkinter as tk
import pandas as pd

model = pd.read_pickle('house_price_predictor.pkl')


class LinRegGui():
    def __init__(self):
        self.app = tk.Tk()
        self.app.geometry('600x400')
        self.app.resizable(False, False)
        self.app.title('House Price Predictor')
        self.font = ('verdana', 12)
        self.btnFont = ('verdana', 18)
        self.btn_gridStyle = {"ipadx": 10, "ipady": 20, "padx": 5, "pady": 3}
        self._createWidget()
        self.app.mainloop()

    def getresult(self):
        income = eval(self.incomeField.get())
        age = eval(self.ageField.get())
        rooms = eval(self.roomsField.get())
        population = eval(self.populationField.get())
        query = pd.DataFrame({'income': [income], 'age': [age], 'rooms': [rooms], 'population': [population]})
        result = model.predict(query)
        self.resultLabel.configure(text=f"$ {result[0]:,.2f}")

    def _createWidget(self):
        # button
        self.predictButton = tk.Button(self.app, text='Predict', font=self.btnFont, width=15,
                                       background='#0ffdc1',
                                       activebackground="orange",
                                       command=self.getresult)
        self.predictButton.place(x=180, y=200)

        # income field
        tk.Label(self.app, text='Income', font=self.font).place(x=10, y=50)
        self.income = tk.StringVar()
        self.incomeField = tk.Entry(self.app, textvariable=self.income, font=self.font, width=12)
        self.incomeField.place(x=140, y=50)
        # age field
        tk.Label(self.app, text='Age of house', font=self.font).place(x=10, y=80)
        self.age = tk.StringVar()
        self.ageField = tk.Entry(self.app, textvariable=self.age, font=self.font, width=12)
        self.ageField.place(x=140, y=80)
        # rooms field
        tk.Label(self.app, text='No. of Rooms', font=self.font).place(x=300, y=50)
        self.rooms = tk.StringVar()
        self.roomsField = tk.Entry(self.app, textvariable=self.rooms, font=self.font, width=12)
        self.roomsField.place(x=420, y=50)
        # population field
        tk.Label(self.app, text='Population', font=self.font).place(x=300, y=80)
        self.population = tk.StringVar()
        self.populationField = tk.Entry(self.app, textvariable=self.population, font=self.font, width=12)
        self.populationField.place(x=420, y=80)

        # result label
        self.resultLabel = tk.Label(self.app, font=('verdana', 20, 'bold'))
        self.resultLabel.place(x=180, y=300)


if __name__ == '__main__':
    linRegGui = LinRegGui()
