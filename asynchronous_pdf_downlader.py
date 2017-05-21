from concurrent import futures


import requests


def downloader(url):
    response = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response.content)

    return 'Finished Downloading: {}'.format(file_name)



def multiple_downloader(urls):
    workers = len(urls)
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(downloader, urls)

    return len(list(res))



urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",]

print(multiple_downloader(urls))
