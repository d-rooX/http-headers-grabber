import requests
import sys

# URLS FILEPATH GETTING
try:
    urls = open(sys.argv[1], 'r')
except IndexError:
    print('http-header-grabber by droox')
    exit(0)
except FileNotFoundError:
    print('file not found')
    exit(-1)

# OUTPUT GETTING
if '-o' in sys.argv:
    try:
        output = open(sys.argv[sys.argv.index('-o')+1], 'a')
    except IndexError:
        print('you did not specify an output file')
        exit(-1)
else:
    output = sys.stdout

fucked_up_urls = []
# DOIN STUFF
for url in urls:
    url = url.replace('\n', '')
    if url == '\n' or url == '': continue
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        fucked_up_urls.append((url, 'ConnectionError'))
    else:
        if response.status_code == 200:
            response_headers = response.headers
            output.write(f'{url}\n')
            for header_key in response_headers:
                output.write(f'\t{header_key}: {response_headers[header_key]}\n')
            output.write('\n\n')
        else:
            fucked_up_urls.append((url, response.status_code))

print('done')
if fucked_up_urls:
    fucked_up_urls = dict(fucked_up_urls)
    for i in fucked_up_urls:
        print(i, fucked_up_urls[i])
