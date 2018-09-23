# Report functions

#1.
def count_games(file_name):  
    split_file_rows = file_name.splitlines()
    return len(split_file_rows)

"""return how many games are in the file"""

#2.
def decide(file_name, year):  
    split_file_rows = file_name.splitlines()
    game_releases = [i.split('\t')[2] for i in split_file_rows]
    if year in game_releases:
        return True
    if year not in game_releases:
        return False

"""return if there is a game from the  given year"""

#3.
def get_latest(file_name): #output the latest
    split_file_rows = file_name.splitlines()
    splitted_games = [i.split('\t') for i in split_file_rows]
    most_release_order = [splitted_games[0]]
    for row in splitted_games:
        if row[2] > most_release_order[0][2]:
            most_release_order.append(row)
            most_release_order.remove(most_release_order[0])
    return most_release_order[0][0]

"""return the title of the latest game"""

#4.
def count_by_genre(file_name, genre):
    split_file_rows = file_name.splitlines()
    genres = []
    for i in split_file_rows:
        genres.append(i.split('\t')[3])
    genre_counter = 0
    for words in genres:
        if words == genre:
            genre_counter += 1
    return genre_counter

"""return how many games we have by genre"""

#5.
def get_line_number_by_title(file_name,title):
    split_file_rows = file_name.splitlines()
    titles = [i.split('\t')[0] for i in split_file_rows] 
    counter = 0
    for rows in titles:
        counter += 1
        if rows == title:
            return counter
        elif counter == 24:
            print("The given game title is not valid.")
            raise ValueError        

"""return the line number of the given game title"""

#6.
def sort_abc(file_name):
    split_file_rows = file_name.splitlines()
    titles = [i.split('\t')[0] for i in split_file_rows]
    sorted_titles = []
    while titles:
        smallest = min(titles)
        sorted_titles.append(smallest)
        titles.remove(smallest)
    return sorted_titles

""" Sort the titles by alphabetical order,
    while in the titles is only one value the program append the smallest value. """

#7.
def get_genres(file_name):
    split_file_rows = file_name.splitlines()
    game_genres = [i.split('\t')[3] for i in split_file_rows]
    setted_game_genres = set(game_genres)
    return sorted(setted_game_genres,key=str.lower)

"""return all game genres we have"""

#8.
def when_was_top_sold_fps(file_name):
    split_file_rows = file_name.splitlines()
    splitted_games = [i.split('\t') for i in split_file_rows]
    filtered_s_g = [row for row in splitted_games if row[3] == 'First-person shooter']
    filtered_s_g.sort(key=lambda x: (float(x[1]), x[0]))
    return filtered_s_g[-1][2]

"""return the release date of the top sold "First-person shooter" game"""