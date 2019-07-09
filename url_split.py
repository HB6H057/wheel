from urllib import parse
url = "http://www.example.org/default.html?ct=32&op=92&item=98"
parse.urlsplit(url)
# SplitResult(scheme='http', netloc='www.example.org', path='/default.html', query='ct=32&op=92&item=98', fragment='')
parse.parse_qs(parse.urlsplit(url).query)
# {'item': ['98'], 'op': ['92'], 'ct': ['32']}
dict(parse.parse_qsl(parse.urlsplit(url).query))
# {'item': '98', 'op': '92', 'ct': '32'}
