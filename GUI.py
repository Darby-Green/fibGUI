import customtkinter

from fib import fib

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry('500x400')

def call():
    numb = int(entry.get())
    print(fib(numb))


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = customtkinter.CTkLabel(master=frame, text='Fib Producer')
label.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(master=frame, placeholder_text='Fib no. to produce')
entry.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text='Enter', command=call)
button.pack(pady=12, padx=10)

root.mainloop()
