	https://selenium-python.readthedocs.io/getting-started.html
	
	this is python documentation and selectors are given in the modele selectors
	
	if you are extracting data with xpath end with [.get attribute('attribute')]
	
	if some part are dynamic in nature then text don’t work perfectly and the remedy for this is at end=[ .get attribute('attribute')]
	
	simple text ke liye text nautanki ke liye .get attri
	
	for a adynamic site height code = 
	
	driver.execute_script("return document.body.scrollHeight")
	
	use a while true for ending script=
	
	height = 0
	while True:
	new_height = height code
	if new_height == height
		break  
	scroll code
	sleep(3)
	
	if there is button as readmore or load more then use its body.
	
	
	
	
	
	
	using keys= like end key
	
	driver.find_elements(By_XPATHS, path).send_keys(Keys.END)
	
	
	
	 
	
	
	
	
	If I want to scrape with out loading of website then -
	
	Code in shell teminal

	1. python learn2
	2. quit()
	3. from selenium import web driver
	4. driver = webdriver.Chrome()
	5. driver.get('https://www.fjlabs.com/portfolio')
	6. driver.find_elements(By_XPATHS, path).get attribute('attribute')
	7. container [1].find_elements(By_XPATHS,path).get attribute('attribute')
	#if there are many containers in one container then nesting can be done
	8. 
	

