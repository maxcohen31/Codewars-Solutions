def modify_multiply(st, loc, num):
    result = f"{st.split()[loc]}-" * num
    return result[0:-1]

print(modify_multiply("This is a string",3,5))