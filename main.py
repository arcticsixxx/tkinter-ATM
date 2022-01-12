import time
import random
import sys
import tkinter as tk
from PIL import ImageTk
from tkinter import Entry, IntVar, Label, Button, StringVar, Canvas


class App(tk.Frame):

    money = random.randint(2000, 5000)   

    def __init__(self, master):
        self.master = master
        super().__init__(master)
        self.initUI(master)
        self.cardAnimation(master)
        self.pinEnter(master)
        

    def initUI(self, master):
        '''Return an apearance of app

        Initialization of main materials of app.
        
        '''
        self.canv = Canvas(master, width=1000, height=900)
        self.mainImage = ImageTk.PhotoImage(file='bank.jpg')
        self.aMain = self.canv.create_image(400, 450, image=self.mainImage) 
        self.canv.place(relx=.187, rely=.061)

        '''Return ATM's buttons
        
        Initialization of ATM's buttons.

        '''
        self.back_button = Button(
                            text='<BCK', 
                            background='#aca498',
                            fg='#000000', 
                            activebackground='#aca498'
        ) 
        self.back_button.place(relx=.5485, rely=.354, width=34)

        self.balance_button = Button(
                                text='<BAL', 
                                background='#aca498', 
                                fg='#000000', 
                                activebackground='#aca498'
        ) 
        self.balance_button.place(relx=.5485, rely=.323, width=34)

        self.getMoney_button = Button(
                                text='>GET', 
                                background='#aca498', 
                                fg='#000000', 
                                activebackground='#aca498'
        ) 
        self.getMoney_button.place(relx=.294, rely=.325, width=34)

        self.giveMoney_button = Button(
                                text='>GVE', 
                                background='#aca498', 
                                fg='#000000', 
                                activebackground='#aca498'
        ) 
        self.giveMoney_button.place(relx=.294, rely=.355, width=34)

        self.exit_button = Button(
                           text='<EXT',
                           background='#aca498',
                           fg='#000000',
                           activebackground='#aca498',
                           command=self.exit
        )

        self.exit_button.place(relx=.5485, rely=.383, width=34)

        '''Return empty screen

        ATM's empty screen.

        '''
        self.screenMain = Label(
                        master, 
                        width=40, 
                        height=14, 
                        background='#a0ccdc'
        ) 
        self.screenMain.place(relx=.323, rely=.238)

    def main_menu(self):
        '''Return main menu
        
        Main menu of an app.

        '''

        self.mainMenu = Label(
                        width=40, 
                        height=14, 
                        background='#a0ccdc', 
                        text='MAIN MENU\n<BCK - RETURN TO MAIN MENU\n<BAL - SHOW BALANCE\n>GET - WITHDRAW CASH\n>GVE - DEPOSIT CASH'
        ) 
        self.mainMenu.place(relx=.323, rely=.238)

    def balance(self):
        self.balance = IntVar()
        self.balance.set(self.money)

        self.balanceLabel = Label(
                            width=40, 
                            height=14, 
                            background='#a0ccdc', 
                            textvariable=self.balance
        )
        self.balanceLabel.place(relx=.323, rely=.238)

    def balance_check(self):
        self.successLab = Label(
                        width=40, 
                        height=14, 
                        background='#00cb56', 
                        text='CASH SUCCESSFULLY WITHDRAWN'
        )
        self.failLab = Label(
                    width=40, 
                    height=14, 
                    background='#c9001a', 
                    text='AN ERROR HAS OCCURRED'
        )

        sum_check = int(self.getMoneyEntry.get())
        if sum_check <= int(self.money) and sum_check > 0:
            self.money -= sum_check
            time.sleep(2)
            self.REVmoneyAnimation(self.master)
            self.receiptAnimation(self.master)
            self.successLab.place(relx=.323, rely=.238)
        else:
            time.sleep(2)
            self.failLab.place(relx=.323, rely=.238)

    def getMoney(self):
        self.getMoneyLabel = Label(
                            width=40, 
                            height=14, 
                            background='#a0ccdc', 
                            text='CASH WITHDRAWAL\nENTER AMOUNT:'
        )
        self.getMoneyLabel.place(relx=.323, rely=.238)

        self.getMoneyEntry = Entry()
        self.getMoneyEntry.focus()
        self.getMoneyEntry.place(relx=.416, rely=.360, width=50)
        
        self.acceptButton = Button(
                            text='ACCEPT',
                            background='#aca498', 
                            fg='#000000', 
                            activebackground='#aca498', 
                            command=self.balance_check
        )
        self.acceptButton.place(relx=.413, rely=.389)

    def giveM_check(self):
        self.successLab = Label(
                        width=40, 
                        height=14, 
                        background='#00cb56', 
                        text='CASH SUCCESSFULLY DEPOSITED'
        )

        sum_add = int(self.giveMoneyEntry.get())
        self.money += sum_add
        self.moneyAnimation(self.master)
        self.receiptAnimation(self.master)
        time.sleep(2)
        self.successLab.place(relx=.323, rely=.238)
        

    def give_money(self):
        self.giveMoneyLabel = Label(
                            width=40, 
                            height=14, 
                            background='#a0ccdc', 
                            text='CASH DEPOSIT\nENTER THE AMOUNT YOU WANT TO DEPOSIT:'
        )
        self.giveMoneyLabel.place(relx=.323, rely=.238)

        self.giveMoneyEntry = Entry()
        self.giveMoneyEntry.focus()
        self.giveMoneyEntry.place(relx=.416, rely=.360, width=50)

        self.acceptButton = Button(
                            text='ACCEPT',
                            background='#aca498',
                            fg='#000000', 
                            activebackground='#aca498', 
                            command=self.giveM_check
        )
        self.acceptButton.place(relx=.413, rely=.389)
    
    def exit(self):
        self.REVcardAnimation(self.master)
        sys.exit()

    def verification(self):
        '''Return result of PIN validation
        
        Function validates PIN.  

        '''
        pin = self.pin_entry.get()
        
        if pin == '1234':
            self.pin_screen.destroy()
            self.pin_entry.destroy()
            self.submit_button.destroy()
            self.main_menu()
            self.back_button['command'] =  self.main_menu
            self.balance_button['command'] = self.balance
            self.getMoney_button['command'] = self.getMoney
            self.giveMoney_button['command'] = self.give_money
        else: 
            self.pin_text.set('ENTER PIN CODE\nINVALID PIN CODE')

    def moneyAnimation(self, master):
        list_of_money_images = [
            'Group 27.png', 'Group 28.png', 'Group 29.png', 
            'Group 30.png', 'Group 31.png', 'Group 32.png'
        ]
        for i in range(0, 6):
            money_obj = tk.PhotoImage(file='img/money/' + list_of_money_images[i])
            id_money = self.canv.create_image(468, 799, anchor='sw', image=money_obj)
            master.update()
            time.sleep(0.1)
    
    def REVmoneyAnimation(self, master):
        list_of_money_images_rev = [
            'Group 32.png', 'Group 31.png', 'Group 30.png', 
            'Group 29.png', 'Group 28.png', 'Group 27.png'
        ]
        for i in range(0, 6):
            money_obj = tk.PhotoImage(file='img/money/' + list_of_money_images_rev[i])
            id_money = self.canv.create_image(468, 799, anchor='sw', image=money_obj)
            master.update()
            time.sleep(0.1)
    
    def cardAnimation(self, master):
        list_of_cards_images = [
            'Group 2.png', 'Group 3.png', 'Group 4.png', 
            'Group 5.png', 'Group 6.png', 'Group 7.png', 
            'Group 8.png', 'Group 9.png', 'Group 10.png', 
            'Group 11.png', 'Group 12.png'
        ]
        for i in range(0, 11):
            card_obj = tk.PhotoImage(file='img/card/'+list_of_cards_images[i])
            id_card = self.canv.create_image(640, 642, anchor='sw', image=card_obj)
            master.update()
            time.sleep(0.1)
    
    def receiptAnimation(self, master):
        list_of_receipt_images = [
            'Group 20.png', 'Group 19.png', 'Group 18.png',
            'Group 17.png', 'Group 16.png', 'Group 15.png', 
            'Group 14.png', 'Group 13.png'
        ]
        for i in range(0, 8): 
            chek_obj = tk.PhotoImage(file='img/receipt/'+list_of_receipt_images[i])
            id_chek = self.canv.create_image(605, 403, anchor='sw', image=chek_obj)
            master.update()
            time.sleep(0.1)

    def REVcardAnimation(self, master):
        list_of_cards_images_rev = [
            'Group 12.png', 'Group 11.png', 'Group 10.png',
            'Group 9.png', 'Group 8.png', 'Group 7.png', 
            'Group 6.png', 'Group 5.png', 'Group 4.png', 
            'Group 3.png', 'Group 2.png'
            ]
        for i in range(0, 11): #обратная карта
            card_obj = tk.PhotoImage(file='img/card/'+list_of_cards_images_rev[i])
            id_card = self.canv.create_image(640, 642, anchor='sw', image=card_obj)
            master.update()
            time.sleep(0.1)

    def pinEnter(self, master):
        '''Return PIN's screen 
        
        PIN screen.

        '''
        self.pin_text = StringVar()
        self.pin_text.set('ENTER PIN CODE:')

        self.pin_screen = Label(
                        master, 
                        textvariable=self.pin_text, 
                        width=40, 
                        height=14,
                        background='#a0ccdc'
        ) 
        self.pin_screen.place(relx=.323, rely=.238)

        self.pin_entry = Entry(
                        master, 
                        show='*'
        )
        self.pin_entry.focus()
        self.pin_entry.place(relx=.416, rely=.360, width=50)

        self.submit_button = Button(
                            text='ACCEPT',
                            background='#aca498', 
                            fg='#000000', 
                            activebackground='#aca498',
                            command=self.verification
        )
        self.submit_button.place(relx=.413, rely=.389)
        
            
def main():
    root = tk.Tk()
    root.geometry('1280x1024')
    root.resizable(width=False, height=False)
    myapp = App(root)
    myapp.mainloop()

if __name__ == '__main__':
    main()