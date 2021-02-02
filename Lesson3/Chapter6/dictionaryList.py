destintations = {
    "France" : "Paris",
    "Spain" : "Madrid",
    "Japan" : "Tokyo",
    "Italy" : "Rome",
    "Florida" : "Keys",
    "United Kingdom" : "London"
}
accomodations = {
    "Type" : "AirBnb",
    "Length" : "2 weeks",
    "Bedrooms" : "3",
    "Bathrooms" : "2",
    "Kitchen" : "Yes",
    "WiFi" : "Yes",
    "Laundry" : "Yes"
}
transportation = {
    "Rental" : "Car",
    "Size" : "6 passenger",
    "Miles" : "1,000",
}
trips = [destintations, accomodations, transportation]

for t in trips:
    print(t)