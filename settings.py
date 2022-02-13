"""
Here is a script settings.
JSON_FIELDS according to the TOR and no provide for adding new fields, without changes in the code
In case a new category is added to the CATEGORIES, it also needs to be updated WEIGHTS and TYPES
"""

JSON_FIELDS = (
    'id', 'article', 'category',
    'weight', 'type', 'color',
    'textile', 'description'
)
# List of characteristics for generating goods
CATEGORIES = (
    'outwear', 'shirt', 'socks'
)

MATERIALS = (
    'cotton', 'silk', 'polyester',
    'viscose', 'acrylic'
)

WEIGHTS = {
    'outwear': (1000, 10000),
    'shirt': (100, 2000),
    'socks': (10, 300)
}

TYPES = {
    'outwear': ('coat', 'jacket', 'windbreaker'),
    'shirt': ('casual', 'dress', 'loosefit'),
    'socks': ()  # According to the TOR, socks are not typed
}

# Outgoing files names
OUT_XLSX = 'product_list.xlsx'
OUT_JSON = 'product_list.json'
