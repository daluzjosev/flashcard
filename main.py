import customtkinter
import deckmanager as dm


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


dM = dm.DeckManager()


class FlashcardApp:
    def __init__(self, root):
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(fill="both", expand=True)

        title = customtkinter.CTkLabel(
            master=frame, text="Flashcard App", font=("Ink free", 48)
        )
        title.pack(padx="20", pady="20", anchor="nw")

        # check database for deck titles
        optionmenu = customtkinter.CTkOptionMenu(
            frame,
            values=dM.decks,
            command=dM.select_deck,
        )
        optionmenu.set("Select Deck")
        optionmenu.pack()
        button = customtkinter.CTkButton(frame, text="New Deck", command=)


root = customtkinter.CTk()
root.geometry("1000x600")

FlashcardApp(root)
root.mainloop()
