from bs4 import BeautifulSoup
from amazon_sel import Amazon
import requests
import sys

# required functions


def extract_product_divs(html):
    # these are different layouts of amazon product divs
    different_web_ele_selectors = [
        'div.sg-col-4-of-12.s-result-item.s-asin.sg-col-4-of-16.sg-col.sg-col-4-of-20',
        'div.s-result-item.s-asin.sg-col-0-of-12.sg-col-16-of-20.sg-col.sg-col-12-of-16'
    ]

    for pattern in different_web_ele_selectors:
        product_divs = html.select(pattern)

        if len(product_divs) > 0:
            break  # it means page is grid. No need to check for other alignment

    return product_divs


def extract_images(product_divs):

    # just a wrapper to iterate each product and extract img-link

    for i in range(len(product_divs)):   # for each product
        # for any product, this unique id will be present...
        uid = product_divs[i].get('data-asin')
        try:

            prod = product_divs[i]

            img_link = prod.find('img').get('src')

            download_img(img_link, uid)   # download img and saves the image

        except:
            print(uid)   # products for which image is failed to download
            continue


def download_img(img_url, uid):

    # it will store elements in the images folder. make sure it already exists !!!
    img = requests.get(img_url).content

    with open(f'output/{uid}.jpg', 'wb') as f:
        f.write(img)


# we ask user to enter the product to be searched, and number of items or pages
def input_details():
    '''

        Helper function to get details from the user !!!

    '''
    print('\nEnter the Details\n')
    item_name = input('Enter the name of product to be searched : ')

    if not item_name:
        # without product name, we cannot scrape anything...
        return -1

    num_pages = input(
        'Enter the number of pages to be traversed. (default: 10)')

    if not num_pages:
        num_pages = 10  # default

    else:
        num_pages = int(num_pages)

    print('-' * 50)
    print('Entered Details : \n')
    print(f'Item  :\t {item_name}')
    print(f'Number of pages to be processed  :\t {num_pages}')

    print('-' * 50)

    return item_name, num_pages


def print_details(count, pages, completed=False):

    if not completed:
        if (count % 25 == 0) or (pages % 5 == 0):

            print('=' * 50)
            print(
                f'\nProducts extracted: {count}\nPages Traversed : {pages}\n')
            print('=' * 50)

    else:
        # prints for the last time !!
        print('=' * 30+' Final Details ' + '=' * 30)
        print(
            f'\nTotal Number of Products extracted: {count}\nTatal Pages Traversed : {pages}\n')
        print('=' * 50)


def main():

    print(sys.executable)   # just to check we are in correct env or not !!!

    # take the input details
    # iterate till one of condition met !!

    details = input_details()

    if details == -1:
        sys.exit('Exiting Since product name is not entered !!')

    item_name, num_pages = details[0], details[1]
    
    ama_search = Amazon()  # instantiate amazon search class
    pg_src = ama_search.search_text(item_name)

    pages_traversed = 0
    count_products = 0

    # break when required products count is reached or req of pages are traversed !!!

    while (pages_traversed < num_pages):

        html = BeautifulSoup(pg_src, 'lxml')
        # extract the actual product divs
        product_divs = extract_product_divs(html)



        # will download all the images of extracted products
        extract_images(product_divs)

        # Inc the prods count
        count_products += len(product_divs)

        pg_src = ama_search.next_page()   # open next page....

        if pg_src == -1:
            print('Extraction Completed !!')
            break

        pages_traversed += 1

        # helper func to print details
        print_details(count_products, pages_traversed)

    print_details(count_products, pages_traversed,
                  True)  # print all the details


if __name__ == main():
    main()
