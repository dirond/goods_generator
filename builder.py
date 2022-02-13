from faker import Faker
from string import ascii_uppercase
from settings import JSON_FIELDS, CATEGORIES, MATERIALS, WEIGHTS, TYPES
from collections import OrderedDict as od
from typing import Union


def gen_article(category, fake: Faker) -> str:
    """
    Generates article
    :param fake:
    :param category: product category
    :return: product article
    """
    code = fake.bothify(text='??##', letters=ascii_uppercase)
    return f'OZON_{category}_{code}'


def gen_category(categories, fake: Faker) -> str:
    """
    Generates category of product
    :param fake: Faker() instance
    :param categories: list of possible categories from options
    :return: product category
    """
    return fake.word(ext_word_list=categories)


def gen_weight(category, fake: Faker) -> int:
    """
    Generates product weight according list of possible weights from options
    :param fake: Faker() instance
    :param category: category of product
    :return: product weight
    """
    category_weight = WEIGHTS.get(category)
    return fake.random_int(min=category_weight[0], max=category_weight[1])


def gen_type(category, fake: Faker) -> Union[str, None]:
    """
    Generates type of product
    :param fake: Faker() instance
    :param category: category of product
    :return: type of product or None if product has no available type. e.g. category "socks"
    """
    category_type = TYPES.get(category)
    return fake.word(category_type) if category_type else None


def gen_color(fake: Faker) -> str:
    """
    Generates color of product
    :param fake: Faker() instance
    :return: color of product
    """
    return fake.color_name()


def gen_percents(number_of_materials, fake: Faker) -> list:
    """
    Generates percents of materials in textile.
    :param number_of_materials: number of materials in textile
    :param fake: Faker() instance
    :return: list of percents

    """
    percents = []
    _max = 100 - number_of_materials
    for _ in range(number_of_materials):
        if sum(percents) < 100:
            percent = fake.random_int(min=1, max=_max)
            percents.append(percent)
        _max = 100 - sum(percents)
    percents[0] += 100 - sum(percents)
    return percents


def gen_textile(fake: Faker) -> dict:
    """
    Generates textile of product
    :param fake: Faker() instance
    :return: dictionary with materials and their percentage
    """
    materials = fake.random_elements(MATERIALS, unique=True)
    material_percents = gen_percents(len(materials), fake)
    return dict(zip(materials, material_percents))


def gen_description(fake: Faker) -> str:
    """
    Generate description of product
    :param fake: Faker() instance
    :return: description of product
    """
    return fake.text(max_nb_chars=140)


def products_builder(number_of_products):
    """
    Builds list of dictionaries with generated products
    :param number_of_products: number of products
    :return: list of dictionaries
    """
    products = []
    fake = Faker()
    for num in range(1, number_of_products + 1):
        prd_id = num
        prd_category = gen_category(CATEGORIES, fake)
        prd_article = gen_article(prd_category, fake)
        prd_weignt = gen_weight(prd_category, fake)
        prd_type = gen_type(prd_category, fake)
        prd_color = gen_color(fake)
        prd_textile = gen_textile(fake)
        prd_description = gen_description(fake)
        product = od(zip(JSON_FIELDS,
                         (prd_id, prd_article, prd_category, prd_weignt,
                          prd_type, prd_color, prd_textile, prd_description)))
        if product.get('type') is None:  # According TOR, products without type not contain key "type"
            del (product['type'])
        products.append(product)
    return products
