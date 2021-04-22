print("CodeInc ticket booker")
fname = input("Enter ur first name :")
lname = input("Enter ur last name :")
email = input("Enter ur email :")
age = int(input("Enter ur age :"))
gender = input("Enter ur gender :")
mobile = int(input("Enter ur mobile no. :"))


def movie():
    print("Select the movie")
    print("1. movie1")
    print("2. movie2")
    print("3. movie3")
    print("4. movie4")


movie()

m = int(input("enter"))


def movie_select(m):
    if m == 1:
        print("U selected movie1")
    elif m == 2:
        print("U selected movie2")
    elif m == 3:
        print("U selected movie3")
    elif m == 4:
        print("U selected movie4")


movie_select(m)
