#from googlesearch.googlesearch import GoogleSearch
import googlesearch
response = googlesearch.GoogleSearch().search("site:ing.* ext:swf",num_results=10)
for result in response.results:
    print("[+] New url found : " + result.url)


