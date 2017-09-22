def reducer():
    SalesTotal = 0
    OldKey = None

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue
        thisKey, thisSale = data
        if OldKey and OldKey != thisKey:
            print "{0}\t{1}".format(OldKey, SalesTotal)
            SalesTotal = 0
            OldKey = thisKey
            SalesTotal += float(thisSale)
            
