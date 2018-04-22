from GUI import GUI


class Application:
    def __init__(self):
        print('Application init')
        # init notes, init current note, init GUI.
        note1 = {
            'Id': 1,
            'Content': 'note 1',
            'Date': '',
        }
        note2 = {
            'Id': 2,
            'Content': 'note 2',
            'Date': ''
        }
        self.allNotes = [note1, note2]
        self.currentNote = self.allNotes[1:]
        GUI(
            allnotes=self.allNotes,
            currentnote=self.currentNote,
            new_note=self.new_note,
            select_note=self.select_note,
        )

    def new_note(self):
        print('making a new note now')

    def select_note(self, selected_note):
        self.currentNote = selected_note
        print(self.currentNote)
