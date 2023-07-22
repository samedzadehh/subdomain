try:
    
    import requests


    print("1.Find subdomains\n2.Find subdirectories")
    choice=input("Choice: ")
    target_url=input("URL: ")

    def request(target_url):
        try:
            return requests.get("http://"+target_url)
            
        except requests.exceptions.ConnectionError:
            pass

    def subdomain():
        wordlist=input("Wordlis way: ")
        with open("{}".format(wordlist),"r") as wordlist_file:
            for line in wordlist_file:
                word=line.strip()
                test_url=word+"."+target_url
                response=request(test_url)

                if response:
                    print("Discovered subdomain -> ",test_url)

    def subdirectories():
        wordlist=input("Wordlis way: ")
        with open("{}".format(wordlist),"r") as wordlist_file:
            for line in wordlist_file:
                word=line.strip()
                test_url=target_url+"/"+word
                response=request(test_url)

                if response:
                    print("Discovered subdirectory -> ",test_url)

    if choice=='1':
        subdomain()
    elif choice=='2':
        subdirectories()
    else:
        print("OPeration not avialble please try again")
except KeyboardInterrupt:
    print(" \nProgram ended ") 