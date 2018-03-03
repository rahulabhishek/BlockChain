page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('http:')#find the strating index of "http://udacity.com"
end_link_index=page.find('.com') #find the starting index of .com
url=page[start_link:(end_link_index+4)]#find the link without the .com
print(url)

end_link1=page[end_link_index:] #prints the last part of the url i.e ".com">"
end_link3=end_link1.find('">')# find the index of the ">
x=end_link1[:end_link3] # prints the strings before the index of ">, from the above code
print(x)
end_link2=end_link1.find(".")

url=y+x
print(url)