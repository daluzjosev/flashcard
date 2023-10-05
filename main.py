import customtkinter
import deckmanager as dm

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



dM = dm.DeckManager

class FlashcardApp:

    def __init__(self, root):

        frame = customtkinter.CTkFrame(master=root)
        frame.pack(fill="both", expand=True)

        title = customtkinter.CTkLabel(master=frame, text="Flashcard App", font=("Ink free", 48))
        title.pack(padx="20", pady="20", anchor="nw")
        
        label = customtkinter.CTkLabel(frame, text="Choose deck")
        label.pack()
        #check database for deck titles
        optionmenu = customtkinter.CTkOptionMenu(frame, values=["option 1", "option 2"],
                                         command=dM.new_deck)
        optionmenu.set("option 2")
        optionmenu.pack()
        




root = customtkinter.CTk()
root.geometry("1000x600")

FlashcardApp(root)
root.mainloop()
