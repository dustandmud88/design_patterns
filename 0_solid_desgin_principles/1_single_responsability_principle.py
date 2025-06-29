import json
import os.path


class Book:

    def __init__(self, book_id, title, author, price_usd):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price_usd = price_usd


class PersistentManager:

    @staticmethod
    def save_object_to_json_file(file_path, object_to_convert):

        attributes_dict = vars(object_to_convert)
        dict_to_save = {attributes_dict["book_id"]: attributes_dict}
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                temp_data = json.load(file)

            temp_data.update(dict_to_save)
            with open(file_path, "w") as file:
                json.dump(temp_data, fp=file, indent=4, sort_keys=True)

        else:
            with open(file_path, "w") as file:
                json.dump(dict_to_save, fp=file, indent=4)


"""
According to single responsibility principle we don't overload objects
with too many responsibilities. In this way we avoid:
- Classes become too large: reduce complexity
- Modifying code in many places if fix is needed because functionality
is isolated and so, change will not impact other parts of code just one part:
 easier to maintain

In this example the persistence of book object functionality is stored 
in a separate class called PersistentManager and not inside the Book class
"""

book2 = Book("2", "Mastering Python Design Patterns",
             " Kamon Ayeva y Sakis Kasampalis", "31.19")
PersistentManager.save_object_to_json_file("books.json", book2)

book1 = Book("1", "Sumérgete en los patrones de diseño",
             "Alexander Shvets", "30")
PersistentManager.save_object_to_json_file("books.json", book1)
