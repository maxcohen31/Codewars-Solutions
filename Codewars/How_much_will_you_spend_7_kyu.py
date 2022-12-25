def get_total(costs, items, tax):
    result = 0

    for k, v in costs.items():
        if k in items:
            result += v * items.count(k)

    return round(result + (result * tax), 2)


costs = {'socks':5, 'shoes':60, 'sweater':30}
print(get_total(costs, ["socks", "shoes"], 0.09))