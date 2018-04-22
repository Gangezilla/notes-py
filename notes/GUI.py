import tkinter as tk
from all_notes_gui import AllNotesGUI


class GUI:
    def __init__(self,
                 allnotes,
                 currentnote,
                 new_note,
                 select_note,
                 ):
        root = tk.Tk()

        notes_frame = tk.Frame(root)
        notes_frame.pack(side='left')

        current_note_frame = tk.Frame(root)
        current_note_frame.pack(side='right')

        menu_frame = tk.Frame(root)
        menu_frame.pack(side='top')

        button = tk.Button(menu_frame, text='New', command=new_note)
        button.pack()

        AllNotesGUI(allnotes,
                    frame=notes_frame,
                    select_note=select_note
                    )

        root.title('pack test')
        root.geometry('800x600')
        root.mainloop()

# allow clicking on a label, change current note
