def increment_string(s):
    numbers = '0123456789'
    s_strip = s.rstrip(numbers)
    get_numbers = s[len(s_strip):]
    if len(get_numbers) > 0:
        adding_proc = 1 + int(get_numbers)
        return s_strip + str(adding_proc).zfill(len(get_numbers)) 
    elif len(get_numbers) == 0:
        return s + '1'
        

    