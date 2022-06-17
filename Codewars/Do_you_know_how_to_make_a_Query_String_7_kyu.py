def to_query_string(data): 
    
    listing_data = []
    for key, values in data.items():
        if isinstance(values, list):
            for i in values:
                listing_data.append(f"{key}={i}")
        
        else:
            listing_data.append(f"{key}={values}")
    return '&'.join(listing_data)

