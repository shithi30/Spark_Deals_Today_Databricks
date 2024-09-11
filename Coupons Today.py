# import
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# setup
from pyvirtualdisplay import Display
Display(visible = 0, size = (1920, 1080)).start()

# window
driver = webdriver.Chrome()
driver.get("https://www.retailmenot.com/ca")

# soup
soup = BeautifulSoup(driver.page_source, "html.parser")
soup = soup.find_all("div", attrs = {"class": "relative flex h-full flex-col justify-center p-2 md:justify-start"})

# accumulators
coupon_df = pd.DataFrame()
company = []
offer = []
if_coupon_available = []

# scrape
for s in soup:
    # company
    try: val = s.find("h3", attrs = {"class": "text-xs font-bold uppercase tracking-wide md:mt-2"}).get_text()
    except: val = None
    company.append(val)
    # offer on coupon
    try: val = s.find("p", attrs = {"class": "my-2 line-clamp-2 font-proxima text-base capitalize leading-5 md:mb-auto md:line-clamp-3"}).get_text()
    except: val = None
    offer.append(val)
    # if available
    try: val = s.find("p", attrs = {"class": "mt-2 text-xs font-bold uppercase tracking-wide text-purple-700 lg:mb-1"}).get_text()
    except: val = None
    if_coupon_available.append(val)

# accumulate
coupon_df["company"] = company
coupon_df["offer"] = offer
coupon_df["availability"] = if_coupon_available
coupon_df["report_date"] = (datetime.now() - timedelta(hours = 4)).strftime("%d-%b-%Y, %I:%M:%S %p")

# save
coupon_df.to_parquet("coupons_promos_today.parquet", engine = "pyarrow")

# end
print("Total offers found: " + str(coupon_df.shape[0]))
driver.close()
