import tkinter as tk


class CurrentNoteGUI:
    def __init__(self, frame, selected_note, save_note):
        print('making current note', selected_note)

        scroll = tk.Scrollbar(frame)

        text = tk.Text(frame)
        text.insert('end', selected_note["Content"])
        button = tk.Button(text="Save", command=lambda: self.save(selected_note, save_note, text))

        scroll.pack(side='right', fill='y')
        text.pack(side='left', fill='y')
        button.pack(side='bottom')

        scroll.config(command=text.yview)
        text.config(yscrollcommand=scroll.set)
        print(text.get(1.0, 'end'))

    def save(self, selected_note, save_note, text):
        new_note = dict(selected_note)
        new_note["Content"] = text.get(1.0, 'end')
        save_note(new_note)

    # def delete(self, selected_note):

