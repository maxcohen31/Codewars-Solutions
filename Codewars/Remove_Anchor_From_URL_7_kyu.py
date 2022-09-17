def remove_url_anchor(url):
    url = url.split('#')
    return url[0]

# Solution 2
import re
def remove_url_anchor(url):
    return re.sub(r"#.*$", '', url)

print(remove_url_anchor('www.codewars.com#about'))