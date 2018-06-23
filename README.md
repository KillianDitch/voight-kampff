# voight-kampff

Check robots.txt files for actual access.

 While sites often list pages under their robots.txt file that aren't to be accessed by crawlers, those pages are frequently still available and of potential interest. This script targets a domain's robot.txt and checks the status codes on the pages listed therein.


```
./voight-kampff.py -h

usage: voight-kampff.py [-h] -t --target

Scrape robots.txt file and check actual page access.

optional arguments:

  -h, --help   show this help message and exit

  -t --target  Target URL: e.g., https://google.com

./voight-kampff.py -t https://yahoo.com
Targeting: https://yahoo.com
--------------------------------------------------

https://yahoo.com/robots.txt : 200

Specified User-Agents: 1
*


--------------------------------------------------
Allowed Results:

--------------------------------------------------
Number of 200 OK results: 0
Number of 3XX results: 0
Number of 4XX results: 0
Number of other results: 0
--------------------------------------------------

DISallowed Results:
https://yahoo.com/_multiremote : 404
https://yahoo.com/_remote : 503
https://yahoo.com/_td_api : 404
https://yahoo.com/_tdhl_api : 404
https://yahoo.com/_tdpp_api : 404
https://yahoo.com/bin/ : 404
https://yahoo.com/blank.html : 404
https://yahoo.com/digest : 404
https://yahoo.com/includes/ : 404
https://yahoo.com/p/ : 200
https://yahoo.com/r/ : 404

--------------------------------------------------
Number of 200 OK results: 1
Number of 3XX results: 0
Number of 4XX results: 9
Number of other results: 1
```
