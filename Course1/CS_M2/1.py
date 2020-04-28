import sys

while True:

    inp = input("Please enter the password:")

    if not 6 <= len(inp) <= 12:
        print ('Length must be within 6 and 12')
        continue

    counta = 0
    countu = 0
    countn = 0
    counts = 0

    for i in inp:
        if i.isupper():
            countu += 1
        if i.islower():
            counta += 1
        if i.isnumeric():
            countn += 1
        if i in '$#@':
            print ('Entered Special Char')
            counts += 1

    if counta == 0 or countn == 0 or countu == 0 or counts == 0:
        print('Entered password Does not meet security guidelines')
    else:
        print('Entered Password is Meeting Guidelines')