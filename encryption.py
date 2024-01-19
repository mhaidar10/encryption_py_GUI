import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.font import families
import base64
import cryptography 
from cryptography.fernet import Fernet,InvalidToken  


screen =Tk()
screen.title("file encription")
screen.geometry('375x395')

namaFile = ''
keyNotReady = True
fnama=False

class app:
    def __init__(self):
        self.filename=None
        self.keyNotReady=True

    def fpath(self):
        global namaFile
        # show an "Open" dialog box and return the path to the selected file
        filename = askopenfilename()
        self.filename=filename   
        namaFile = filename

        global fnama
        fnama=True

    def keyGen(self):
        key = Fernet.generate_key()
        if self.filename!=None:
            #keygen = txtInput.get(1.0, "end-1c")   
            #keygen=keygen.encode() #encode str to bytes
            with open('filekey.key', 'wb') as filekey:
                filekey.write(key)
            with open('backup.key', 'ab') as backup:
                backup.write(f'{key}  {self.filename}\n'.encode())
        
            screen1=Toplevel(screen) #popup
            screen1.title('Keygen')
            screen1.geometry('400x250')
            screen1.configure(bg='pink')

            Label(screen1,text='Your Key : ',font='impack 10 bold').place(x=5,y=10)
            text2=Text(screen1,font='30',bd=4,wrap=WORD)
            text2.place(x=2,y=30,width=390,height=90)
            text2.insert(END,key)

            Label(screen1,text='Your file path : ',font='impack 10 bold').place(x=5,y=130)
            text3=Text(screen1,font='30',bd=4,wrap=WORD)
            text3.place(x=2,y=150,width=390,height=40)
            text3.insert(END,self.filename)


            #tkinter.messagebox.showinfo("Create By \U0001F49A Developer","You Generated key!!!")

            self.keyNotReady=False
            global keyNotReady 
            keyNotReady = self.keyNotReady

        elif self.filename==None:
            messagebox.showerror('Error','please Select File')
class encrypt(app):
    def __init__(self):
        super().__init__()
        self.filename = namaFile
        self.keyNotReady = keyNotReady
        

    def encrypted(self):
        if namaFile!=None and keyNotReady==False:
            with open('filekey.key', 'rb') as filekey:
                key = filekey.read()
        
            # using the generated key
            fernet = Fernet(key)
            print(fernet,type(fernet))
            # opening the original file to encrypt
            with open(namaFile, 'rb') as file:
                original = file.read()
                
            # encrypting the file
            encrypted = fernet.encrypt(original)
            
            # writing the encrypted data
            with open(namaFile, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)

            tkinter.messagebox.showinfo("Create By \U0001F49A Developer","file is encripted")

        elif fnama==False:
            messagebox.showerror('Error','please Select File')

        elif keyNotReady!=False:
            messagebox.showerror('Error','please Generate Key')


        
        
namaFile=None
dec_key=None
not_succes=True

class decrypt(app):
    def __init__(self):
        super().__init__()

    def decrypted(self):
        dec_key= code.get()
        print(dec_key)

        if namaFile!=None and dec_key!=None:            
            
            """ with open('filekey.key', 'rb') as filekey:
                key = filekey.read() """
                
            # using the key
            try:

                fernet = Fernet(dec_key)

                
                # opening the encrypted file
                with open(namaFile, 'rb') as enc_file:
                    encrypted = enc_file.read()
                
                

                # decrypting the file
                decrypted = fernet.decrypt(encrypted)

                # opening the file in write mode and
                # writing the decrypted data
                with open(namaFile, 'wb') as dec_file:
                    dec_file.write(decrypted)
                
                tkinter.messagebox.showinfo("Create By \U0001F49A Developer","file is decrypted")
                code.set('')
                
            except (ValueError, base64.binascii.Error, InvalidToken):
                #tkinter.messagebox.showerror('Error', 'Invalid Key Format')
                tkinter.messagebox.showerror('Error', 'Invalid Key Format or Decryption Failed')


        elif fnama==False:
            messagebox.showerror('Error','please Select File')
        
app=app()   
enc=encrypt()
dec=decrypt()

Label(screen,text='Select File',font='impack 10').place(x=10,y=10)
btnFile = Button(screen,text='SELECT FILE',bg='#1089ff',height=2,width=50,fg='#ffffff',command=app.fpath)
btnFile.place(x=10,y=50)

btnKeyGen=Button(screen,text='GENERATE KEY',bg='#000000',height=2,width=50,fg='#ffffff',command=app.keyGen)
btnKeyGen.place(x=10,y=100)

Label(screen,text='Paste your decrypt key',font='impack 10').place(x=10,y=170)
""" textDecrypt=Text(screen,font='20')
textDecrypt.place(x=10,y=200,width=360,height=40) """

code=StringVar()
Entry(textvariable=code).place(x=10,y=200,width=360,height=60)


btnEncrypted = Button(screen,text='ENCRYPTED',bg='#ed3833',height=2,width=23,fg='#ffffff',command=enc.encrypted)
btnEncrypted.place(x=10,y=250)

btnDecrypted = Button(screen,text='DECRYPTED',bg='#00bd56',height=2, width=23,fg='#ffffff',command=dec.decrypted)
btnDecrypted.place(x=200,y=250)


screen.mainloop()
