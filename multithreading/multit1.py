import concurrent.futures
import urllib.request
import requests


list1 = [i for i in range(20)]
print (list1)


"""
iteam1 = list1.pop(0)
print(iteam1)
print(list1)
iteam1 = list1.pop(0)
print(iteam1)
print(list1)
"""

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    #with urllib.request.urlopen(url, timeout=timeout,verify=False) as conn:
    with requests.get(url, timeout=timeout,verify=False) as conn:
        return conn.content
        #return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))