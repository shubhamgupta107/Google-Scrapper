from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
bang1=["Koramangala","Indiranagar","M.G. Road","HSR Layout","Richmond Town","Jayanagar","BTM Layout","Sarjapur","Whitefield","Bannerghatta Road","Malleswaram","Kammanahalli","Basavanagudi","Marathahalli","Bellandur","Yelahanka","Hebbal","KR Puram","Banashankari","Electronic City"]
mum1=['Andheri', 'Mira Bhayandar', 'Bandra', 'Borivali', 'Dahisar', 'Goregaon', 'Jogeshwari', 'Juhu', 'Kandivali west', 'Kandivali east', 'Khar', 'Malad', 'Santacruz', 'Vasai', 'Virar', 'Vile Parle', 'Bhandup', 'Ghatkopar', 'Kanjurmarg', 'Kurla', 'Mulund', 'Powai', 'Vidyavihar', 'Vikhroli', 'Chembur', 'Govandi', 'Mankhurd', 'Trombay', 'Antop Hill', 'Byculla', 'Colaba', 'Dadar', 'Fort', 'Girgaon', 'Kalbadevi', 'Kamathipura', 'Matunga', 'Parel', 'Tardeo']
hyd1=["Kapra", "Uppal", "Hayathnagar", "LB Nagar", "Saroornagar", "Malakpet", "Santhoshnagar", "Chandrayangutta", "Charminar", "Falakunuma", "Rajendra Nagar","Mehdipatnam", "Karwan", "Goshamahal", "Khairatabad", "Jubilee Hills", "Amberpet", "Musheerabad", "Malkajgiri", "Secunderabad", "Begumpet", "Yousufguda","Serilingampally", "Chandanagar", "Ramachandra", "Moosapet", "Kukatpally", "Quthbullapur", "Gajula", "Alwal"]
che1=["Thiruvottiyur", "Manali", "Madhavaram", "Tondiarpet", "Royapuram", "Thiru. Vi. Ka. Nagar", "Ambattur", "Anna Nagar", "Teynampet", "Kodambakkam", "Valasaravakkam","Alandur", "Adyar", "Perungudi", "Sholinganallur"]
kol1=["Cossipore", "Chitpur", "Sinthee", "Baranagar", "Bonhoohgly", "Dunlop", "Jorasanko", "Sovabazar", "Ultadanga", "Dum Dum", "Jadavpur", "Santoshpur", "Kasba","Gariahat", "Kalighat", "Tollygunge", "Behala", "Barisha", "Taratala", "Naktala", "Patuli", "Garia", "Joka", "Raja Bazar", "Kankurgachi", "Bowbazar", "Ballygunge", "Taltala", "Tangra", "Lalbazar", "Esplanade", "Park Street", "Lake Town", "Bidhannagar", "Kaikhali", "Rajbari", "Baguiati", "Kestopur", "Rajarhat", "New Town"]
pun1=["Aamby Valley City", "Alandi" "Amanora Park Town", "Ambegaon", "Baramati", "Bhor", "Bhosari", "Chakan", "Chas Ghodegaon", "Chinchwad", "Daund", "Dehu", "Dehu Road", "Dhayari", "Ganj Peth", "Ghatghar", "Gurholi", "Guruwar Peth", "Hadapsar", "Haveli", "Indapur", "Jejuri", "Junnar", "Karli", "Kasarwadi", "Khadkale", "Khadki", "Khodad", "Kusgaon Budruk", "Lavasa", "Lonavala", "Malavli", "Manchar", "Manjri", "Maval", "Moshi", "Murum Village", "Narayangaon", "Nira", "Pimpri", "Pimpri-Chinchwad", "Pirangut", "Pune Metropolitan Region", "Raireshwar", "Rajgurunagar (Khed)", "Saswad", "Shirur", "Shivatkar (Nira)", "Talegaon Dabhade", "Tathavade", "Vadgaon Budruk", "Vadgaon Maval", "Warje"]
gur1=["IMT Manesar", "Dhorka" , "Baslambi", "Kharkari", "Mokalwas","Kukrola","Panchgaon", "Sehrawan","Nainwal", "Naurangpur","Kasan", "Naharpura Kasan","Meoka" ,"Jhund Sarai Viran","Patli Hajiur", "Khaintawas", "Sihi", "Sector 83", "Sadrana", "Dhankot", "Kherki Majra", "Tikampur", "Behrampur", "Sarai Alawardi", "Kanahi", "Ghata", "Nirvana Country", "Tikri","Suncity","DLF Cyber City", "Phase V", "Maruti Udyog", "Palam Vihar", "Inayatpur", "Hamirpur", "Sultanpur"]
del1=["Connaught Place","Chanakyapuri","Delhi Cantonment","Vasant Vihar","Alipur","Model Town","Narel","Alipur", "Kanjhawala","Rohini","Kanjhawala","Saraswati Vihar","Rajouri Garden","Patel Nagar","Punjabi Bagh","Rajouri Garden","Dwarka","Najafgarh","Kapashera","Saket","Hauz Khas","Mehrauli","Defence Colony","Kalkaji","Sarita Vihar","Daryaganj","Kotwali","Civil Lines","Karol Bagh","Nand Nagri","Seelampur","Yamuna Vihar","Karawal Nagar","Shahdara","Seemapuri","Vivek Vihar","Preet Vihar","Gandhi Nagar","Preet Vihar","Mayur Vihar"]
place_names={"Mumbai":mum1,"Bangalore":bang1,"Pune":pun1,"Delhi":del1,"Gurgaon":gur1,"Kolkata":kol1,"Chennai":che1,"Hyderabad":hyd1}
shops=["salon","restaurant"]
#lon=80
#lat=100
#zoom=12
webdriver = "/home/shubham/chromedriver"
def change(driver,ind):
	t1=driver.find_elements_by_class_name("gm2-caption")
	if(len(t1)==0):
		return False
	else:
		t2=t1[0].find_element_by_class_name('n7lv7yjyC35__left').text
		temp="Showing results "+str((1+ind)*20+1)+" "
		if(t2.split('-')[0]==temp):
			print(temp)
			return True
		else:
			print(t2,temp)
			return False

driver = Chrome(webdriver)
for shop in shops:

	writer = pd.ExcelWriter('{}_data.xlsx'.format(shop), engine='xlsxwriter')  # pylint: disable=abstract-class-instantiated
	for place in place_names:
		total = []
		for area in place_names[place]:
			place1=(shop+" in "+place+" "+area).replace(' ','+')
			#url = "https://www.google.com/maps/search/"+place1+"/@"+str(lon)+","+str(lat)+","+str(zoom)+"z/"
			url = "https://www.google.com/maps/search/"+place1+"/"
			driver.get(url)
			index=0
			while True:
				results = driver.find_elements_by_class_name("section-result-text-content")
				for result in results:
					name=None
					try:
						name = result.find_element_by_class_name('section-result-title').text
					except:
						name=None
					finally:
						location=None
						try:
							location = result.find_element_by_class_name('section-result-location').text
						except:
							location=None
						finally:
							details=None
							try:
								details = result.find_element_by_class_name('section-result-details').text
							except:
								details=None
							finally:
								contact=None
								try:
									contact = result.find_element_by_class_name('section-result-phone-number').text
								except:
									contact=None
								finally:
									rating=None
									try:
										rating = result.find_element_by_class_name('section-result-rating').text
									except:
										rating=None
									finally:
										new = ((name,location,details,contact,rating,area))
										if(name!=None):
											total.append(new)
				try:
					driver.find_element_by_id("n7lv7yjyC35__section-pagination-button-next").click()
				except:
					break
				finally:
					try:
					    element = WebDriverWait(driver, 20).until(
					        lambda driver: change(driver,index)
					    )
					except:
						break
					finally:
					    driver.implicitly_wait(1)
					    index+=1
		df = pd.DataFrame(total,columns=['NAME','LOCATION','DETAILS','CONTACT','RATING','AREA'])
		df=df.set_index('NAME')
		df = df.loc[~df.index.duplicated(keep='first')]
		df.to_excel(writer,sheet_name=place)
	writer.save()
driver.close()