# Console Interface
from db import MessageDatabase
import rsa_utils


class SecretNotes:
    def __init__(self):
        self.db = MessageDatabase()
        self.public_key, self.private_key = rsa_utils.generate_keys()

    def add_note(self, note):
        encrypted_data = rsa_utils.encrypt(note, self.public_key)
        return self.db.save_message(str(encrypted_data))

    def view_note(self, note_id):
        note = self.db.get_message_by_id(note_id)
        if note:
            encrypted_data = eval(note[1])
            decrypted_text = rsa_utils.decrypt(
                encrypted_data, self.private_key)
            return decrypted_text
        return None

    def list_all_notes(self):
        return self.db.get_all_messages()


def main():
    notes = SecretNotes()
    print("\n=== Secret Notes ===")

    while True:
        print("\n1. Add Note")
        print("2. View Note")
        print("3. List Notes")
        print("4. Exit")

        choice = input("\nChoice (1-4): ")

        if choice == '1':
            note = input("Enter note: ")
            note_id = notes.add_note(note)
            print(f"Saved with ID: {note_id}")

        elif choice == '2':
            try:
                note_id = int(input("Enter Note ID: "))
                decrypted = notes.view_note(note_id)
                if decrypted:
                    print("\n=== Note ===")
                    print(f"Decrypted message: {decrypted}")
                else:
                    print("Note not found!")
            except ValueError:
                print("Invalid ID!")

        elif choice == '3':
            all_notes = notes.list_all_notes()
            if all_notes:
                print("\n=== All Notes ===")
                for note in all_notes:
                    print(f"ID: {note[0]}, Created: {note[2]}")
            else:
                print("No notes found!")

        elif choice == '4':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
