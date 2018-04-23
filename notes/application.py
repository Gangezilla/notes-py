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
        self.currentNote = self.allNotes[0]
        GUI(
            all_notes=self.allNotes,
            current_note=self.currentNote,
            new_note=self.new_note,
            select_note=self.select_note,
            save_note=self.save_note,
        )

    def new_note(self):
        print('making a new note now')

    def delete_note(self):
        print('d=time to delete')

    def select_note(self, selected_note):
        self.currentNote = selected_note
        print(self.currentNote)

    def save_note(self, new_note):
        print('saving note', new_note)
        note_index = self.find(self.allNotes, "Id", new_note["Id"])
        self.allNotes[note_index] = new_note
        print('here!', self.allNotes)

    def find(self, lst, key, value):
        for i, dic in enumerate(lst):
            if dic[key] == value:
                return i
        return -1

