import tkinter as tk
from all_notes_gui import AllNotesGUI
from current_note_gui import CurrentNoteGUI


class GUI:
    def __init__(self,
                 all_notes,
                 current_note,
                 new_note,
                 select_note,
                 save_note,
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

        self.AllNotesGUI = AllNotesGUI(
                    all_notes,
                    frame=notes_frame,
                    select_note=select_note
                    )

        self.CurrentNoteGUI = CurrentNoteGUI(
            frame=current_note_frame,
            selected_note=current_note,
            save_note=save_note,
        )

        root.title('pack test')
        root.geometry('800x600')
        root.mainloop()

        def update_selected_note(self, selected_note):
            print('hello is this thing on')
            self.CurrentNoteGUI.update_selected_note(selected_note)
