from bs4 import BeautifulSoup
import requests
import csv
import sys

def main(argv):

    URL = argv[1]
    File = open("title.csv", "a")
    
    writer = csv.writer(File)
    HEADERS = ({'User-Agent':
                 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})



    html_doc = requests.get(URL , headers = HEADERS) 
    soup = BeautifulSoup(html_doc.text, 'html.parser') 
    
  
    try:
        title = soup.find_all("span" ,{'class': 'a-size-base-plus a-color-base a-text-normal'})
        title_list = []
        for text in title:

            title_strip = text.get_text().replace(',', '').encode("utf-8")
            title_list.append(title_strip)
        
    except AttributeError:
        str_title = "NA"                
    
   

    try:
        price = soup.find_all("span", {'class':'a-price-whole'})
        price_list = []
       
        for pr in price:
            
                price_strip = pr.get_text().replace(',', '').encode("utf-8")
                price_list.append(price_strip)
                
                

             
    except AttributeError:
        price = "NA" 
    
    writer.writerows([title_list])
    writer.writerows([price_list])
if __name__ == "__main__":
    main(sys.argv)

#main('https://www.amazon.com/s?k=hhd&crid=1LBCOBUKIJS3W&sprefix=hh%2Caps%2C192&ref=nb_sb_noss_2')
#main('https://www.amazon.com/s?k=ssd&crid=191KTLBDKLR17&sprefix=ss%2Caps%2C748&ref=nb_sb_noss_2')  
#main('https://www.amazon.com/b?node=16225016011&pf_rd_r=YTVZMPFEP9YXHZAHDBV2&pf_rd_p=e5b0c85f-569c-4c90-a58f-0c0a260e45a0&pd_rd_r=ad2d4c1f-6b53-4e70-be94-796cabecd1d9&pd_rd_w=7WaiY&pd_rd_wg=3Vwk0&ref_=pd_gw_unk')