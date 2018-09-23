# Report functions

#1.
def get_most_played(file_name):
    split_file_rows = file_name.splitlines()
    game_solds = [i.split('\t')[1] for i in split_file_rows]
    make_solds_int = map(lambda x: float(x), game_solds)
    max_game_solds = str(int(max(make_solds_int)))
    if max_game_solds not in game_solds:
        max_game_solds = round(max_game_solds)
    max_index = game_solds.index(max_game_solds)
    game_titles = [i.split('\t')[0] for i in split_file_rows]
    return game_titles[max_index]

"""Return the title of the most played game"""

#2.
def sum_sold(file_name):
    split_file_rows = file_name.splitlines()
    game_solds = [i.split('\t')[1] for i in split_file_rows]
    make_solds_int = map(lambda x: float(x), game_solds)
    return sum(make_solds_int)

"""Return how many cipies have been sold totally""" 

#3.
def get_selling_avg(file_name):
    split_file_rows = file_name.splitlines()
    game_solds = [i.split('\t')[1] for i in split_file_rows]
    make_int = map(lambda x: float(x), game_solds)
    avg_solds = sum(make_int)/len(game_solds)
    return avg_solds

"""Return the average value of the sellings"""

#4.
def  count_longest_title(file_name):
    split_file_rows = file_name.splitlines()
    game_titles = [i.split('\t')[0] for i in split_file_rows]
    max_list = []
    for words in game_titles:
        max_list.append(len(words))
    return max(max_list)

"""Return how many characters long is the longest title"""

#5.
def  get_date_avg(file_name):
    split_file_rows = file_name.splitlines()
    game_releases = [i.split('\t')[2] for i in split_file_rows]
    game_releases_int = map(lambda x: float(x), game_releases)
    return round(sum(game_releases_int)/len(game_releases))

"""Return the average value of the release dates"""

#6.
def get_name(file_name,title):
    split_file_rows = file_name.splitlines()
    splitted_games = [i.split('\t') for i in split_file_rows]
    titles = [i.split('\t')[0] for i in split_file_rows] 
    counter = -1
    for rows in titles:
        counter += 1
        if rows == title:
            return splitted_games[counter]
     
"""Return the properties of the given game title's"""

#7.
def count_grouped_by_genre(file_name):
    split_file_rows = file_name.splitlines()
    game_genres = [i.split('\t')[3] for i in split_file_rows]
    group_by_genre = {}
    for genres in game_genres:
        if genres not in group_by_genre:
            group_by_genre[genres] = 1
        else:
            group_by_genre[genres] += 1
    return group_by_genre

"""Return how many games are there grouped by genre"""

#8.
def get_date_ordered(file_name):
    split_file_rows = file_name.splitlines()
    splitted_games = [i.split('\t') for i in split_file_rows]
    sort_by_alphabetic = sorted(splitted_games, key=lambda x: (x[0], x[0]))
    sort_by_release = sorted(sort_by_alphabetic, key=lambda x: (x[2], x[0]),reverse=True)
    get_titles = [[row[i] for row in sort_by_release] for i in range(4)]
    return get_titles[0]

"""Return the date ordered list of the games"""