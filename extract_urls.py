page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('a href')#find the strating index of "http://udacity.com"
#print(page[start_link:])
start_quote=page.find('"',start_link) #find the starting index of .com
#print(page[start_quote:])
end_quote =page.find('"',start_quote+1)
#print(page[end_quote:])
url=page[start_quote+1:end_quote]#find the link without the .com
print(url)

