#Dave Jornales
#BSIS-NS-2B
# Activity # 5: Modify your Activity # 1 with GUI implemDetation

from tkinter import * 
from tkinter import messagebox

Excess = []

class LabelSample(Tk):

    def __init__(self):

        Tk.__init__(self)
        self.geometry("1280x720")
        self.config(bg= "#26323D")
        self.title("Decrypt/ Decrypt")
        self.iconbitmap('icon.ico')
        self.icon = PhotoImage(file = "icon.png")
        self.iconLbl = Label(self,  bg="#26323D", image =self.icon)
        self.iconLbl.place(relx = 0.5, rely = 0.05, anchor ='n')

        #Encrypt =============================================================
        self.EncryptFrame = Frame(self, height= 720, width= 500, bg="#26323D")
        self.EncryptFrame.place(relx = 0.03, rely = 0.55, anchor ='w')
        self.EncryptLabel = Label(self.EncryptFrame, text = "Encryption",  bg="#26323D", fg="#D3D7D8", font=('Arial', 18))
        self.EncryptLabel.grid(row=0, column=0, sticky="news")
        self.EncryptWordLabel = Label(self.EncryptFrame, text = "Word/s to Encrypt",  bg="#26323D", fg="#D3D7D8", font=('Arial', 14))
        self.EncryptWordLabel.grid(row=1, column=0, pady= 20, sticky="news")
        self.EncryptWordField = Text(self.EncryptFrame, bg="#2E3D4A", fg = "#D3D7D8", font=('Arial', 16), height=5, width= 45)
        self.EncryptWordField.grid(row=2, column=0, sticky="news")
        self.EncryptKeyLabel = Label(self.EncryptFrame, text = "Key",  bg="#26323D", fg="#D3D7D8", font=('Arial', 14))
        self.EncryptKeyLabel.grid(row=3, column=0, pady= 10, sticky="news")
        self.EncryptKeyField = Text(self.EncryptFrame, bg="#2E3D4A", fg = "#D3D7D8", font=('Arial', 16), height=5, width= 45)
        self.EncryptKeyField.grid(row=4, column=0, pady=5, sticky="news")
        self.EncryptedMessage = StringVar()
        self.EncryptedMessage.set("  Encrypted Message: ")
        self.EncryptedMessEntry = Entry(self.EncryptFrame, font=('Arial', 12), bd=0, state="readonly", textvariable=self.EncryptedMessage)
        self.EncryptedMessEntry.grid(row = 5, column= 0, pady=10, ipady=20, sticky="ew")
        self.EncryptBtn = Button(self.EncryptFrame, text = "Encrypt!", bg="#1B2731", fg = "#D3D7D8", font=('Arial', 12), command=self.encrypt, height= 2, width=20 )
        self.EncryptBtn.grid(row = 6, column= 0, pady=10)
        #=====================================================================

        #Decrypt =============================================================
        self.DecryptFrame = Frame(self, height= 720, width= 500, bg="#26323D")
        self.DecryptFrame.place(relx = 0.969, rely = 0.55, anchor ='e')
        self.DecryptLabel = Label(self.DecryptFrame, text = "Decryption",  bg="#26323D", fg="#D3D7D8", font=('Arial', 18))
        self.DecryptLabel.grid(row=0, column=0, sticky="news")
        self.DecryptWordLabel = Label(self.DecryptFrame, text = "Encrypted Word",  bg="#26323D", fg="#D3D7D8", font=('Arial', 14))
        self.DecryptWordLabel.grid(row=1, column=0, pady= 20, sticky="news")
        self.DecryptWordField = Text(self.DecryptFrame, bg="#2E3D4A", fg = "#D3D7D8", font=('Arial', 16), height=5, width= 45)
        self.DecryptWordField.grid(row=2, column=0, sticky="news")
        self.DecryptKeyLabel = Label(self.DecryptFrame, text = "Key",  bg="#26323D", fg="#D3D7D8", font=('Arial', 14))
        self.DecryptKeyLabel.grid(row=3, column=0, pady= 10, sticky="news")
        self.DecryptKeyField = Text(self.DecryptFrame, bg="#2E3D4A", fg = "#D3D7D8", font=('Arial', 16), height=5, width= 45)
        self.DecryptKeyField.grid(row=4, column=0, pady=5, sticky="news")
        self.DecryptedMessage = StringVar()
        self.DecryptedMessage.set("  Decrypted Message: ")
        self.DecryptedMessEntry = Entry(self.DecryptFrame, font=('Arial', 12), bd=0, state="readonly", textvariable=self.DecryptedMessage)
        self.DecryptedMessEntry.grid(row = 5, column= 0, pady=10, ipady=20, sticky="ew")
        self.DecryptBtn = Button(self.DecryptFrame, text = "Decrypt!", bg="#1B2731", fg = "#D3D7D8", font=('Arial', 12), command=self.decrypt, height= 2, width=20 )
        self.DecryptBtn.grid(row = 6, column= 0, pady=10)
        #=====================================================================

    def encrypt(self):
        keyStorage = list(self.EncryptKeyField.get(1.0, "end-1c"))
        wordStorage = list(self.EncryptWordField.get(1.0, "end-1c"))
        if len(keyStorage) != len(wordStorage):
            messagebox.showwarning("Warning", "Word and Key must have the\n same character length!")
            return
        keyNumbers = []
        for i in range(len(keyStorage)):
            ordinalValue = ord(keyStorage[i])
            divide = ordinalValue/23
            keyNumbers.append(round(divide))

        code = ""
        for i in range(len(wordStorage)):
            ordinalValue = ord(wordStorage[i])
            changedValue = ordinalValue + keyNumbers[i]
            if changedValue > 126:
                excess = changedValue - 126
                changedValue -= excess
                Excess.append(excess)
            Excess.append(0)
            code += chr(changedValue)
        self.EncryptedMessage.set("  Encrypted Message: \n"+code)


    def decrypt(self):
        keyStorage = list(self.DecryptKeyField.get(1.0, "end-1c"))
        wordStorage = list(self.DecryptWordField.get(1.0, "end-1c"))
        keyNumbers = []
        for i in range(len(keyStorage)):
            ordinalValue = ord(keyStorage[i])
            divide = ordinalValue/23
            keyNumbers.append(round(divide))

        x = 0
        answer = ""
        for i in range(len(wordStorage)):
            ordinalValue = ord(wordStorage[i])
            if ordinalValue == 126:
                ordinalValue += Excess[x]
                changedValue = ordinalValue - keyNumbers[i]
                answer += chr(changedValue)
                x += 1
            else:
                changedValue = ordinalValue - keyNumbers[i]
                answer += chr(changedValue)
        self.DecryptedMessage.set("  Decrypted Message: \n"+answer)

def main():
    LabelSample().mainloop()

main()