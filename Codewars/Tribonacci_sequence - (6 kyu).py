def tribonacci(signature, n):
    sig = signature[:]
    if n == 3:
        return signature
    elif n == 0:
        return []
    elif n < 3:
        first = []
        for i in range(0, n):
            first.append(sig[i])
        return first    
    elif n > 3:
        for i in range(3, n):
            tribo = sig[i-1] + sig[i-2] + sig[i-3]
            sig.append(tribo)
        return sig
    
      
sign = [1, 1, 1]
print(tribonacci(sign, 1))       

