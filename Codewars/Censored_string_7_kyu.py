def uncensor(infected: str, discovered: str) -> str:
    result = infected[:]
    asterisk_counter = 0

    if discovered == "":
        return infected
    else:
        for idx in range(len(result)):
            if result[idx] == '*':
                result = result[:idx] + discovered[asterisk_counter] + result[idx+1:]
                asterisk_counter += 1
    return result 

# Alternative solution - best practice
def uncensor(infected: str, discovered: str) -> str:
	return infected.replace('*', '{}').format(*discovered)

print(uncensor("*h*s *s v*ry *tr*ng*", "Tiiesae"))