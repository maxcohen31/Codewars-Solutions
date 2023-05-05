from re import findall

def get_product_id(s: str) -> str:
    return findall(r"(?<=\-)\d+(?=\-[0-9]{8})", s)[0]   




print(get_product_id("exampleshop.com/public-toilet-proximity-radar-p-942312798-01012020.html"))

print(get_product_id("http://www.exampleshop.com/test-p-3051980-11112011.html"))
print(get_product_id("http://www.exampleshop.com/p-p-1124329-12122000.html"))

