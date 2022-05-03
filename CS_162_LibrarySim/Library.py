# Author: Angela Montez
# Github Username: almontez
# Date: 01/19/2022
# Description: Library simulator with check out, return, and request capabilities that can
#               charge members fees for overdue items

class LibraryItem:
    """Represents an item that can be found in a library"""

    def __init__(self, item_id, title):
        """Initializes LibraryItem fields"""
        self._library_item_id = item_id
        self._title = title
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None
        self._location = "ON_SHELF"

    def get_location(self):
        """Returns the location of a library item"""
        return self._location

    def set_location(self, new_location):
        """Updates the location of a library item"""
        self._location = new_location

    def get_checked_out_by(self):
        """Returns the date of a checked out library item"""
        return self._checked_out_by

    def set_checked_out_by(self, patron_id):
        """Updates who checked out item"""
        self._checked_out_by = patron_id

    def get_requested_by(self):
        """Returns the id of patron requesting library item"""
        return self._requested_by

    def set_requested_by(self, patron_id):
        """Updates who requested item"""
        self._requested_by = patron_id

    def get_date_checked_out(self):
        """Returns the day a library item was checked out"""
        return self._date_checked_out

    def set_date_checked_out(self, new_day):
        """Update check out date of item"""
        self._date_checked_out = new_day

    def get_item_id(self):
        """Returns the id of a library item"""
        return self._library_item_id

    def get_title(self):
        """Returns the title of a library item"""
        return self._title


class Book(LibraryItem):
    """Represents a Book item with inheritance from LibraryItem class"""

    def __init__(self, item_id, title, author):
        """Initializes Book fields"""
        super().__init__(item_id, title)
        self._author = author
        self._check_out_length = 21

    def get_check_out_length(self):
        """Returns the number of days a book can be checked out"""
        return self._check_out_length

    def get_author(self):
        """Returns the author of book"""
        return self._author


class Album(LibraryItem):
    """Represents an Album item with inheritance from LibraryItem class"""

    def __init__(self, item_id, title, artist):
        """Initializes Album fields"""
        super().__init__(item_id, title)
        self._artist = artist
        self._check_out_length = 14

    def get_check_out_length(self):
        """Returns the number of days an album can be checked out"""
        return self._check_out_length

    def get_artist(self):
        """Returns the artist of an album"""
        return self._artist


class Movie(LibraryItem):
    """Represents a Movie item with inheritance from LibraryItem class"""

    def __init__(self, item_id, title, director):
        """Initializes Movie fields"""
        super().__init__(item_id, title)
        self._director = director
        self._check_out_length = 7

    def get_check_out_length(self):
        """Returns the number of days a movie can be checked out"""
        return self._check_out_length

    def get_director(self):
        """Returns the director for a movie"""
        return self._director


class Patron:
    """Represents a Patron who can check out library item"""

    def __init__(self, patron_id, name):
        """Initializes Patron fields"""
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_fine_amount(self):
        """Returns the amount due for overdue items"""
        return self._fine_amount

    def add_library_item(self, library_item):
        """Adds library item to checked_out_items"""
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        """Removes library item from checked_out_items"""
        self._checked_out_items.remove(library_item)

    def get_checked_out_items(self):
        """Returns list of checked out items for a patron"""
        return self._checked_out_items

    def amend_fine(self, amount):
        """Updates amount due for fines"""
        # positive value increases the fine_amount
        # negative value decreases the fine_amount
        self._fine_amount += amount

    def get_patron_name(self):
        """Returns the name of patron"""
        return self._name

    def get_patron_id(self):
        """Returns patron id"""
        return self._patron_id


class Library:
    """Represents a library with check out, return, request, and fine methods"""

    def __init__(self):
        """Initializes library fields"""
        self._holdings = {}
        self._members = {}
        self._current_day = 0

    def add_library_item(self, library_item):
        """Adds items to library collection"""
        item_id = library_item.get_item_id()
        self._holdings[item_id] = library_item

    def lookup_library_item_from_id(self, item_id):
        """Returns a LibraryItem object corresponding to the item id"""
        if item_id in self._holdings:
            return self._holdings[item_id]
        else:
            return None

    def add_patron(self, patron):
        """Adds patron to members"""
        patron_id = patron.get_patron_id()
        self._members[patron_id] = patron

    def lookup_patron_from_id(self, patron_id):
        """Returns a Patron object corresponding to patron id"""
        if patron_id in self._members:
            return self._members[patron_id]
        else:
            return None

    def check_out_library_item(self, patron_id, item_id):
        """Checks out valid items to valid patrons"""

        if patron_id not in self._members:
            return "patron not found"
        if item_id not in self._holdings:
            return "item not found"

        requested_by = self._holdings[item_id].get_requested_by()
        if requested_by is not None and requested_by != patron_id:
            return "item on hold by other patron"
        if self._holdings[item_id].get_location() == "CHECKED_OUT":
            return "item already checked out"
        else:
            # update item fields
            self._holdings[item_id].set_checked_out_by(patron_id)
            self._holdings[item_id].set_date_checked_out(self._current_day)
            self._holdings[item_id].set_location("CHECKED_OUT")

            # update item requested by status
            if patron_id == self._holdings[item_id].get_requested_by():
                self._holdings[item_id].set_requested_by(None)

            # add item to patron's checked_out_items
            item = self._holdings[item_id]
            self._members[patron_id].add_library_item(item)

            return "check out successful"

    def return_library_item(self, item_id):
        """Updates library item's status and location after being returned"""

        if item_id not in self._holdings:
            return "item not found"
        if self._holdings[item_id].get_location() != "CHECKED_OUT":
            return "item already in library"
        else:
            # remove returned item from patron's checked out items
            patron_id = self._holdings[item_id].get_checked_out_by()
            item = self._holdings[item_id]
            self._members[patron_id].remove_library_item(item)

            # update location of returned item
            if self._holdings[item_id].get_requested_by() is not None:
                self._holdings[item_id].set_location("ON_HOLD_SHELF")
            else:
                self._holdings[item_id].set_location("ON_SHELF")

            self._holdings[item_id].set_checked_out_by(None)

            return "return successful"

    def request_library_item(self, patron_id, item_id):
        """Places an item on hold for a patron"""

        if patron_id not in self._members:
            return "patron not found"
        if item_id not in self._holdings:
            return "item not found"
        if self._holdings[item_id].get_requested_by() is not None:
            return "item already on hold"
        else:
            self._holdings[item_id].set_requested_by(patron_id)

            # update location of requested item if ON_SHELF only
            if self._holdings[item_id].get_location() == "ON_SHELF":
                self._holdings[item_id].set_location("ON_HOLD_SHELF")

            return "request successful"

    def pay_fine(self, patron_id, amount_paid):
        """Updates patron's fines due"""
        if patron_id not in self._members:
            return "patron not found"
        else:
            self._members[patron_id].amend_fine(-1 * amount_paid)
            return "payment successful"

    def increment_current_date(self):
        """Increases days open and calculates fine due"""
        self._current_day += 1
        fines_due = 0

        # get patron's checked out items
        for patron_id in self._members:
            patron_items = self._members[patron_id].get_checked_out_items()
            # get individual library item in checked out items
            for library_item in patron_items:
                days_checked_out = self._current_day - library_item.get_date_checked_out()
                check_out_length = library_item.get_check_out_length()
                if days_checked_out > check_out_length:
                    fines_due += .10

            self._members[patron_id].amend_fine(fines_due)
            fines_due = 0

    def get_holdings(self):
        """Returns all items that belong to library"""
        return self._holdings

    def get_members(self):
        """Returns a collection of library patrons"""
        return self._members
