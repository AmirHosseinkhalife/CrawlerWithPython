from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import datetime


# sites = []

# sites.append({
#     "sitemap" : "https://meghdadit.com/product-sitemap-2.xml",
#     "SiteName" :"",
#     "priceId" :"",
#     "imageId":"",
#     "titleId":""
# })


# آدرس فایل سایت مپ
sitemap_url = "https://meghdadit.com/product-sitemap-2.xml"

# دریافت فایل سایت مپ
response = requests.get(sitemap_url)

# تبدیل محتوای فایل به یک شیء XML
root = ET.fromstring(response.content)


product_urls = []

# پیدا کردن تمام المان‌های مورد نظر
for child in root:
    # اگر المان با تگ "url" باشد، اطلاعات مورد نیاز رو استخراج کنید
    if child.tag.endswith("url"):
        loc = child.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
        # lastmod = child.find("{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod").text
        # changefreq = child.find("{http://www.sitemaps.org/schemas/sitemap/0.9}changefreq").text
        # priority = child.find("{http://www.sitemaps.org/schemas/sitemap/0.9}priority").text
        product_urls.append(loc)

for productUrl in product_urls:
    start_time = datetime.datetime.now()
    # Start TopLearn
    number_Page_Toplearn = requests.get(productUrl, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    )
    soupToplearn = BeautifulSoup(number_Page_Toplearn.content, 'html.parser')
    price = soupToplearn.find(id="SharedHead_head_mtaProductPrice").get('content')
    image = soupToplearn.find(id="SharedMessage_ContentPlaceHolder1_imgItem").get('src')
    title = soupToplearn.find(id="SharedMessage_ContentPlaceHolder1_lblItemTitle").contents
    titleEn = soupToplearn.find(id="SharedMessage_ContentPlaceHolder1_lblItemTitle2").contents
    # data = {
    #     "Price": price,
    #     "Image":image,
    #     "Title":title,
    #     "Engli":titleEn

    # }
    print('URL : '+str(productUrl))
    print('price : '+str(price))
    print('image : '+str(image))
    print('title : '+str(title))
    print('titleEn : '+str(titleEn))
    end_time = datetime.datetime.now()

    print(end_time - start_time)
    print('________________________________________ PRODUCTS ________________________________________')
