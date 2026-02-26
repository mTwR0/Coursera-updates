# expectation is that code raises error when yo udo a specific thing --> 
# assertRaises de la unittest
#
def name_len2(username,min_len):
    assert type(username) ==str, "name must be string mate"
    if min_len <1:
        raise ValueError("mate how can the length be <1?")
    if len(username)< min_len:
        return False
    if not username.isalnum():
        return False
    return True

#print(name_len2(12,0))