def wordsummary(test_string):
    test_string = "dfgs fdgs dfgs dfgs fdgf fg ff fff. fgsdg sd sdfgsf gf fgfds gs fgsg fgsfg. fgfsdg fgsgf fdsgfsgf. gg khlk hk hjh jhj jhjh jhjh jhjh. jhjh jhjh jhj jhjh jhjh jhjh jhi iuoiu oiuo uou iuoiuo iuouo iuoiui uioiu uioui uoiu iouou iouiu oiuoiu iuoi iooiu uiiuiu oiui iouui"
    limit=50
    crop = ""
    count=0
    wc = len(test_string.split()) # Word Count

    for i in test_string.split(" "): # Loop to read the words and select first 50
        crop = crop + " " +i
        count+=1
        if(count==limit):
            break;
    
    index = (crop.rfind('.')) # Index holds Rightmost value of period

    print("This is the summary : "+ test_string[:index])
    
    return test_string[:index]
