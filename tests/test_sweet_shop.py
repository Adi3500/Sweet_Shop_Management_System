
# Add project root to sys.path for import to work
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the SweetShop class from your package
from sweet import SweetShop
import pytest

# Test: Adding a sweet successfully

def test_add_sweet():
    shop = SweetShop()
    shop.add_sweet(1, "Ladoo", "Pastry", 10.0, 20)
    sweets = shop.view_sweets()
    assert len(sweets) == 1
    assert sweets[0]["name"] == "Ladoo"

# Test: Adding a sweet with missing fields
# Should raise ValueError

def test_add_missing_fields():
    shop = SweetShop()
    with pytest.raises(ValueError):
        shop.add_sweet(None, "", "Candy", None, None)

# Test: Deleting a sweet by ID

def test_delete_sweet():
    shop = SweetShop()
    shop.add_sweet(2, "Barfi", "Candy", 15.0, 5)
    shop.delete_sweet(2)
    assert shop.view_sweets() == []

# Test: Searching for sweet by name

def test_search_by_name():
    shop = SweetShop()
    shop.add_sweet(3, "Peda", "Pastry", 12.0, 10)
    results = shop.search_sweets(name="Peda")
    assert len(results) == 1
    assert results[0]["category"] == "Pastry"



