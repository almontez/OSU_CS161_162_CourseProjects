# Author: Angela Montez
# GitHub username: almontez
# Date: 01/12/2022
# Description: Unit Test for LemonadeStand program

import unittest
from LemonadeStand import MenuItem, SalesForDay, LemonadeStand


class TestLemonadeStand(unittest.TestCase):

    def test_name_of_stand(self):
        """Tests get_name() method in LemonadeStand class"""
        stand = LemonadeStand('Jolly Juice')
        self.assertEqual(stand.get_name(), 'Jolly Juice')

    def test_item_added_to_menu(self):
        """Tests add_menu_item() method in LemonadeStand class"""
        stand = LemonadeStand('Jolly Juice')
        item1 = MenuItem('lemonade', .5, 1.5)
        stand.add_menu_item(item1)
        self.assertIn('lemonade', stand._menu)

    def test_creation_of_Sales_for_day_obj(self):
        """Tests enter_sales_for_today() method to check that a SalesForDay object is created"""
        stand = LemonadeStand('Jolly Juice')

        item1 = MenuItem('lemonade', .5, 1.5)
        stand.add_menu_item(item1)

        day0 = {'lemonade': 5}
        stand.enter_sales_for_today(day0)
        self.assertIsInstance(stand._sales_for_day[0], SalesForDay)

    def test_validity_of_sales_record(self):
        stand = LemonadeStand('Jolly Juice')

        item1 = MenuItem('lemonade', .5, 1.5)
        stand.add_menu_item(item1)

        day0 = {'lemonade': 5}
        stand.enter_sales_for_today(day0)

        # get record for day 0
        added_dict = stand.get_sales_dict_for_day(0)

        # assert retrieved dict and original dict are the same
        self.assertEqual(day0, added_dict)

    def test_accuracy_of_total_items_sold(self):
        """Tests total_sales_for_menu_item() method in LemonadeStand class"""
        stand = LemonadeStand('Jolly Juice')

        item1 = MenuItem('lemonade', .5, 1.5)
        stand.add_menu_item(item1)

        day0 = {'lemonade': 5}
        day1 = {'lemonade': 5}
        day2 = {'lemonade': 6}

        stand.enter_sales_for_today(day0)
        stand.enter_sales_for_today(day1)
        stand.enter_sales_for_today(day2)

        self.assertEqual(stand.total_sales_for_menu_item('lemonade'), 16)

    def test_total_profit_for_single_item(self):
        """Tests total_profit_for_menu_item() method in LemonadeStand Class"""
        stand = LemonadeStand('Jolly Juice')

        item1 = MenuItem('lemonade', .5, 1.5)
        stand.add_menu_item(item1)

        day0 = {'lemonade': 5}
        day1 = {'lemonade': 5}
        day2 = {'lemonade': 6}

        stand.enter_sales_for_today(day0)
        stand.enter_sales_for_today(day1)
        stand.enter_sales_for_today(day2)

        self.assertAlmostEqual(stand.total_profit_for_menu_item('lemonade'), 16.0)

    def test_total_profit_for_stand(self):
        """Tests total_profit_for_stand() method in LemonadeStand Class"""
        stand = LemonadeStand('Jolly Juice')

        item1 = MenuItem('lemonade', .5, 1.5)
        stand.add_menu_item(item1)

        item2 = MenuItem('cookie', .2, 1)
        stand.add_menu_item(item2)

        item3 = MenuItem('dog treat', .3, 6)
        stand.add_menu_item(item3)

        day0 = {'lemonade': 5, 'cookie': 2, 'dog treat': 5}
        day1 = {'lemonade': 5, 'cookie': 1, 'dog treat': 1}

        stand.enter_sales_for_today(day0)
        stand.enter_sales_for_today(day1)

        self.assertAlmostEqual(stand.total_profit_for_stand(), 46.6)
