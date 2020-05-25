from tkinter import *
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import Create_key, RSA_genKey, Decrypt, Encrypt
from tkinter import messagebox
from tkinter import filedialog

def run():
    root = Tk()

    root.title("Menu")

    global Dict_data
    Dict_data = {}

    def button_create_RSA_key(entry,layer):
        password = entry.get()
        print(password)
        res = RSA_genKey.generate_key(password)
        if res:
            respond = messagebox.showinfo("Create New RSA key", "See folder ./keys to get privatekey and publickey")
            if(respond == "ok"):
                layer.destroy()

    def button_choose_key_file(layer,Dict):
        filename = filedialog.askopenfilename(initialdir = parent_dir, title = "Choose AES key file", filetypes=(("key file","*.key"),("all files","*.*")))
        label = Label(layer, text = "Keyfile : " + filename)
        Dict["keyfile"] = filename
        label.grid(row = 0, column = 0, padx = 3, pady=3)
        
    def button_choose_file(layer,Dict):
        filename = filedialog.askopenfilename(initialdir = parent_dir, title = "Choose File need encrypt", filetypes=(("text file", "*.txt"),("all files","*.*")))
        label = Label(layer, text = "File : " + filename)
        Dict["inputfile"] = filename
        label.grid(row = 1, column = 0, padx = 3, pady=3)

    def button_choose_file_2(layer,Dict):
        filename = filedialog.askopenfilename(initialdir = parent_dir, title = "Choose File need encrypt", filetypes=(("text file", "*.txt"),("all files","*.*")))
        label = Label(layer, text = "File : " + filename)
        Dict["inputfile2"] = filename
        label.grid(row = 3, column = 0, padx = 3, pady=3)

    def button_choose_key(layer,type,Dict):
        filename = filedialog.askopenfilename(initialdir = parent_dir, title = "Choose File need encrypt", filetypes=(("pem file", "*.pem"),("all files","*.*")))
        if type:
            label = Label(layer, text = "Private_key : " + filename)
            Dict["private_key"] = filename
            label.grid(row = 3, column = 0, padx = 3, pady=3)
        else:
            label = Label(layer, text = "Public_key : " + filename)
            Dict["public_key"] = filename
            label.grid(row = 2, column = 0, padx = 3, pady=3)
        

    def button_check(layer, entry, type, data):
        if not type:
            #Encrypt
            password = entry.get()
            res = Encrypt.Encrypt_File(data["keyfile"], data["inputfile"], data["public_key"], (data["private_key"],password))
            messagebox.showinfo("Encrypt", res)
        else:
            #Decrypt
            password = entry.get()
            res = Decrypt.Decrypt_File(data["inputfile"], data["public_key"], (data["private_key"],password))
            messagebox.showinfo("Decrypt", res)

    def button_check_2(layer, data):
        res = Decrypt.CheckIntergity(data["inputfile"], data["inputfile2"], data["public_key"])
        messagebox.showinfo("Encrypt", res)

    def button_cancel(layer):
        response = messagebox.askokcancel("Cancel ", "Are you want to cancel?")
        if response:
            layer.destroy()

    def button_click(case):
        if case == 1:
            Create_key.generate_new_Fernet_key()
            messagebox.showinfo("Create New AES key", "New key was stored in key.key")
        elif case == 2:
            top = Toplevel()
            top.title("Create Pair RSA keys")
            e = Entry(top,width = 50)
            e.pack()
            e.insert(0, "Enter your password for create private key")
            Button(top, text = "Create", command= lambda :button_create_RSA_key(e,top)).pack()
        elif case == 3:
            top = Toplevel()
            top.title("---Encrypt file---")

            Dict_data["keyfile"] = None
            Dict_data["inputfile"] = None
            Dict_data["public_key"] = None
            Dict_data["private_key"] = None
                
            Button(top, text= "------Key file-----" , command = lambda: button_choose_key_file(top,Dict_data)).grid(row = 0, column = 1, padx = 3, pady = 3)
            Button(top, text= "File Need Encrypt", command= lambda:button_choose_file(top,Dict_data)).grid(row = 1, column = 1, padx = 3, pady = 3)
            Button(top, text= "Public_key of receiver", command= lambda:button_choose_key(top,0,Dict_data)).grid(row = 2, column = 1, padx = 3, pady = 3)
            Button(top, text= "Private_key of you", command= lambda:button_choose_key(top,1,Dict_data)).grid(row = 3, column = 1, padx = 3, pady = 3)
            e = Entry(top, width = 50)
            e.insert(0, "Enter your password of private key")
            e.grid(row = 4, column = 1, padx = 3, pady = 3)
            Button(top, text= "Encrypt", command= lambda:button_check(top, e, 0, Dict_data)).grid(row = 5, column = 0, padx = 3, pady = 3,sticky = E)
            Button(top, text = "Cancel", command = lambda: button_cancel(top)).grid(row = 5, column = 1, padx = 3, pady = 3, sticky= E)

        elif case == 4:
            top = Toplevel()
            top.title("---Decrypt file---")

            Dict_data["inputfile"] = None
            Dict_data["public_key"] = None
            Dict_data["private_key"] = None
                
            Button(top, text= "File Need Decrypt", command= lambda:button_choose_file(top,Dict_data)).grid(row = 1, column = 1, padx = 3, pady = 3)
            Button(top, text= "Public_key of sender", command= lambda:button_choose_key(top,0,Dict_data)).grid(row = 2, column = 1, padx = 3, pady = 3)
            Button(top, text= "Private_key of you", command= lambda:button_choose_key(top,1,Dict_data)).grid(row = 3, column = 1, padx = 3, pady = 3)
            e = Entry(top, width = 50)
            e.insert(0, "Enter your password of private key")
            e.grid(row = 4, column = 1, padx = 3, pady = 3)
            Button(top, text= "Decrypt", command= lambda:button_check(top, e, 1, Dict_data)).grid(row = 5, column = 0, padx = 3, pady = 3,sticky = E)
            Button(top, text = "Cancel", command = lambda: button_cancel(top)).grid(row = 5, column = 1, padx = 3, pady = 3, sticky= E)
        
        else: 
            top = Toplevel()
            top.title("-Check Integrity of file-")

            Dict_data["inputfile"] = None
            Dict_data["inputfile2"] = None
            Dict_data["public_key"] = None
                
            Button(top, text= "File Decrypted", command= lambda:button_choose_file(top,Dict_data)).grid(row = 1, column = 1, padx = 3, pady = 3)
            Button(top, text= "Public_key of sender", command= lambda:button_choose_key(top,0,Dict_data)).grid(row = 2, column = 1, padx = 3, pady = 3)
            Button(top, text= "File Ecrypted", command= lambda:button_choose_file_2(top,Dict_data)).grid(row = 3, column = 1, padx = 3, pady = 3)
            Button(top, text= "Check", command= lambda:button_check_2(top, Dict_data)).grid(row = 5, column = 0, padx = 3, pady = 3,sticky = E)
            Button(top, text = "Cancel", command = lambda: button_cancel(top)).grid(row = 5, column = 1, padx = 3, pady = 3, sticky= E)


    button_create_new_key = Button(root, text = "Create New AES key" , padx=40 ,pady=30, command= lambda: button_click(1))

    button_create_new_pair_key = Button(root, text = "Create Pair RSA keys" , padx=40 ,pady=30, command= lambda: button_click(2))

    button_encrypt_file = Button(root, text = "---Encrypt file---" , padx=40 ,pady=30, command= lambda: button_click(3))

    button_decrypt_file = Button(root, text = "---Decrypt file---" , padx=40 ,pady=30, command= lambda: button_click(4))

    Button(root, text = "-Check Integrity of file-" , padx=40 ,pady=30, command= lambda: button_click(5)).grid(row = 4, padx = 2, pady = 2)

    Button(root, text = "Cancel", padx=20 ,pady=20, command = lambda: button_cancel(root)).grid(row = 5, padx = 2, pady = 2)

    button_create_new_key.grid(row = 0, padx = 2, pady = 2)
    button_create_new_pair_key.grid(row = 1, padx = 2, pady = 2)
    button_encrypt_file.grid(row = 2, padx = 2, pady = 2)
    button_decrypt_file.grid(row = 3, padx = 2, pady = 2)

    root.mainloop()
