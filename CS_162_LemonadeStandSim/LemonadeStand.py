# Author: Angela Montez
# GitHub username: almontez
# Date: 01/12/2022
# Description: Program for running a lemonade stand including creating menu items and recording daily sales and profit

class InvalidSalesItemError(Exception):
    pass


class MenuItem:
    """Represents items to be sold at a lemonade stand"""

    def __init__(self, item_name, item_cost, item_price):
        """Initializes the name, cost, and sale's price for menu items in a lemonade stand"""
        self._name = item_name
        self._wholesale_cost = item_cost
        self._selling_price = item_price

    def get_name(self):
        """Returns the name of a menu item for a lemonade stand"""
        return self._name

    def get_wholesale_cost(self):
        """Returns the wholesale cost of a menu item for a lemonade stand"""
        return self._wholesale_cost

    def get_selling_price(self):
        """Returns the sale's price of a menu item for a lemonade stand"""
        return self._selling_price


class SalesForDay:
    """Represents the total sales of menu items given a particular day for a day"""

    def __init__(self, days_open, items_sold_dict):
        """Initializes days open and sales info for menu item"""
        self._days = days_open
        self._sales_dict = items_sold_dict

    def get_day(self):
        """Returns the number of days a lemonade stand has been open"""
        return self._days

    def get_sales_dict(self):
        """Returns a dictionary of items sold with the amount sold for any given day"""
        return self._sales_dict


class LemonadeStand:
    """Blueprint for a lemonade stand with methods for stand name, menu items, sales, and profit"""

    def __init__(self, name_of_stand):
        """Initializes the stand name, days open, menu items, and sales"""
        self._name = name_of_stand
        self._current_day = 0
        self._menu = {}
        self._sales_for_day = []

    def get_name(self):
        """Returns lemonade stand name"""
        return self._name

    def add_menu_item(self, menu_item_obj):
        """Adds items to the lemonade stand menu"""
        obj_name = menu_item_obj.get_name()
        self._menu[obj_name] = menu_item_obj

    def get_menu(self):
        """Returns dictionary of menu items"""
        return self._menu

    def enter_sales_for_today(self, sales_today):
        """Create new SalesForDay object if all items sold are on menu"""
        # check validity of dictionary
        is_valid = True
        for item in sales_today:
            if item not in self._menu:
                is_valid = False

        # add dictionary to sales record
        if is_valid:
            new_sales_for_day_obj = SalesForDay(self._current_day, sales_today)
            self._sales_for_day.append(new_sales_for_day_obj)
        else:
            raise InvalidSalesItemError

        self._current_day += 1

    def get_sales_dict_for_day(self, day):
        """Returns a dictionary of sales for all menu items for a given day"""
        sales_for_given_day = self._sales_for_day[day]
        sales_dict = sales_for_given_day.get_sales_dict()
        return sales_dict

    def total_sales_for_menu_item(self, name_of_menu_item):
        """Returns the total amount of an item sold over the duration of a particular lemonade stand"""
        total_amount_sold = 0

        for obj in self._sales_for_day:
            sales_dict = obj.get_sales_dict()
            total_amount_sold += sales_dict[name_of_menu_item]

        return total_amount_sold

    def total_profit_for_menu_item(self, name_of_menu_item):
        """Returns the total profit of a menu item over the history of a particular lemonade stand"""
        item_name = self._menu[name_of_menu_item]

        amount_sold = self.total_sales_for_menu_item(name_of_menu_item)
        cost_per_item = item_name.get_wholesale_cost()
        selling_price_per_item = item_name.get_selling_price()

        total_cost_of_item = amount_sold * cost_per_item
        total_value_sold = amount_sold * selling_price_per_item

        total_profit_of_item = total_value_sold - total_cost_of_item

        return total_profit_of_item

    def total_profit_for_stand(self):
        """Returns the total profit of all items sold over the history of a lemonade stand"""
        total_profit_over_time = 0

        for item in self._menu:
            total_profit_of_item = self.total_profit_for_menu_item(item)
            total_profit_over_time += total_profit_of_item

        return total_profit_over_time


def main():
    stand = LemonadeStand('Lemons R Us')

    item1 = MenuItem('lemonade', .5, 1.5)
    stand.add_menu_item(item1)

    item2 = MenuItem('cookie', .2, 1)
    stand.add_menu_item(item2)

    day0 = {'lemonade': 5, 'cookie': 2, 'dog treat': 3}

    try:
        stand.enter_sales_for_today(day0)
    except InvalidSalesItemError:
        print("One of the items sold is not on the menu.")


if __name__ == '__main__':
    main()
