

def give_detail_birth(player_data, employ_data):
    detail = f"Born in {player_data[2]}, "
    detail += f"From the nation of {player_data[3]}.\n"
    return detail


def give_detail_current_team(player_data, employ_data):
    last_employ = employ_data[-1]
    detail = f"Last played in team {last_employ[10]}, in the {last_employ[11]}.\n"
    return detail


def give_detail_money(player_data, employ_data):
    last_employ = employ_data[-1]
    detail = f"Worth {last_employ[7]}$, with a wage of {last_employ[8]}$.\n"
    return detail


def give_detail_body(player_data, employ_data):
    last_employ = employ_data[-1]
    detail = f"At height of {last_employ[5]}cm, and weight of {last_employ[6]}kg.\n"
    return detail


def give_detail_preform(player_data, employ_data):
    last_employ = employ_data[-1]
    detail = f"Play positions of {last_employ[3]}. With performance rating {last_employ[4]}.\n"
    return detail


def give_detail_shirt(player_data, employ_data):
    last_employ = employ_data[-1]
    detail = f"Staring the shirt number {last_employ[9]}.\n"
    return detail


def give_detail_change_team(player_data, employ_data):
    for i in range(1, len(employ_data)):
        if employ_data[i][10] != employ_data[0][10]:
            detail = f"Has changed teams from {employ_data[0][10]} to {employ_data[i][10]}.\n"
            return detail
    years = employ_data[-1][2] - employ_data[0][2] + 1
    detail = f"Has remained in the same team for {years} years.\n"
    return detail


def give_detail_change_features(player_data, employ_data):
    weight = employ_data[-1][6] - employ_data[0][6]
    if abs(weight) >= 4:
        if weight > 0:
            detail = f"While playing in the leagues, his weight increased by {weight} kg.\n"
        else:
            detail = f"While playing in the leagues, his weight decreased by {abs(weight)} kg.\n"
        return detail
    height = employ_data[-1][5] - employ_data[0][5]
    if height >= 3:
        detail = f"While playing in the leagues, his height increased by {height} cm.\n"
        return detail
    rating = employ_data[-1][4] - employ_data[0][4]
    if abs(rating) >= 5:
        if rating > 0:
            detail = f"While playing in the leagues, his overall rating increased by {rating}.\n"
        else:
            detail = f"While playing in the leagues, his overall rating decreased by {abs(rating)}.\n"
        return detail
    value = employ_data[-1][7] - employ_data[0][7]
    if abs(value) >= 6000000:
        if rating > 0:
            detail = f"While playing in the leagues, his value increased by {value}$.\n"
        else:
            detail = f"While playing in the leagues, his value decreased by {abs(value)}$.\n"
        return detail
    salary = employ_data[-1][8] - employ_data[0][8]
    if abs(salary) >= 8000:
        if rating > 0:
            detail = f"While playing in the leagues, his salary increased by {salary}$.\n"
        else:
            detail = f"While playing in the leagues, his salary decreased by {abs(salary)}$.\n"
        return detail
    years = employ_data[-1][2] - employ_data[0][2] + 1
    detail = f"Has not had a significant change in features or status for {years} years.\n"
    return detail
