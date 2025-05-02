import customtkinter as ctk
from PIL import Image
from utils.db_util import *
from utils.security_util import *

# COLOR PALLETE = https://coolors.co/ffffff-32373b-4a5859-9395d3-3185fc
WIDTH, HEIGHT = 960, 600

# Pallete
WHITE = "#FFFFFF"
BLACK = "#32373b"
GREY = "#4a5859"
PURPLE = "#5155B8"
BLUE = "#3185fc"

class App:
    '''
        Starts up baking application with all functionality included
    '''
    def __init__(self):       
        self.id = 1
        self.window = ctk.CTk()
        self.window.title("Trust Bank Online Service")
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        self.window.resizable(False, False)

        self.current_screen = self.login_screen_init()
        self.current_screen.grid_configure(row=1, column=1)

        self.window.mainloop()

    def login_screen_init(self) -> ctk.CTkFrame:
        self.login_frame = ctk.CTkFrame(master=self.window, width=WIDTH, height=HEIGHT)
        
        def login_section():
            self.left_frame = ctk.CTkTabview(master=self.login_frame, width=WIDTH//2, height=HEIGHT, 
                            fg_color=BLACK, segmented_button_selected_color=BLUE, 
                            bg_color=PURPLE)
            
            # Tab Setup
            self.left_frame.add("Login")
            self.left_frame.add("Sign Up")
            self.left_frame.set("Login")
            
            # Login Section
            self.login_info_frame = ctk.CTkFrame(master=self.left_frame.tab("Login"), fg_color=GREY,
                                       border_color=PURPLE, border_width=3)
            self.login_label = ctk.CTkLabel(master=self.login_info_frame, text="Login", fg_color=GREY, 
                                            text_color=WHITE, font=ctk.CTkFont("Bespoke Stencil", 40, 'bold'))
            self.l_email_input = ctk.CTkEntry(master=self.login_info_frame, width=200, bg_color=GREY, 
                                            border_color=PURPLE, placeholder_text_color=WHITE, 
                                            placeholder_text="Email..", font=ctk.CTkFont("Technor"))
            self.l_password_input = ctk.CTkEntry(master=self.login_info_frame, width=200, bg_color=GREY, 
                                            border_color=PURPLE, placeholder_text_color=WHITE, 
                                            placeholder_text="Password..", font=ctk.CTkFont("Technor"))
            self.login_button = ctk.CTkButton(master=self.login_info_frame, text="Login", fg_color=BLUE, 
                                            font=ctk.CTkFont("Technor"), command=self.login)
            self.l_notifier = ctk.CTkLabel(self.login_info_frame, text="Something went wrong, check input and try again...", 
                                                text_color="red", font=ctk.CTkFont("Technor", 20, "bold"), fg_color="transparent")
            
        def sign_up_section():
            # Sign Up Section
            self.sign_up_info_frame = ctk.CTkFrame(master=self.left_frame.tab("Sign Up"), 
                                       fg_color=GREY,
                                       border_color=PURPLE,
                                       border_width=3)
            self.sign_up_label = ctk.CTkLabel(master=self.sign_up_info_frame, text="Sign Up", fg_color=GREY, text_color=WHITE,
                                    font=ctk.CTkFont("Bespoke Stencil", 40, 'bold'))
            self.name_input = ctk.CTkEntry(master=self.sign_up_info_frame, width=200, bg_color=GREY, border_color=PURPLE, 
                                    placeholder_text_color=WHITE, placeholder_text="Name..",
                                    font=ctk.CTkFont("Technor"))
            self.s_email_input = ctk.CTkEntry(master=self.sign_up_info_frame, width=200, bg_color=GREY, border_color=PURPLE, 
                                    placeholder_text_color=WHITE, placeholder_text="Email..",
                                    font=ctk.CTkFont("Technor"))
            self.s_password_input = ctk.CTkEntry(master=self.sign_up_info_frame, width=200, bg_color=GREY, border_color=PURPLE, 
                                    placeholder_text_color=WHITE, placeholder_text="Password..", 
                                    font=ctk.CTkFont("Technor"))
            self.sign_up_button = ctk.CTkButton(master=self.sign_up_info_frame, text="Sign Up", fg_color=BLUE,
                                        font=ctk.CTkFont("Technor"), command=self.create_account)
            
            self.birthdate_frame = ctk.CTkFrame(master=self.sign_up_info_frame)
            self.year_input = ctk.CTkEntry(master=self.birthdate_frame, width=70, bg_color=GREY, border_color=PURPLE, 
                                    placeholder_text_color=WHITE, placeholder_text="YYYY",  
                                    font=ctk.CTkFont("Technor"))
            self.month_input = ctk.CTkEntry(master=self.birthdate_frame, width=40, bg_color=GREY, border_color=PURPLE, 
                                    placeholder_text_color=WHITE, placeholder_text="MM", 
                                    font=ctk.CTkFont("Technor"))
            self.date_input = ctk.CTkEntry(master=self.birthdate_frame, width=40, bg_color=GREY, border_color=PURPLE, 
                                    placeholder_text_color=WHITE, placeholder_text="DD", 
                                    font=ctk.CTkFont("Technor"))
            self.s_notifier = ctk.CTkLabel(self.sign_up_info_frame, text="Something went wrong, check input and try again...", 
                                                text_color="red", font=ctk.CTkFont("Technor", 20, "bold"), fg_color="transparent")

        def hero_section():
            # Hero Section
            self.right_frame = ctk.CTkFrame(master=self.login_frame, width=WIDTH//2, height=HEIGHT, fg_color=WHITE)
            img = Image.open("images/hero.png")
            self.hero_img = ctk.CTkImage(img, img, (img.width/1.5, img.height/1.5))
            self.hero_img_frame = ctk.CTkLabel(master=self.right_frame, width=WIDTH//2, height=HEIGHT, image=self.hero_img, text="")

        def organize():
            # Screen Config
            self.left_frame.grid_configure(row=1, column=1)
            self.left_frame.pack_propagate(False)
            
            # Login Confif
            self.login_info_frame.pack_configure(anchor="center", fill="both", padx=55, pady=180)
            self.login_label.pack_configure(padx=12, pady=12)
            self.l_email_input.pack_configure(pady=5)
            self.l_password_input.pack_configure(pady=5)
            self.login_button.pack_configure(pady=5)
            
            # Sign up config
            self.sign_up_info_frame.pack_configure(anchor="center", fill="both", padx=55, pady=140)
            self.sign_up_label.pack_configure(padx=12, pady=12)
            self.name_input.pack_configure(pady=5)
            self.s_email_input.pack_configure(pady=5)
            self.s_password_input.pack_configure(pady=5)
            self.birthdate_frame.pack_configure(pady=5)
            self.year_input.grid_configure(row=1, column=1)
            self.month_input.grid_configure(row=1, column=2)
            self.date_input.grid_configure(row=1, column=3)
            self.sign_up_button.pack_configure(pady=5)
            
            # Hero Section Config
            self.hero_img_frame.grid_configure()
            self.right_frame.grid_configure(row=1, column=2)
            
        login_section()
        sign_up_section()
        hero_section()
        organize()
        
        return self.login_frame
    
    def main_menu_init(self):
        self.main_menu_frame = ctk.CTkTabview(master=self.window, width=WIDTH, height=HEIGHT,
                                            fg_color=BLACK, segmented_button_selected_color=BLUE, 
                                            bg_color=PURPLE)
        self.main_menu_frame.add("Info")
        self.main_menu_frame.add("Transaction")
        self.main_menu_frame.add("Account")
        
        # Initializes Variables
        def variable_init():
            data = get_info(self.id, "email", "balance", "name", "birthdate", "acc_created")
            
            self.name = ctk.StringVar()
            self.name.set(data["name"])
            
            self.birthdate = ctk.StringVar()
            self.birthdate.set(data["birthdate"])
            
            self.acc_created = ctk.StringVar()
            self.acc_created.set(data["acc_created"])
            
            self.email = ctk.StringVar()
            self.email.set(data["email"])
            
            self.balance = ctk.DoubleVar()
            self.balance.set(data["balance"])
            
            self.accounts = [email for email in get_all_emails() if email != data["email"]]
            self.accounts.insert(0, "In cash")
            
        # Info tab intitiator
        def info_section():
            self.info_frame = ctk.CTkFrame(self.main_menu_frame.tab("Info"), width=WIDTH//2, height=HEIGHT - 50,
                                            fg_color=BLACK)
            self.i_title = ctk.CTkLabel(self.info_frame, text="User Info", text_color=BLUE, bg_color=BLACK,
                                        font=ctk.CTkFont("Bespoke Stencil", 40, 'bold', underline=True))
            
            self.i_name_label = ctk.CTkLabel(self.info_frame, text="Name:  ", text_color= BLUE,
                                             font=ctk.CTkFont("Technor", 20, "bold"))
            self.i_name = ctk.CTkLabel(self.info_frame, textvariable=self.name, text_color=WHITE,
                                       font=ctk.CTkFont("Technor", 20, "bold", slant='italic'))
            
            self.i_email_label = ctk.CTkLabel(self.info_frame, text="Email:  ", text_color= BLUE,
                                             font=ctk.CTkFont("Technor", 20, "bold"))
            self.i_email = ctk.CTkLabel(self.info_frame, textvariable=self.email, text_color=WHITE,
                                       font=ctk.CTkFont("Technor", 20, "bold", slant='italic'))
            
            self.i_balance_label = ctk.CTkLabel(self.info_frame, text="Balance:  ", text_color= BLUE,
                                             font=ctk.CTkFont("Technor", 20, "bold"))
            self.i_balance = ctk.CTkLabel(self.info_frame, textvariable=self.balance, text_color=WHITE,
                                       font=ctk.CTkFont("Technor", 20, "bold", slant='italic'))
            
            self.i_birthdate_label = ctk.CTkLabel(self.info_frame, text="Birthdate:  ", text_color= BLUE,
                                             font=ctk.CTkFont("Technor", 20, "bold"))
            self.i_birthdate = ctk.CTkLabel(self.info_frame, textvariable=self.birthdate, text_color=WHITE,
                                       font=ctk.CTkFont("Technor", 20, "bold", slant='italic'))
            
            self.i_acc_created_label = ctk.CTkLabel(self.info_frame, text="Account Created:  ", text_color= BLUE,
                                             font=ctk.CTkFont("Technor", 20, "bold"))
            self.i_acc_created = ctk.CTkLabel(self.info_frame, textvariable=self.acc_created, text_color=WHITE,
                                       font=ctk.CTkFont("Technor", 20, "bold", slant='italic'))
            
            self.i_title_2 = ctk.CTkLabel(self.info_frame, text="Important", text_color=BLUE, bg_color=BLACK,
                                        font=ctk.CTkFont("Bespoke Stencil", 40, 'bold', underline=True))
            
        # Transaction tab initiator
        def transaction_section():
            self.transaction_frame = ctk.CTkFrame(self.main_menu_frame.tab("Transaction"), width=WIDTH//2, height=HEIGHT - 50,
                                                  fg_color=BLACK)
            self.t_title = ctk.CTkLabel(self.transaction_frame, text="Transactions", text_color=BLUE, bg_color=BLACK,
                                        font=ctk.CTkFont("Bespoke Stencil", 40, 'bold', underline=True))
            
            self.t_withdraw_title = ctk.CTkLabel(self.transaction_frame, text="Withdraw:  $", text_color= WHITE,
                                             font=ctk.CTkFont("Technor", 20, "bold"))
            self.t_withdraw = ctk.CTkEntry(self.transaction_frame, bg_color=GREY, 
                                            border_color=BLUE, placeholder_text_color=GREY, 
                                            placeholder_text="100..", font=ctk.CTkFont("Technor"))
            self.t_withdraw_button = ctk.CTkButton(master=self.transaction_frame, text="Withdraw", fg_color=BLUE, 
                                            font=ctk.CTkFont("Technor"), command=self.withdraw)
            self.t_withdraw_dropdown = ctk.CTkOptionMenu(self.transaction_frame, values=self.accounts, fg_color=BLUE,
                                                         text_color=WHITE, dropdown_text_color="black",
                                                         dropdown_fg_color=GREY, dropdown_font=ctk.CTkFont("Technor"))
            
            self.t_deposit_title = ctk.CTkLabel(self.transaction_frame, text="Deposit:    $", text_color= WHITE,
                                             font=ctk.CTkFont("Technor", 20, "bold"))
            self.t_deposit = ctk.CTkEntry(self.transaction_frame, bg_color=GREY, 
                                            border_color=BLUE, placeholder_text_color=GREY, 
                                            placeholder_text="100..", font=ctk.CTkFont("Technor"))
            self.t_deposit_button = ctk.CTkButton(master=self.transaction_frame, text="Deposit", fg_color=BLUE, 
                                            font=ctk.CTkFont("Technor"), command=self.deposit)
            
            self.t_notifier = ctk.CTkLabel(self.transaction_frame, text="Something went wrong, check input and try again...", 
                                                text_color="red", font=ctk.CTkFont("Technor", 20, "bold"))
        
        # Account tab initiator
        def account_section():
            self.account_frame = ctk.CTkFrame(self.main_menu_frame.tab("Account"), width=WIDTH//2, height=HEIGHT - 50,
                                                  fg_color=BLACK)
            self.a_title = ctk.CTkLabel(self.account_frame, text="Account", text_color=BLUE, bg_color=BLACK,
                                        font=ctk.CTkFont("Bespoke Stencil", 40, 'bold', underline=True))
            
            self.a_change_password_label = ctk.CTkLabel(self.account_frame, text="Change Password:  ", text_color= WHITE,
                                             font=ctk.CTkFont("Technor", 20, "bold"))
            self.a_change_password = ctk.CTkEntry(self.account_frame, bg_color=GREY, 
                                            border_color=BLUE, placeholder_text_color=WHITE, 
                                            placeholder_text="New password", font=ctk.CTkFont("Technor"))
            self.a_change_password_button = ctk.CTkButton(master=self.account_frame, text="Change", fg_color=BLUE, 
                                            font=ctk.CTkFont("Technor"), command=self.change_password)
            
            self.a_change_email_label = ctk.CTkLabel(self.account_frame, text="Change Email:  ", text_color= WHITE,
                                             font=ctk.CTkFont("Technor", 20, "bold"))
            self.a_change_email = ctk.CTkEntry(self.account_frame, bg_color=GREY, 
                                            border_color=BLUE, placeholder_text_color=WHITE, 
                                            placeholder_text="New email", font=ctk.CTkFont("Technor"))
            self.a_change_email_button = ctk.CTkButton(master=self.account_frame, text="Change", fg_color=BLUE, 
                                            font=ctk.CTkFont("Technor"), command=self.change_email)
            
            self.a_sign_out_button = ctk.CTkButton(master=self.account_frame, text="Sign Out", fg_color=BLUE, 
                                            font=ctk.CTkFont("Technor"), command=self.sign_out)
            self.a_delete_button = ctk.CTkButton(master=self.account_frame, text="Delete Account", fg_color="red", 
                                            font=ctk.CTkFont("Technor"), command=self.delete_account)
            
            self.a_notifier = ctk.CTkLabel(self.account_frame, text="Something went wrong, check input and try again...", 
                                                text_color="red", font=ctk.CTkFont("Technor", 20, "bold"))
        
        # Organizes all widgets in all tabs
        def organize():
            # Info tab
            self.i_title.grid_configure(row=1, column=1, columnspan=5, pady=40)
            
            self.i_name_label.grid_configure(row=2, column=1)
            self.i_name.grid_configure(row=2, column=2, padx=10)
            
            self.i_acc_created_label.grid_configure(row=3, column=1)
            self.i_acc_created.grid_configure(row=3, column=2, padx=10)
            
            self.i_birthdate_label.grid_configure(row=4, column=1)
            self.i_birthdate.grid_configure(row=4, column=2, padx=10)
            
            self.i_title_2.grid_configure(row=5, column=1, columnspan=5, pady=40)
            
            self.i_email_label.grid_configure(row=6, column=1)
            self.i_email.grid_configure(row=6, column=2, padx=10)
            
            self.i_balance_label.grid_configure(row=7, column=1)
            self.i_balance.grid_configure(row=7, column=2, padx=10)
            
            self.info_frame.pack_configure(anchor="center", fill="y")
            
            # Transaction tab
            self.t_title.grid_configure(row=1, column=1, columnspan=5)
            
            self.t_withdraw_title.grid_configure(row=2, column=1)
            self.t_withdraw.grid_configure(row=2, column=2)            
            self.t_withdraw_dropdown.grid_configure(row=2, column=3, padx=10)
            self.t_withdraw_dropdown.set("In cash")
            self.t_withdraw_button.grid_configure(row=3, column=2, pady=20)

            self.t_deposit_title.grid_configure(row=5, column=1)
            self.t_deposit.grid_configure(row=5, column=2)
            self.t_deposit_button.grid_configure(row=5, column=3, columnspan=2, pady=20)
            
            self.transaction_frame.pack_configure(anchor="center", fill="y")
            
            # Account tab
            self.a_title.grid_configure(row=1, column=1, columnspan=5)
            
            self.a_change_password_label.grid_configure(row=2, column=1)
            self.a_change_password.grid_configure(row=2, column=2)
            self.a_change_password_button.grid_configure(row=2, column=3, padx=10, pady=20)
            
            self.a_change_email_label.grid_configure(row=4, column=1)
            self.a_change_email.grid_configure(row=4, column=2)
            self.a_change_email_button.grid_configure(row=4, column=3, padx=10, pady=20)
            
            self.a_sign_out_button.grid_configure(row=6, column=1, pady=150)
            self.a_delete_button.grid_configure(row=6, column=3, pady=150)
            
            self.account_frame.pack_configure(anchor="center", fill="y")
            
            
        variable_init()
        info_section()
        transaction_section()
        account_section()
        organize()
        
        return self.main_menu_frame
    
    # Creates account and checks for misinputs
    def create_account(self):
        email = self.s_email_input.get()
        password = hash_password(self.s_password_input.get())
        name = self.name_input.get()
        birthdate = f"{self.year_input.get()}-{self.month_input.get()}-{self.date_input.get()}"
        
        # If email exists
        if get_id(email):
            self.s_notifier.configure(text="Email Exists", text_color="red") 
            self.s_notifier.pack_configure()
            self.window.after(3000, lambda: self.s_notifier.pack_forget())
            return
        
        # If password, email or name is empty
        elif self.s_password_input.get() == "" or self.s_email_input.get() == "" or self.name_input.get() == "":
            self.s_notifier.configure(text="One or more fields are empty", text_color="red") 
            self.s_notifier.pack_configure()
            self.window.after(3000, lambda: self.s_notifier.pack_forget())
            return
        
        # If year, date or month are not digits
        elif not self.year_input.get().isdigit() or not self.month_input.get().isdigit() or not self.date_input.get().isdigit():
            self.s_notifier.configure(text="One or more birthdate values are not digits", text_color="red") 
            self.s_notifier.pack_configure()
            self.window.after(3000, lambda: self.s_notifier.pack_forget())
            return
        
        # If year, month or date are not the right length
        elif len(self.year_input.get()) < 4 or len(self.month_input.get()) > 2 or len(self.date_input.get()) > 2:
            self.s_notifier.configure(text="One or more birthdate values are invalid", text_color="red") 
            self.s_notifier.pack_configure()
            self.window.after(3000, lambda: self.s_notifier.pack_forget())
            return
        
        # If month is not in range 0 < x <= 12
        elif int(self.month_input.get()) > 12 or int(self.month_input.get()) <= 0:
            self.s_notifier.configure(text="Month is invalid", text_color="red") 
            self.s_notifier.pack_configure()
            self.window.after(3000, lambda: self.s_notifier.pack_forget())
            return
        
        # If date is not in range 0 < x <= 31
        elif int(self.date_input.get()) > 31 or int(self.date_input.get()) <= 0:
            self.s_notifier.configure(text="Date is invalid", text_color="red") 
            self.s_notifier.pack_configure()
            self.window.after(3000, lambda: self.s_notifier.pack_forget())
            return
        
        add_user(email, password, name, birthdate)
        
        self.id = get_id(email)
        self.current_screen.grid_forget()
        self.current_screen = self.main_menu_init()
        self.current_screen.grid_configure(row=1, column=1)
    
    # Logs user in and checks for misinputs
    def login(self):
        email = self.l_email_input.get()
        id = get_id(email)
        
        # If email corresponds with id
        if id:
            hashed_pass = get_info(id, "hash")["hash"]
            password = self.l_password_input.get()
            is_correct = check_password_hash(str(hashed_pass), str(password))
            
            # If password is correct
            if is_correct:
                self.id = id
                self.current_screen.grid_forget()
                self.current_screen = self.main_menu_init()
                self.current_screen.grid_configure(row=1, column=1)
            else:
                self.l_notifier.configure(text="Incorrect Password", text_color="red") 
                self.l_notifier.pack_configure()
                self.window.after(3000, lambda: self.l_notifier.pack_forget())
        else: 
            self.l_notifier.configure(text="Email Doesn't Exist", text_color="red") 
            self.l_notifier.pack_configure()
            self.window.after(3000, lambda: self.l_notifier.pack_forget())
    
    # Withdraw money and check for errors
    def withdraw(self):
        amount : str = self.t_withdraw.get() 
        
        # If input is empty
        if len(amount) == 0:
            self.t_notifier.configure(text="Input empty...", text_color="red")
            self.t_notifier.grid_configure(row=6, column=1, columnspan=5)
            self.window.after(3000, lambda: self.t_notifier.grid_forget())
            return
        
        # If input is not a number
        if not amount.isdigit(): 
            try:
                if not isinstance(float(amount), float):
                    self.t_notifier.configure(text="Not a valid number..", text_color="red")
                    self.t_notifier.grid_configure(row=6, column=1, columnspan=5)
                    self.window.after(3000, lambda: self.t_notifier.grid_forget())
                    return
            except:
                self.t_notifier.configure(text="Not a valid number..", text_color="red")
                self.t_notifier.grid_configure(row=6, column=1, columnspan=5)
                self.window.after(3000, lambda: self.t_notifier.grid_forget())
                return
        
        # If input is a number or decimal
        if amount.isdigit() or isinstance(float(amount), float):
            amount = round(float(amount), 2)
            available_cash = float(get_info(self.id, "balance")["balance"])
            
            if amount <= 0:
                self.t_notifier.configure(text="Zeros and less are invalid", text_color="red")
                self.t_notifier.grid_configure(row=6, column=1, columnspan=5)
                self.window.after(3000, lambda: self.t_notifier.grid_forget())    
                return
            
            # If input is greater than money available in account
            if (available_cash >= amount):
                recipient = self.t_withdraw_dropdown.get()
                
                if recipient != "In cash":
                    recipient_id = get_id(recipient)
                    recipient_balance = float(get_info(recipient_id, "balance")["balance"])
                    
                    update_info(self.id, balance=available_cash - amount)
                    update_info(recipient_id, balance=recipient_balance + amount)
                else:
                    update_info(self.id, balance=available_cash - amount)
                
                
                self.balance.set(round(float(get_info(self.id, "balance")["balance"]), 2))
                self.t_notifier.configure(text="Success", text_color="green")
                self.t_notifier.grid_configure(row=6, column=1, columnspan=5)
                self.window.after(3000, lambda: self.t_notifier.grid_forget())       
                return
            
            self.t_notifier.configure(text="Insufficient funds", text_color="red")
            self.t_notifier.grid_configure(row=6, column=1, columnspan=5)
            return
        
        self.t_notifier.configure(text="Something went wrong, check input and try again...", text_color="red")
        self.t_notifier.grid_configure(row=6, column=1, columnspan=5)
        return
    
    # Adds money to account and checks for errors
    def deposit(self):
        amount : str = self.t_deposit.get() 
        
        # If input is empty
        if len(amount) == 0:
            self.t_notifier.configure(text="Input empty...", text_color="red")
            self.t_notifier.grid_configure(row=6, column=1, columnspan=5)
            self.window.after(3000, lambda: self.t_notifier.grid_forget())   
            return
        
        # If input is not a number
        if not amount.isdigit(): 
            try:
                if not isinstance(float(amount), float):
                    self.t_notifier.configure(text="Not a valid number..", text_color="red")
                    self.t_notifier.grid_configure(row=6, column=1, columnspan=5)
                    self.window.after(3000, lambda: self.t_notifier.grid_forget())   
                    return
            except:
                self.t_notifier.configure(text="Not a valid number..", text_color="red")
                self.t_notifier.grid_configure(row=6, column=1, columnspan=5)
                self.window.after(3000, lambda: self.t_notifier.grid_forget())   
                return
        
        # If input is a decimal or integer
        if amount.isdigit() or isinstance(float(amount), float):
            amount = round(float(amount), 2)
            
            if amount <= 0:
                self.t_notifier.configure(text="Zeros and less are invalid", text_color="red")
                self.t_notifier.grid_configure(row=6, column=1, columnspan=5)
                self.window.after(3000, lambda: self.t_notifier.grid_forget())   
                return
            
            available_cash = float(get_info(self.id, "balance")["balance"])
            
            update_info(self.id, balance=available_cash + amount)
            
            self.balance.set(round(available_cash + amount, 2))
            self.t_notifier.configure(text="Success", text_color="green")
            self.t_notifier.grid_configure(row=6, column=1, columnspan=5)
            self.window.after(3000, lambda: self.t_notifier.grid_forget())       
            return
        
        self.t_notifier.configure(text="Something went wrong, check input and try again...", text_color="red")
        self.t_notifier.grid_configure(row=6, column=1, columnspan=5)
        return
    
    # Changes password in account section
    def change_password(self):
        new_password = hash_password(self.a_change_password.get())
        update_info(self.id, hash=new_password)
        
        self.a_notifier.grid_configure(row=5, column=1, columnspan=5)
        self.a_notifier.configure(text="Changed Password Successfully", text_color="green")
        self.window.after(3000, lambda: self.a_notifier.grid_forget())       
        return
    
    # Changes email in account section
    def change_email(self):
        email = self.a_change_email.get()
        id = get_id(email)
        
        # If email is not available
        if id != None:
            self.a_notifier.grid_configure(row=5, column=1, columnspan=5)
            self.a_notifier.configure(text="Email Taken", text_color="red")
            self.window.after(3000, lambda: self.a_notifier.grid_forget())       
            return
        
        update_info(self.id, email=email)
        self.email.set(email)
        self.a_notifier.grid_configure(row=5, column=1, columnspan=5)
        self.a_notifier.configure(text="Changed Email Successfully", text_color="green")
        self.window.after(3000, lambda: self.a_notifier.grid_forget()) 
    
    # Signs user out and takes them back to login screen
    def sign_out(self):
        self.id = None
        self.current_screen.grid_forget()
        self.current_screen = self.login_screen_init()
        self.current_screen.grid_configure(row=1, column=1)
    
    # Deletes user account and signs them out.
    def delete_account(self):
        
        def countdown(counter):            
            if counter == 0:
                self.window.after(3000, lambda: self.a_notifier.grid_forget()) 
                delete_user(self.id)
                self.sign_out()
                return
                
            self.a_notifier.grid_configure(row=5, column=1, columnspan=5)
            self.a_notifier.configure(text=f"Deleting account in {counter}...", text_color="red")
            self.window.after(1000, countdown, counter-1) 
            
        countdown(5)
        