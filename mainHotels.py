import hotelsapi
import sentimentsAPI as sentiments
myHotels = {}


while True:
    print("I have",len(myHotels),"favourite Hotels :)")
    print("1.- Search hotel by Name")
    print("2.- Quality by Id")
    print("3.- Import hotel by Id")
    print("4.- List hotels")
    print("5.- List reviews by Id")
    print("6.- List hotels by value")
    print("7.- Analize reviews by Id")
    print("8.- Exit")
    option = int(input("Select option:"))
    if (option == 8):
        print("Bye!")
        break

    elif (option == 1):
        nameHotel = input("Enter name hotel:")
        hotels = hotelsapi.getHotelsByName(nameHotel)
        print("HOTELID","INFO")
        for hotelId, hotelDetail in hotels.items():
            print(hotelId)
            print("\tName:",hotelDetail["name"])
            print("\tAddress:",hotelDetail["address"])
            print("\tcity:",hotelDetail["city"])
            print("\tprovince:",hotelDetail["province"])
             
    elif (option == 2):
        hotelId = input("Enter hotel Id:")
        print("Quality:",hotelsapi.getValue(hotelId))

    elif (option == 3):
        hotelId = input("Enter hotel Id:")
        hotel = hotelsapi.getHotelDetailById(hotelId)
        if hotel != None:
            print("Importing....")
            reviews = hotelsapi.getReviewById(hotelId)
            if reviews != None:
                hotel["reviews"] = reviews
                myHotels[hotelId]  = hotel
            print("Imported successfully!")

    elif (option == 4):
        print("Listing Hotels")
        for hotel,detail in myHotels.items():
            print(hotel)
            print("\tName:",detail["name"])
            print("\tAddress:",detail["address"])
            print("\tCity:",detail["city"])
            print("\tProvince:",detail["province"])
            print("\tValue:",detail["value"])
            print("\tReviews (",len(detail["reviews"]),")") 

    elif (option == 5):
        hotelId = input("Enter hotel Id:")
        if hotelId in myHotels:
            print("Reviews for ",myHotels[hotelId]["name"],":")
            for r in myHotels[hotelId]["reviews"]:
                print("\t",r)

    elif (option == 6):
        quality = float(input("Enter min quality [0-10]:"))
        print("Listing Hotels....")
        for hotel,detail in myHotels.items():
            if (float(detail["value"].split("/")[0]) >= quality):
                print(hotel)
                print("\tName:",detail["name"])
                print("\tAddress:",detail["address"])
                print("\tCity:",detail["city"])
                print("\tProvince:",detail["province"])
                print("\tValue:",detail["value"])

    elif option == 7:
        valores = {"P+":0,"P":0,"NEU":0,"N":0,"N+":0,"NONE":0}

        hotelId = input("Enter hotel Id:")
        if hotelId in myHotels:
            for r in myHotels[hotelId]["reviews"]:
                estadocompleto = sentiments.getScoreTag(r)
                if estadocompleto[0] not in valores:
                    valores[estadocompleto[0]] = 0
                valores[estadocompleto[0]] += 1
    
        print("Reviews for the hotel ",myHotels[hotelId]["name"],": ")
        for k,v in valores.items():
            print("\t",str(k)+":",str(v))

    else:
        print("Option incorrect!!!")