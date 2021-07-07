import re
def domain_name(url):
    pat = re.search('(https?://)?(www\.)?(?P<name>[\w-]+)\.', url)
    return pat.group('name')
