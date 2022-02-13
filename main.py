import json
from builder import products_builder
from xlsx_exporter import write_xlsx
from json_exporter import write_json

if __name__ == '__main__':
    while True:
        num = input('Type number of products:')
        try:
            num = int(num)
        except ValueError:
            print('Please type a number with a digit.')
        if isinstance(num, int):
            break

    products = json.dumps(products_builder(num), indent=2)
    write_json(products)

    # Additional task - save list of generated products to xlsx file
    write_xlsx(products)
