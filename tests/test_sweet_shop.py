
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
