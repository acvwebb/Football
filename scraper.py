# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
#lines 4 and 5 are the first two libraries that need to be imported 
import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://www.facebook.com/amelia.c.webb/friends?pnref=lhc")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
names = root.cssselect("ul/li[1]/div/div/div[2]/div/div[2]/div")
for name in names: 
  print name.text
  print name.attrib['href']

#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
