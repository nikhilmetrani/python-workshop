__author__ = 'nick'

# import re
# import urllib

# target = "http://www.straitstimes.com/news/singapore"
#
# webFile = urllib.urlopen(target)
# content = webFile.read().decode("utf-8")
# webFile.close()
#
# pattern = re.compile(r'<span class=\"hp_bn_title[]^<]+?'
#                      r'<a href=\"([^\"]+?)\">'
#                      r'([^<]+?)<\/a>', re.DOTALL)
#
# for match in pattern.finditer(content):
#     print('URL:' + match.group(1))
#     print('TITLE:' + match.group(2))

import urllib2

def getgoogleurl(search,siteurl=False):
    if siteurl==False:
        return 'http://www.google.com/search?q='+urllib2.quote(search)
    else:
        return 'http://www.google.com/search?q=site:'+urllib2.quote(siteurl)+'%20'+urllib2.quote(search)

def getgooglelinks(search,siteurl=False):
   #google returns 403 without user agent
   headers = {'User-agent':'Mozilla/11.0'}
   req = urllib2.Request(getgoogleurl(search,siteurl),None,headers)
   site = urllib2.urlopen(req)
   data = site.read()
   site.close()

   #no beatifulsoup because google html is generated with javascript
   start = data.find('<div id="res">')
   end = data.find('<div id="foot">')
   if data[start:end]=='':
      #error, no links to find
      return False
   else:
      links =[]
      data = data[start:end]
      start = 0
      end = 0
      while start>-1 and end>-1:
          #get only results of the provided site
          if siteurl==False:
            start = data.find('<a href="/url?q=')
          else:
            start = data.find('<a href="/url?q='+str(siteurl))
          data = data[start+len('<a href="/url?q='):]
          end = data.find('&amp;sa=U&amp;ei=')
          if start>-1 and end>-1:
              link =  urllib2.unquote(data[0:end])
              data = data[end:len(data)]
              if link.find('http')==0:
                  links.append(link)
      return links


import json
import urllib

def showsome(searchfor):
  query = urllib.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.urlopen(url)
  search_results = search_response.read()
  results = json.loads(search_results)
  data = results['responseData']
  print 'Total results: %s' % data['cursor']['estimatedResultCount']
  hits = data['results']
  print 'Top %d hits:' % len(hits)
  for h in hits: print ' ', h['url']
  print 'For more results, see %s' % data['cursor']['moreResultsUrl']

showsome('ermanno olmi')