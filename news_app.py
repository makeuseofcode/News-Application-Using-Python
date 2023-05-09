from tkinter import *
from tkinter import messagebox
import requests

apiKey = 'YOUR_API_KEY'

class NewsApp:
    global apiKey, type
    def __init__(self, root):
        self.root = root
        self.root.geometry('1000x650')
        self.root.title("News Application")
        self.root.config(bg='#ffc0cb')
        self.newsCatButton = []
        self.newsCat = ["general", "entertainment", "sports", "technology"]

        title = Label(self.root, text="News Application", font=("times new roman", 28, "bold"),pady=2, bg='#ff007f').pack(fill=X)

        F1 = LabelFrame(self.root,bg='#fc6c85')
        F1.place(x=20, y=80, width=215, height=210)

        for i in range(len(self.newsCat)):
            b = Button(F1, text=self.newsCat[i].upper(), width=15, bd=3, font="arial 14 bold", bg='#c154c1')
            b.grid(row=i, column=0, padx=10, pady=5)
            b.bind('<Button-1>', self.Newsarea)
            self.newsCatButton.append(b)

        F2 = Frame(self.root, bd=3)
        F2.place(x=260, y=80, relwidth=0.7, relheight=0.8)
        scroll_y = Scrollbar(F2, orient=VERTICAL)
        self.txtarea = Text(F2, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), bg='#fc6c85')
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.insert(END,"Select a category:")
        self.txtarea.pack(fill=BOTH, expand=1)

    def Newsarea(self, event):
        type = event.widget.cget('text').lower()
        BASE_URL = f'http://newsapi.org/v2/top-headlines?country=in&category={type}&apiKey=' + apiKey
        self.txtarea.delete("1.0", END)
        self.txtarea.insert(END, "--------------------------------------------------------------------\n")
        try:
            articles = (requests.get(BASE_URL).json())['articles']
            if (articles != 0):
                for i in range(len(articles)):
                    self.txtarea.insert(END, f"{articles[i]['title']}\n")
                    self.txtarea.insert(END, f"{articles[i]['description']}\n\n")
                    self.txtarea.insert(END, f"{articles[i]['content']}\n\n")
                    self.txtarea.insert(END, f"read more...{articles[i]['url']}\n")
                    self.txtarea.insert(END, "--------------------------------------------------------------------\n")
                    self.txtarea.insert(END, "--------------------------------------------------------------------\n")
            else:
                self.txtarea.insert(END, "No news available")
        except Exception as e:
            messagebox.showerror('ERROR', "Sorry, we ran into some issues. Please check your internet connection and try again.'(")

root = Tk()
obj = NewsApp(root)
root.mainloop()
