# voight-kampff

Check robots.txt files for actual access.

 While sites often list pages under their robots.txt file that aren't to be accessed by crawlers, those pages are frequently still available and of potential interest. This script targets a domain's robot.txt and checks the status codes on the pages listed therein.



./voight-kampff.py -h<br/>

usage: voight-kampff.py [-h] -t --target


Scrape robots.txt file and check actual page access.

optional arguments:<br/>

  -h, --help   show this help message and exit<br/>

  -t --target  Target URL: e.g., https://google.com

./voight-kampff.py -t https://yahoo.com
