import urllib

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
            return "error"


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link== -1:
        return None,0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def print_all_links(page):
    while True:
        url,endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break

print_all_links(get_page('https://stackoverflow.com/questions/39045802/python-program-doesnt-return-links-from-http-xkcd-com-353-udacity-intro-to-c'))