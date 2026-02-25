# try except --> try: #code that raises error except #errortype: #what to do
# ruleaza exceptu doar cand errortype e tipul de eroare care chiar a venit, altfel nu
# ei recomanda sa verifici functia pe care o folosesti --> with open de ex
# dupa sa verifici ce erori poate returna --> docs --> handle those errors with except errortype:
#

def name_len(username,min_len):
    if len(username)< min_len:
        return False
    if not username.isalnum():
        return False
    return True

print(name_len('sas',0))
# aici poti sa rulezi linistit cu min length = 0 dar nu prea are sens. de asta se creaza erori custom to be raised

def name_len1(username,min_len):
    if min_len <1:
        raise ValueError("mate how can the length be <1?")
    if len(username)< min_len:
        return False
    if not username.isalnum():
        return False
    return True
#print(name_len1('sas',0))

#print(name_len1(12,1)) # TypeError: object of type 'int' has no len()
#print(name_len1(['dasda'],1)) # AttributeError: 'list' object has no attribute 'isalnum'

# cum reparam asta? fortam inputul sa fie un data type specific, altfel dam eroare prestabilita cu assert
# assert --> assert x is true --> altfel da assertion message 

def name_len2(username,min_len):
    assert type(username) ==str, "name must be string mate"
    if min_len <1:
        raise ValueError("mate how can the length be <1?")
    if len(username)< min_len:
        return False
    if not username.isalnum():
        return False
    return True

print(name_len2(12,0))
