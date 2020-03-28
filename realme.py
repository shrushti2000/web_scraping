#REALME PHONES
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url1="https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme&sort=price_asc"
uClient=uReq(my_url1)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
containers=page_soup.findAll("div",{"class":"_3O0U0u"})
#print(len(containers))
#print(soup.prettify(containers[0]))

filename="Realme.csv"
f=open(filename,"w")

headers="Product_Name,Pricing,Rating\n"
f.write(headers)

for container in containers:
	prodname=container.div.img["alt"]

	print(prodname)
	prodprice=container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
	pp=prodprice[0].text.strip()

	print(pp)
	prodrating=container.findAll("div",{"class":"niH0FQ"})
	pr=prodrating[0].text

	trim_price=''.join(pp.split(','))
	rm_rupee=trim_price.split("₹")
	add_rs_price="Rs."+rm_rupee[1]
	split_price=add_rs_price.split('E')
	final_price=split_price[0]

	split_rating=pr.split(" ")
	final_rating=split_rating[0]

	print(prodname.replace(",","|")+","+final_price +","+final_rating+"\n")
	f.write(prodname.replace(",","|")+","+final_price +","+final_rating+"\n")
print("*"*30)
f.close()

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url2="https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme&sort=price_asc&page=2"
uClient=uReq(my_url2)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
containers=page_soup.findAll("div",{"class":"_3O0U0u"})
#print(len(containers))
#print(soup.prettify(containers[0]))

#filename="products.csv"
f=open(filename,"a")

#headers="Product_Name,Pricing,Rating\n"
#f.write(headers)

for container in containers:
	prodname=container.div.img["alt"]

	print(prodname)
	prodprice=container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
	pp=prodprice[0].text.strip()

	print(pp)
	prodrating=container.findAll("div",{"class":"niH0FQ"})
	pr=prodrating[0].text

	trim_price=''.join(pp.split(','))
	rm_rupee=trim_price.split("₹")
	add_rs_price="Rs."+rm_rupee[1]
	split_price=add_rs_price.split('E')
	final_price=split_price[0]

	split_rating=pr.split(" ")
	final_rating=split_rating[0]

	print(prodname.replace(",","|")+","+final_price +","+final_rating+"\n")
	f.write(prodname.replace(",","|")+","+final_price +","+final_rating+"\n")
print("*"*30)
f.close()

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url2="https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme&sort=price_asc&page=3"
uClient=uReq(my_url2)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
containers=page_soup.findAll("div",{"class":"_3O0U0u"})
#print(len(containers))
#print(soup.prettify(containers[0]))

#filename="products.csv"
f=open(filename,"a")

#headers="Product_Name,Pricing,Rating\n"
#f.write(headers)

for container in containers:
	prodname=container.div.img["alt"]

	print(prodname)
	prodprice=container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
	pp=prodprice[0].text.strip()

	print(pp)
	prodrating=container.findAll("div",{"class":"niH0FQ"})
	pr=prodrating[0].text

	trim_price=''.join(pp.split(','))
	rm_rupee=trim_price.split("₹")
	add_rs_price="Rs."+rm_rupee[1]
	split_price=add_rs_price.split('E')
	final_price=split_price[0]

	split_rating=pr.split(" ")
	final_rating=split_rating[0]

	print(prodname.replace(",","|")+","+final_price +","+final_rating+"\n")
	f.write(prodname.replace(",","|")+","+final_price +","+final_rating+"\n")
print("*"*30)
f.close()



