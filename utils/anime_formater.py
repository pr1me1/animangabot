def anime_list_format(anime_list: [{}]):
    message = ""
    for i in range(len(anime_list)):
        message += str(i + 1) + ".\t"
        message += str(anime_list[i].get('title_english')) + ' rating: ' + str(anime_list[i].get('rating')) + '\n'

    return message


def anime_format(anime: {}):
    message = ""
    message += '<b>Anime name: ' + str(anime.get('title')) + '</b>' + '\n\n'
    for title in anime.get('titles'):
        message += str(title.get('type')) + ": " + str(title.get('title')) + '\n'

    message += "Status: " + str(anime.get('status')) + '\n'
    message += "Rating: " + str(anime.get('rating')) + '\n'
    message += "Score" + str(anime.get('score')) + " " + str(anime.get("scored_by")) + '\n'
    message += "Rank: " + str(anime.get('rank')) + '\n'
    message += "Popularity: " + str(anime.get('popularity')) + '\n'
    message += "Favorites: " + str(anime.get('favorites')) + '\n'

    return message
