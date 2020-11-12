RANK = 0
COUNTRY = 1
RATING = 2
BYEAR = 3

def open_file(filename):
    try:
        file_stream = open(filename, 'r')
        return file_stream
    except FileNotFoundError:
        return None

def create_players_dict(file_stream):
    the_dict = {}
    for line in file_stream:
        rank, name, country, rating, byear = line.split(";")
        lastname, firstname = name.split(",")

        firstname = firstname.strip(",")
        lastname = lastname.strip(",")
        country = country.strip(",")

        key = "{} {}".format(firstname, lastname)
        value = (int(rank), country, int(rating), int(byear))
        the_dict[key] = value
    return the_dict

def create_countries_dict(dict_players):
    country_dict = {}

    for chess_player, chess_player_data in dict_players.items():
        country = chess_player_data[COUNTRY]
        if country in country_dict:
            name_list = country_dict[country]
            name_list.append(chess_player)
        else:

            country_dict[country] = [chess_player]
    return country_dict

def create_byear_dict(dict_players):
    byear_dict = {}

    for chess_player, chess_player_data in dict_players.items():
        byear = chess_player_data[BYEAR]
        if byear in byear_dict:
            name_list = byear_dict[byear]
            name_list.append(chess_player)
        else:

            byear_dict[byear] = [chess_player]
    return byear_dict

def get_average_rating(players, dict_players):
    ratings = [dict_players[player][RATING] for player in players]
    average = sum(ratings)/len(ratings)
    return average

def print_sorted(dict_players, dict_byear):
    sorted_dict = sorted(dict_byear.items())
    for key, players in sorted_dict:
        average = get_average_rating(players, dict_players)

        print("{} ({}) ({:.1f}):".format(key, len(players), average))
        for player in players:
            rating = dict_players[player][RATING]
            print("{:>40}{:>10d}".format(player, rating))

def print_header(header_str):
    print(header_str)
    dashes = "-" * len(header_str)
    print(dashes)

def main():
    filename = input("Enter filename: ")
    file_stream = open_file(filename)
    if file_stream:
        dict_players = create_players_dict(file_stream)
        dict_countries = create_countries_dict(dict_players)
        dict_byear = create_byear_dict(dict_players)

        print_header("Players by country:")
        print_sorted(dict_players, dict_countries)
        print_header("\nPlayers by birth year:")
        print_sorted(dict_players, dict_byear)

main()