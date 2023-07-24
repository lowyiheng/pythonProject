"""
place = empty list
longest_place = empty string
get place
while place != string
      add place to places
      get place
if length of places > 0
   display On my holiday, I went to:
   for place in places
       display place
       if length of place > length of longest_place
           longest_place = place
    display longest_place
else
    display I went nowhere :(
"""
places = []
longest_place = ""
place = input("Place: ").title()
while place != "":
    places.append(place)
    place = input("Place: ").title()
if len(places) > 0:
    print("On my holiday, I went to: ")
    for place in places:
        print(place)
        if len(place) > len(longest_place):
            longest_place = place
    print("The place with the longest names was", longest_place)
else:
    print("I went nowhere :(")