import notes.note as NoteModel

class Actions:

    def create(self, user):
        print(f"\nOk {user[1]}, let's create a new note'")

        title = input("Enter your note title:  ")
        description = input("Enter your note description: ")

        note = NoteModel.Note(user[0], title, description)
        save = note.save()

        if save[0] >= 1:
            print(f"\nPerfect, you have saved the note:  {note.title}")

        else:
            print(f"\nThe note has not been saved")

    def show(self, user):
        print(f"\nOk {user[1]}, here are your notes:  ")

        note = NoteModel.Note(user[0])
        notes = note.listNotes()

        for note in notes:
            print(f"\n***************************")
            print(note[2])
            print(note[3])
            print(f"***************************")

    def delete(self, user):
        print(f"\nOk {user[1]}, let's delete a note")

        title = input("Enter your note title:  ")

        note = NoteModel.Note(user[0], title)
        delete = note.deleteNote()

        if delete[0] >= 1:
            print(f"\nYou have deleted the note: {note.title}")
        else:
            print(f"\n No note was deleted")