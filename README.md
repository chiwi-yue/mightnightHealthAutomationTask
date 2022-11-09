# mightnightHealthAutomationTask

The following task should be taken as an opportunity to highlight your skills using Python and Selenium. 
In your solution, you are free to use whichever webdriver (ChromeDriver, GeckoDriver, etc.) that you wish.


Q: HOW to use it?
A: Easy as following. 
  1) clone the repo
  2) Just input AXS company full name, e.g.: BHP GROUP LIMITED, hit ENTER.
  3) The 'stock.csv' file will be created at the same folder ./demo/

KNOWN ISSUE:
 - It might have some flake testing due AXS server response
 - If error just re-run the CLI
 
 
% python3 retrieveASX.py
Companyname: > 

>>>>>>>>>>>>>>>>>>>>>>>>>>>
CLI output log example as below
>>>>>>>>>>>>>>>>>>>>>>>>>>>

(venv) stanma@Stans-MacBook-Pro demo % python3 retrieveASX.py 
Companyname: BHP GROUP LIMITED
############################################
Stage 1: Retrieve the 3th company stock info
The current page url is https://www2.asx.com.au/
Title is :Home
The page url: https://www2.asx.com.au/markets/company/bhp
Title: BHP share price and company information for ASX:BHP
Stock1 ticker: BHP
Stock1 Last Price: $41.170
Stock1 PE ratio: 6.55
The related company array is :['BHP', 'S32', 'PLS', 'MIN']

############################################
Stage 2: Retrieve the 2nd company stock info
The page url: https://www2.asx.com.au/markets/company/S32
Title: S32 share price and company information for ASX:S32
Stock2 ticker: S32
Stock2 Last Price: $3.950
Stock2 PE ratio: 4.47

############################################
Stage 3: Retrieve the 3th company stock info
The page url: https://www2.asx.com.au/markets/company/PLS
Title: PLS share price and company information for ASX:PLS
Stock3 ticker: PLS
Stock3 Last Price: $5.475
Stock3 PE ratio: 28.41

############################################
Stage 4: Retrieve the 4th company stock info
The page url: https://www2.asx.com.au/markets/company/MIN
Title: MIN share price and company information for ASX:MIN
Stock4 ticker: MIN
Stock4 Last Price: $82.450
Stock4 PE ratio: 40.79
{'BHP': 6.55, 'S32': 4.47, 'PLS': 28.41, 'MIN': 40.79}
Recommended purchased is S32
##########################
Thank you guys for having me practice such interesting task and making me continuously improving! :-)

