#def factorial(n):
#	result = 1
#	while n >= 1:
#		result = result * n
#		n = n -1
#	return result

#print factorial(22)

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    #Insert your code here
    else:
	    start_quote = page.find('"', start_link)
	    end_quote = page.find('"', start_quote + 1)
	    url = page[start_quote + 1:end_quote]
	    return url, end_quote
                 
url, endpos = get_next_target('Not "good" at all!')
if url:
	print "Valid url"
else:
	print "Not a url"