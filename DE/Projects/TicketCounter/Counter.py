movies=["The Batman", "Avatar: The Way of Water", "Top Gun: Maverick", "Jurassic World Dominion", "Doctor Strange in the Multiverse of Madness"]
seats_available=[50, 100, 75, 60, 80]
movies=[movie.lower() for movie in movies]
def greet()->str:
    print("Hello! Welcome to the TimePass Theaters!! What movie would you like to watch today?\nType 'exit' to leave the counter.\n")
    m=input("Enter the movie name: ")
    if m.lower()=="exit":
        print("Thank you for visiting TimePass Theaters. Have a great day!\n")
        exit()
    return m


def list_movies()->None:
    print("Here are the movies currently available in our theater:")
    for movie in movies:
        print(f"- {movie.title()}")
    print("\n")

def find_movies(movie_name:str)->bool:
    if movie_name.lower() in movies:
        return True
    else:
        return False
def seats_available_for_movie(movie_name:str)->int:
    id=movies.index(movie_name.lower())
    if id>=0:
        return seats_available[id],id
    else:
        return -1, -1
def buy_tickets(movie_name:str, num_tickets:int)->bool:
    a,id=seats_available_for_movie(movie_name)
    if num_tickets<=a:
        seats_available[id]-=num_tickets
        return True
    else:
        return f"No enough seats available."
def main():
    flag=True
    while sum(seats_available)>0 or flag:
        list_movies()
        movie_name=greet()
        if find_movies(movie_name):
            a,id=seats_available_for_movie(movie_name)
            print(f"Seats available for {movie_name}: {a}\n")
            num_tickets=int(input("Enter the number of tickets you want to buy: "))
            if buy_tickets(movie_name, num_tickets):
                print(f"Successfully bought {num_tickets} tickets for {movie_name}.\n")
            else:
                print(f"Failed to buy tickets for {movie_name}.\n")
        else:
            print(f"{movie_name} is not available in our theater.\n")
