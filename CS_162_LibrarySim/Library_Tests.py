# Author: Angela Montez
# GitHub username: almontez
# Date: 01/19/2022
# Description: Unit Tests for Library Simulator

import unittest
from Library import LibraryItem, Book, Album, Movie, Patron, Library


class TestLibraryItem(unittest.TestCase):

    def test_get_id(self):
        item1 = LibraryItem("A1", "Baby")
        self.assertEqual(item1.get_item_id(), "A1")

    def test_get_title(self):
        item1 = LibraryItem("A1", "Baby")
        self.assertEqual(item1.get_title(), "Baby")

    def test_checked_out(self):
        item1 = LibraryItem("A1", "Baby")
        self.assertEqual(item1.get_checked_out_by(), None)

        item1.set_checked_out_by("Dog1")
        self.assertEqual(item1.get_checked_out_by(), "Dog1")

    def test_requested_by(self):
        item1 = LibraryItem("A1", "Baby")
        self.assertEqual(item1.get_requested_by(), None)

        item1.set_requested_by("Dog1")
        self.assertEqual(item1.get_requested_by(), "Dog1")

    def test_dated_checked_out(self):
        item1 = LibraryItem("A1", "Baby")
        self.assertEqual(item1.get_date_checked_out(), None)

        item1.set_date_checked_out(100)
        self.assertEqual(item1.get_date_checked_out(), 100)

    def test_location(self):
        item1 = LibraryItem("A1", "Baby")
        self.assertEqual(item1.get_location(), "ON_SHELF")

        item1.set_location("ON_HOLD_SHELF")
        self.assertEqual(item1.get_location(), "ON_HOLD_SHELF")

        item1.set_location("CHECKED_OUT")
        self.assertEqual(item1.get_location(), "CHECKED_OUT")


class TestBook(unittest.TestCase):

    def test_book_fields(self):
        book1 = Book("b1", "Leaves of Grass", "Walt Whitman")
        self.assertEqual(book1.get_author(), "Walt Whitman")
        self.assertEqual(book1.get_title(), "Leaves of Grass")
        self.assertEqual(book1.get_item_id(), "b1")
        self.assertEqual(book1.get_check_out_length(), 21)


class TestAlbum(unittest.TestCase):

    def test_album_fields(self):
        album1 = Album("a1", "Bombs Away", "Sheppard")
        self.assertEqual(album1.get_artist(), "Sheppard")
        self.assertEqual(album1.get_title(), "Bombs Away")
        self.assertEqual(album1.get_item_id(), "a1")
        self.assertEqual(album1.get_check_out_length(), 14)


class TestMovie(unittest.TestCase):

    def test_movie_fields(self):
        movie1 = Movie("m1", "Shang-Chi", "D.D. Cretton")
        self.assertEqual(movie1.get_director(), "D.D. Cretton")
        self.assertEqual(movie1.get_title(), "Shang-Chi")
        self.assertEqual(movie1.get_item_id(), "m1")
        self.assertEqual(movie1.get_check_out_length(), 7)


class TestPatron(unittest.TestCase):

    def test_patron_identification(self):
        patron1 = Patron("p1", "JoJo")
        self.assertEqual(patron1.get_patron_id(), "p1")
        self.assertEqual(patron1.get_patron_name(), "JoJo")

    def test_checked_out_items(self):
        patron1 = Patron("p1", "Angela")
        book1 = Book("b1", "Leaves of Grass", "W. Whitman")
        book2 = Book("b2", "Dub", "A.P. Gumbs")

        patron1.add_library_item(book1)
        patron_items = patron1.get_checked_out_items()
        self.assertIn(book1, patron_items)

        patron1.add_library_item(book2)
        patron_items = patron1.get_checked_out_items()
        self.assertIn(book2, patron_items)

        patron1.remove_library_item(book1)
        patron_items = patron1.get_checked_out_items()
        self.assertNotIn(book1, patron_items)

    def test_fines(self):
        patron1 = Patron("p1", "Angela")
        amount_owed = patron1.get_fine_amount()
        self.assertEqual(amount_owed, 0)

        patron1.amend_fine(10.26)
        amount_owed = patron1.get_fine_amount()
        self.assertAlmostEqual(amount_owed, 10.26)

        patron1.amend_fine(-10.26)
        amount_owed = patron1.get_fine_amount()
        self.assertAlmostEqual(amount_owed, 0)


class TestLibrary(unittest.TestCase):

    def test_holdings(self):
        lib = Library()
        book1 = Book("b1", "Leaves of Grass", "W.Whitman")
        book2 = Book("b2", "Dub", "A.P. Gumbs")

        lib.add_library_item(book1)
        lib.add_library_item(book2)
        holdings = lib.get_holdings()

        item_obj = holdings['b1']
        self.assertEqual(book1, item_obj)

        item_obj = holdings['b2']
        self.assertEqual(book2, item_obj)

        self.assertEqual(book1, lib.lookup_library_item_from_id('b1'))
        self.assertEqual(None, lib.lookup_library_item_from_id('b3'))

    def test_membership(self):
        lib = Library()
        patron1 = Patron("p1", "Angela")
        patron2 = Patron("p2", "JoJo")

        lib.add_patron(patron1)
        lib.add_patron(patron2)

        members = lib.get_members()

        patron_obj = members['p1']
        self.assertEqual(patron1, patron_obj)

        patron_obj = members['p2']
        self.assertEqual(patron2, patron_obj)

        self.assertEqual(patron1, lib.lookup_patron_from_id('p1'))
        self.assertEqual(None, lib.lookup_patron_from_id('p3'))

    def test_check_out_items(self):
        lib = Library()

        book1 = Book("b1", "Leaves of Grass", "W.Whitman")
        book2 = Book("b2", "Dub", "A.P. Gumbs")

        lib.add_library_item(book1)
        lib.add_library_item(book2)

        patron1 = Patron("p1", "Angela")
        patron2 = Patron("p2", "JoJo")

        lib.add_patron(patron1)
        lib.add_patron(patron2)

        # Test for empty list
        self.assertEqual(patron1.get_checked_out_items(), [])

        # Test item has been added to patron's checked_out_items
        lib.check_out_library_item('p1', 'b1')
        self.assertIn(book1, patron1.get_checked_out_items())

        # Test accurate date checked out
        self.assertEqual(book1.get_date_checked_out(), 0)

        # Test logic for item already checked out
        self.assertEqual(lib.check_out_library_item('p2', 'b1'), 'item already checked out')

        # Test logic for item on hold by other patron
        book2.set_requested_by('p1')
        self.assertEqual(lib.check_out_library_item('p2', 'b2'), "item on hold by other patron")

        # Test that patron can check out item held for them
        self.assertEqual(lib.check_out_library_item('p1', 'b2'), "check out successful")

        # Test item or patron not found
        self.assertEqual(lib.check_out_library_item('p2', 'b3'), "item not found")
        self.assertEqual(lib.check_out_library_item('p3', 'b2'), "patron not found")

    def test_return_item(self):
        lib = Library()

        book1 = Book("b1", "Leaves of Grass", "W.Whitman")
        book2 = Book("b2", "Dub", "A.P. Gumbs")

        lib.add_library_item(book1)
        lib.add_library_item(book2)

        patron1 = Patron("p1", "Angela")
        patron2 = Patron("p2", "JoJo")

        lib.add_patron(patron1)
        lib.add_patron(patron2)

        lib.check_out_library_item('p1', 'b1')
        lib.check_out_library_item('p1', 'b2')

        lib.return_library_item('b1')
        self.assertNotIn(book1, patron1.get_checked_out_items())
        self.assertEqual(book1.get_location(), "ON_SHELF")
        self.assertEqual(book1.get_checked_out_by(), None)

        book1.set_requested_by('p2')
        self.assertEqual(book1.get_location(), "ON_HOLD_SHELF")

    def test_request_item(self):
        lib = Library()

        book1 = Book("b1", "Leaves of Grass", "W.Whitman")
        book2 = Book("b2", "Dub", "A.P. Gumbs")

        lib.add_library_item(book1)
        lib.add_library_item(book2)

        patron1 = Patron("p1", "Angela")
        patron2 = Patron("p2", "JoJo")

        lib.add_patron(patron1)
        lib.add_patron(patron2)

        self.assertEqual(lib.request_library_item('p1', 'b1'), "request successful")
        self.assertEqual(book1.get_requested_by(), 'p1')
        self.assertEqual(book1.get_location(), "ON_HOLD_SHELF")

        book2.set_requested_by('p2')
        self.assertEqual(lib.request_library_item('p1', 'b2'), "item already on hold")

    def test_pay_fines(self):
        lib = Library()
        patron1 = Patron("p1", "Angela")

        lib.add_patron(patron1)

        patron1.amend_fine(100)
        lib.pay_fine('p1', -10.50)

        self.assertAlmostEqual(patron1.get_fine_amount(), 89.50)

    def test_fines_due(self):
        lib = Library()

        book1 = Book('b1', "Leaves of Grass", "W.Whitman")
        album1 = Album('a1', "album", 'artist')
        movie1 = Movie('m1', "movie", 'director')
        book2 = Book('b2', "Dub", "A.P. Gumbs")

        lib.add_library_item(book1)
        lib.add_library_item(album1)
        lib.add_library_item(movie1)
        lib.add_library_item(book2)

        patron1 = Patron("p1", "Angela")
        patron2 = Patron("p2", "JoJo")

        lib.add_patron(patron1)
        lib.add_patron(patron2)

        lib.check_out_library_item('p1', 'b1')
        lib.check_out_library_item('p1', 'b2')
        # lib.check_out_library_item('p1', 'm1')
        # lib.check_out_library_item('p2', 'a1')

        for i in range(57):
            lib.increment_current_date()

        self.assertAlmostEqual(patron1.get_fine_amount(), 7.20)

        lib.pay_fine('p1', 7.20)
        self.assertAlmostEqual(patron1.get_fine_amount(), 0)
        # self.assertAlmostEqual(patron2.get_fine_amount(), 4.30)
