import requests
from pprint import pprint 
base_url = 'https://fr.openfoodfacts.org/cgi/search.pl?'
url_tags =  {
    'name' : ('product_name', 'generic_name', 'generic_name_LANG_COD'),
    'nutrition_grade' : ('nutrition_grades', 'nutrition_grades_tags'),
    'image' : ('image_small_url', 'image_thumb_url', 'image_url'),
    'brands' : ('brands'),
    'additives' : ('additives_original_tags', 'additives_prev_tags'),
    'countries' : ('countries_tags'),
    'ingredients' : ('ingredients_text', 'ingredients_tags'),
    'allergen' : ('allergens_tags', 'allergens'),
    'date' : ('last_edit_dates_tags'),
    }
categories = {
    'snacks' : 'snacks',
    'breakfasts' : 'breakfasts',

}

page_size = 20

def get_search_url(category, page_size, page):
    """ This method creates the products url needed """
    params = {
        'action' : 'process',
        'tagtype_0' : 'categories',
        'tag_contains_0' : 'contains',
        'tag_0' : category,
        'page_size' : page_size,
        'page' : page,
        'json' : '1'
    }
    response = requests.get(base_url, params=params)
    status = response.status_code
    if status < 400:
        return response.json()
    else:
        raise RuntimeError('response status: {}'.format(status))

def get_url(category, page_size):
    page = 1
    for product in range(10):
        url = get_search_url(category, page_size, page)
        if len(url['products']) == 0:
            break        
        page +=1
    return url            

def get_products(url):
    products = url["products"]
    return products


def main():
    p = get_url('snacks', 1)
    pprint(get_products(p))

#     pprint(p['products'][0])
    #products = get_search_url('snacks', 50, 681)
if __name__ == "__main__":
    main()