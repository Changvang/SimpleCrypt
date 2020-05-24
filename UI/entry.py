from tkinter import *
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import Create_key, RSA_genKey, Decrypt, Encrypt
from tkinter import messagebox

def run():
    root = Tk()

    root.title("Menu")

    def button_create_RSA_key(entry,layer):
        password = entry.get()
        print(password)
        res = RSA_genKey.generate_key(password)
        if res:
            respond = messagebox.showinfo("Create New RSA key", "See folder ./keys to get privatekey and publickey")
            if(respond == "ok"):
                layer.destroy()

    def button_choose_key_file():


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
            top.Toplevel()
            top.title("---Encrypt file---")

            global keyfile, inputfile, public_key, private_key, password

            Button(top, text= "Key file" , command = button_choose_key_file)
            Button(top, text= "File Need Encrypt", command= button_choose_file)
            Button(top, text= "Public_key of receiver", command= button_choose_public_key)
            Button(top, text= "Private_key of you", command= button_choose_private_key)
            Button(top, text= "Password to authentication private Key", command= button_input_password)
            Button(top, text= "Encrypt", command= button_check)


        else:
            pass

    button_create_new_key = Button(root, text = "Create New AES key" , padx=40 ,pady=30, command= lambda: button_click(1))

    button_create_new_pair_key = Button(root, text = "Create Pair RSA keys" , padx=40 ,pady=30, command= lambda: button_click(2))

    button_encrypt_file = Button(root, text = "---Encrypt file---" , padx=40 ,pady=30, command= lambda: button_click(3))

    button_decrypt_file = Button(root, text = "---Decrypt file---" , padx=40 ,pady=30, command= lambda: button_click(4))

    button_create_new_key.grid(row = 0, padx = 2, pady = 2)
    button_create_new_pair_key.grid(row = 1, padx = 2, pady = 2)
    button_encrypt_file.grid(row = 2, padx = 2, pady = 2)
    button_decrypt_file.grid(row = 3, padx = 2, pady = 2)

    root.mainloop()
