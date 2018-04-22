import tkinter as tk


class AllNotesGUI:
    def __init__(self, all_notes, frame, select_note):
        self.create_gui_elements(all_notes, frame, select_note)

    def create_gui_elements(self, all_notes, frame, select_note):
        for note in all_notes:
            # SelectableNote(note, frame, select_note)
            self.make_selectable_note(note, frame, select_note)

    def make_selectable_note(self, note, frame, select_note):
        label = tk.Label(frame, text=note['Content'])
        label.bind("<Button-1>", lambda x: select_note(note))
        label.pack()