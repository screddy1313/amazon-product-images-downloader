# amazon-product-images-downloader
Given a product name, the python program downloads all the images. This includes pagenation also.

## Description 

Often times, we need to download all the images of products. These images can be useful to gather data for 
Machine Learning / Deep learning projects. 

This program takes 3 inputs from the user :
- Product name : This product name is entered in amazon search box and products are retrieved.
- Number of items : Optional, default 100. These many number of product images to be downloaded.
- Number of pages : optional, default 10. These many number of pages will be traversed to download the product images.

All the downloaded images will be stored in images folder, where name of image is its asin-id (unique amazon product id).
Make sure that images folder exists in working directory.

## Libraries Used :
- Selenium : To automate the amazon search and for pagenation
- Beautiful Soup 4 : To parse the html content
- python 3.6
- requests : to download the image from the url

#### Install
```
// Linux
python3 -V // Ensure 3.6+
pip3 -V // Ensure... pip3

pip3 install selenium
pip3 install webdriver_manager
pip3 install requests
pip3 install beautifulsoup4
pip3 install lxml

// Linux only
sudo apt install chromium-chromedriver
```

## Usage : 
Make sure all the above mentioned libraries are installed. </br>
python product_images_downloader.py  ( look the output images directory to get the idea !!)

## Debugging :
If you're a filthy degenerate hiding behind a proxy and the amazon captcha shows up, run the following

> $ python3
```
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.amazon.in')
// Solve the captcha
exit()
// Close the browser
```

That should stave off the bots for a few extra runs.
## Things to do :
- Eliminate the images of sponsored products.
- Extracting all the details of product (name, price, ratings) and storing in csv. 
