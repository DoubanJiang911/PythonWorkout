from operator import itemgetter
from collections import namedtuple

PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

Person = namedtuple('Person', ['name', 'id', 'score'])

Movie = namedtuple('Movie', ['title', 'length', 'director'])


def format_sort_records(list_of_tuples) -> str:
    output = []

    template = '{1:10} {0:10} {2:5.2f}'
    for person in sorted(list_of_tuples, key=itemgetter(1, 0)):
        output.append(template.format(*person))
    return '\n'.join(output)

def format_sort_records_by_named_tuples(list_of_tuples) -> str:
    output = []
    for person in sorted(list_of_tuples, key=lambda p: (p.id, p.name)):
        output.append(f"{person.id:10} {person.name:10} {person.score:5.2f}")
    return '\n'.join(output)

def sort_movies(movies: list[tuple], sort_by: str) -> list[tuple]:
    if sort_by == 'title':
        return sorted(movies, key=lambda movie: movie.title)
    elif sort_by == 'length':
        return sorted(movies, key=lambda movie: movie.length)
    elif sort_by == 'director':
        return sorted(movies, key=lambda movie: movie.director)
    else:
        return movies

def choice_how_to_sort_movie(movies: list[tuple]):
    print("How would you like to sort the movies?")
    print("1. By title")
    print("2. By length")
    print("3. By director's name")
    choice = input("Enter your choice (1/2/3): ")

    if choice in ['1', '2', '3']:
        sorted_movies = sort_movies(movies, {'1': 'title', '2': 'length', '3': 'director'}[choice])
        for movie in sorted_movies:
            print(f"Title: {movie.title:50} Length: {movie.length:5} minutes, Director: {movie.director:15}")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

# Function to sort movies by multiple criteria
def sort_movies_by_many_fields(movies: list[tuple], sort_keys: tuple[str]) -> list[tuple]:
    return sorted(movies, key=lambda movie: tuple(getattr(movie, key) for key in sort_keys))

# Ask the user for sorting preferences
def choice_how_to_sort_movie_by_many_fields(movies: list[tuple]):
    print("How would you like to sort the movies? (Enter fields separated by commas: title, length, director)")
    user_input = input("Enter your choice: ").strip().lower()

    # Replace ', ' with ',' to handle both ',' and ', ' inputs
    user_input = user_input.replace(', ', ',')
    # Split the user input into a list of sorting criteria
    sort_criteria = user_input.split(',')

    # Validate user input and sort the list
    if set(sort_criteria).issubset({'title', 'length', 'director'}):
        sorted_movies = sort_movies_by_many_fields(movies, sort_criteria)
        for movie in sorted_movies:
            print(f"Title: {movie.title:50} Length: {movie.length:5} minutes, Director: {movie.director:15}")
    else:
        print("Invalid choice. Please enter valid field names (title, length, director) separated by commas.")


if __name__ == '__main__':
    print(format_sort_records(PEOPLE))

    people = [
        Person(name='Alice', id=2, score=85.5),
        Person(name='Bob', id=1, score=90.0),
        Person(name='Charlie', id=3, score=88.2)
    ]
    print("====format_sort_records_by_named_tuples====")
    print(format_sort_records_by_named_tuples(people))
    print("====format_sort_records====")
    print(format_sort_records(people))

    print("====extend exercise: sorted movies by the user’s choice====")
    movie_list = [
        Movie('Parasite', 132, 'Bong Joon Ho'),
        Movie('1917', 119, 'Sam Mendes'),
        Movie('Once Upon a Time... in Hollywood', 161, 'Quentin Tarantino'),
        Movie('Joker', 122, 'Todd Phillips'),
        Movie('The Irishman', 209, 'Martin Scorsese')
    ]

    choice_how_to_sort_movie(movie_list)

    print("====extend exercise: sort by two or three of these fields====")
    choice_how_to_sort_movie_by_many_fields(movie_list)