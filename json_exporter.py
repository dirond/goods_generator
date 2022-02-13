
from settings import OUT_JSON


def write_json(products, fname=OUT_JSON):
    """
    Function saves the JSON object to a file
    :param products: JSON object
    :param fname: name of saving file
    :return: None
    """
    with open(fname, 'w') as f:
        f.write(products)
