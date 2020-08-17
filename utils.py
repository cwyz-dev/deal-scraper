def convert_price_to_number(price):
    price = price.split("$")[1]
    try:
        price = price.replace("\n", ".")
    except:
        Exception()

    try:
        price = price.split(",")[0] + price.split(",")[1]
    except:
        Exception()

    return float(price)

def my_range(start, end, step, forwards):
    if (forwards):
        while start <= end:
            yield start
            start += step
    else:
        while start >= end:
            yield start
            start -= step
