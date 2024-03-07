import random
import tkinter as tk
from tkinter import messagebox, ttk
import backend

from tkinter import font
size_h = 750
size_w = 1000


def login(entry_username, entry_password):
    username = entry_username.get()
    password = entry_password.get()
    if backend.login(username, password):
        clear_root()
        draw_homepage()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def back_to_homepage():
    clear_root()
    draw_homepage()


def end_game():
    backend.end_game()
    back_to_homepage()


def search_player():
    clear_root()
    draw_search_player()


def login_page():
    clear_root()
    draw_login_page()

def filter_player(name):
    clear_root()
    draw_filtered_player(name)


def random_player():
    clear_root()
    draw_random_player()


def back_to_filtered():
    clear_root()
    draw_search_player()


def choose_difficulty():
    clear_root()
    draw_choose_difficulty()


def create_root():
    ret_root = tk.Tk()
    ret_root.geometry("1000x750")
    return ret_root


def clear_root():
    for child in root.winfo_children():
        child.destroy()


def search_by_team():
    clear_root()
    draw_search_players_by_team()


def display_by_team(team_name, players, i):
    clear_root()
    draw_players_by_team(team_name, players, i)


def choose_team(difficulty):
    clear_root()
    backend.set_game_difficulty(difficulty)
    draw_choose_team()


def start_game(team):
    exist = backend.set_game_team(team)
    if exist is False:
        messagebox.showerror("Search Team", "Team do not exist.")
        clear_root()
        draw_choose_team()
        return
    play_game()


def start_game_without_team():
    clear_root()
    play_game()


def play_game():
    clear_root()
    draw_play_game()


def display_register():
    clear_root()
    draw_register_page()


def display_answer(answer, correct_answer):
    clear_root()
    draw_check_answer(answer, correct_answer)


def draw_players_by_team(team_name, players, i):
    back_font = font.Font(family="Helvetica", size=12, weight="bold")
    button_search_player = tk.Button(root, text="Back", command=back_to_homepage, width=10, height=1, font=back_font)
    button_search_player.place(x=20, y=20)
    if players is None:
        messagebox.showerror("Search team", "Team do not exist.")
        search_by_team()
        return
    static, dynamic = backend.get_player_data(players[i])
    draw_player_info(static, dynamic)

    i = i + 1
    if i >= len(players):
        i = 0
    button_search_player = tk.Button(root, text="Next Player", command=lambda: display_by_team(team_name, players, i),
                                     width=13, height=1)
    button_search_player.place(relx=0.9, rely=0.8, anchor="center")


def draw_search_players_by_team():
    input_font = font.Font(family="Helvetica", size=11)
    back_font = font.Font(family="Helvetica", size=12, weight="bold")
    button_back = tk.Button(root, text="Back", command=back_to_homepage, width=10, height=1, font=back_font)
    button_back.place(x=20, y=20)

    label_team_name = tk.Label(root, text="Team Name:", font=back_font)
    label_team_name.place(relx=0.5, rely=0.3, anchor="center")

    team_name = tk.Entry(root, width=25, font=input_font)
    team_name.place(relx=0.5, rely=0.35, anchor="center")

    button_search_player = tk.Button(root, text="Search", command=lambda: display_by_team(team_name.get(),
                                                                                          backend.get_team_players(
                                                                                              team_name.get()), 0),
                                     width=10, height=1, font=back_font)
    button_search_player.place(relx=0.5, rely=0.6, anchor="center")


def draw_login_page():
    bold_font = font.Font(family="Helvetica", size=12, weight="bold")
    input_font = font.Font(family="Helvetica", size=11)
    label_username = tk.Label(root, text="Username:", font=bold_font)
    entry_username = tk.Entry(root, font=input_font)

    label_password = tk.Label(root, text="Password:", font=bold_font)
    entry_password = tk.Entry(root, show="*", font=input_font)

    button_login = tk.Button(root, text="Login", command=lambda: login(entry_username, entry_password), font=bold_font)
    button_register = tk.Button(root, text="Register", command=display_register, font=bold_font)

    # Centralize the widgets
    label_username.place(relx=0.5, rely=0.3, anchor="center")
    entry_username.place(relx=0.5, rely=0.35, anchor="center")
    label_password.place(relx=0.5, rely=0.4, anchor="center")
    entry_password.place(relx=0.5, rely=0.45, anchor="center")
    button_login.place(relx=0.5, rely=0.58, anchor="center")
    button_register.place(relx=0.5, rely=0.65, anchor="center")


def draw_homepage():
    bold_font = font.Font(family="Helvetica", size=12, weight="bold")
    main_font = font.Font(family="Helvetica", size=17, weight="bold")
    label_hello = tk.Label(root, text=f"Hello {backend.get_user_name()}", font=main_font)
    label_hello.place(relx=0.5, rely=0.05, anchor="center")

    label_high_score = tk.Label(root, text=f"Highest score {backend.get_player_max_score()}", font=main_font)
    label_high_score.place(relx=0.5, rely=0.1, anchor="center")

    button_search_player = tk.Button(root, text="Search Player By Name", command=search_player, width=25, height=3, font=bold_font)
    button_search_player.place(relx=0.5, rely=0.3, anchor="center")

    button_random_player = tk.Button(root, text="Search Players By Team", command=search_by_team, width=25, height=3, font=bold_font)
    button_random_player.place(relx=0.5, rely=0.4, anchor="center")

    button_random_player = tk.Button(root, text="Learn About Random Players", command=random_player, width=25, height=3, font=bold_font)
    button_random_player.place(relx=0.5, rely=0.5, anchor="center")

    button_play = tk.Button(root, text="Play Game", command=choose_difficulty, width=25, height=3, font=bold_font)
    button_play.place(relx=0.5, rely=0.6, anchor="center")


def draw_random_player():
    back_font = font.Font(family="Helvetica", size=12, weight="bold")
    button_back = tk.Button(root, text="Back", command=back_to_homepage, width=10, height=1, font=back_font)
    button_back.place(x=20, y=20)

    static, dynamic = backend.get_player_data(backend.get_random_player())
    draw_player_info(static, dynamic)

    button_next_player = tk.Button(root, text="Next Player", command=random_player, width=10, height=1, font=back_font)
    button_next_player.place(relx=0.9, rely=0.8, anchor="center")


def draw_search_player():
    input_font = font.Font(family="Helvetica", size=11)
    back_font = font.Font(family="Helvetica", size=12, weight="bold")
    button_back = tk.Button(root, text="Back", command=back_to_homepage, width=10, height=1, font=back_font)
    button_back.place(x=20, y=20)

    label_player_name = tk.Label(root, text="Player Name:", font=back_font)
    label_player_name.place(relx=0.5, rely=0.3, anchor="center")

    player_name = tk.Entry(root, width=25, font=input_font)
    player_name.place(relx=0.5, rely=0.35, anchor="center")

    button_search_player = tk.Button(root, text="Search", command=lambda: filter_player(player_name.get()), width=10, height=1, font=back_font)
    button_search_player.place(relx=0.5, rely=0.6, anchor="center")


def draw_play_game():
    if backend.get_lives() == 0:
        messagebox.showerror("Game Over", f"Out of lives.\nScore: {backend.get_score()}")
        end_game()
        return
    detail_font = font.Font(family="Helvetica", size=13)
    input_font = font.Font(family="Helvetica", size=11)
    state_font = font.Font(family="Helvetica", size=13, weight="bold")
    back_font = font.Font(family="Helvetica", size=12, weight="bold")
    button_search_player = tk.Button(root, text="Back", command=end_game, width=10, height=1, font=back_font)
    button_search_player.place(x=20, y=20)
    correct_id, wrong_names = backend.get_answers()
    static, dynamic = backend.get_player_data(correct_id)
    # difficulty = 0
    details = backend.get_question(static, dynamic)
    label_lives = tk.Label(root, text=f"Lives: {backend.get_lives()}", font=state_font)
    label_lives.place(relx=0.9, rely=0.06, anchor="center")
    label_lives = tk.Label(root, text=f"Score: {backend.get_score()}", font=state_font)
    label_lives.place(relx=0.9, rely=0.10, anchor="center")
    label_details = tk.Label(root, text=details, font=detail_font)
    label_details.place(relx=0.5, rely=0.2, anchor="center")

    answer_list = [name[0] for name in wrong_names]
    answer_list.append(static[1])
    random_subset = random.sample(answer_list, 4)
    ans1, ans2, ans3, ans4 = random_subset

    button_player_1 = tk.Button(root, text=f"{ans1}", command=lambda: display_answer(ans1, static[1]), width=30, height=1, font=input_font)
    button_player_2 = tk.Button(root, text=f"{ans2}", command=lambda: display_answer(ans2, static[1]), width=30, height=1, font=input_font)
    button_player_3 = tk.Button(root, text=f"{ans3}", command=lambda: display_answer(ans3, static[1]), width=30, height=1, font=input_font)
    button_player_4 = tk.Button(root, text=f"{ans4}", command=lambda: display_answer(ans4, static[1]), width=30, height=1, font=input_font)

    # Centralize the buttons horizontally
    x_coordinate = 0.5
    max_width = max(button_player_1.winfo_reqwidth(), button_player_2.winfo_reqwidth(),
                    button_player_3.winfo_reqwidth(), button_player_4.winfo_reqwidth())
    button_player_1.place(relx=x_coordinate, width=max_width, anchor="center", y=250)
    button_player_2.place(relx=x_coordinate, width=max_width, anchor="center", y=300)
    button_player_3.place(relx=x_coordinate, width=max_width, anchor="center", y=350)
    button_player_4.place(relx=x_coordinate, width=max_width, anchor="center", y=400)


def draw_check_answer(answer, correct_answer):
    detail_font = font.Font(family="Helvetica", size=17)
    button_font = font.Font(family="Helvetica", size=12)
    back_font = font.Font(family="Helvetica", size=12, weight="bold")
    button_search_player = tk.Button(root, text="Back", command=end_game, width=10, height=1, font=back_font)
    button_search_player.place(x=20, y=20)

    if answer == correct_answer:
        label_result = tk.Label(root, text="Correct", font=detail_font)
        backend.correct_answer()
    else:
        label_result = tk.Label(root, text="Incorrect", font=detail_font)
        backend.wrong_answer()
    label_result.place(relx=0.5, rely=0.2, anchor="center")
    button_search_player = tk.Button(root, text="Next Question", command=lambda: play_game(), width=25, height=1, font=button_font)
    button_search_player.place(relx=0.5, rely=0.4, anchor="center")


def draw_choose_difficulty():
    bold_font = font.Font(family="Helvetica", size=12, weight="bold")
    label_team_name = tk.Label(root, text="Choose difficulty:", font=bold_font)
    label_team_name.place(relx=0.5, rely=0.15, anchor="center")

    button_back = tk.Button(root, text="Back", command=back_to_homepage, width=10, height=1, font=bold_font)
    button_hard = tk.Button(root, text="Hard", command=lambda: choose_team(2), width=17, height=3, font=bold_font)
    button_medium = tk.Button(root, text="Medium", command=lambda: choose_team(1), width=17, height=3, font=bold_font)
    button_easy = tk.Button(root, text="Easy", command=lambda: choose_team(0), width=17, height=3, font=bold_font)

    # Centralize the buttons vertically
    button_back.place(relx=0.05, rely=0.1, anchor="w")
    button_hard.place(relx=0.3, rely=0.5, anchor="center")
    button_medium.place(relx=0.5, rely=0.5, anchor="center")
    button_easy.place(relx=0.7, rely=0.5, anchor="center")


def draw_filtered_player(name):
    back_font = font.Font(family="Helvetica", size=12, weight="bold")
    button_search_player = tk.Button(root, text="Back", command=back_to_filtered, width=10, height=1, font=back_font)
    button_search_player.place(x=20, y=20)

    result = backend.get_player_by_name(name)
    if result is None:
        messagebox.showerror("Search Player", "Player do not exist.")
        search_player()
    else:
        static, dynamic = result
        draw_player_info(static, dynamic)


def draw_player_info(static, dynamic):
    bold_font = font.Font(family="Helvetica", size=12, weight="bold")
    table_font = font.Font(family="Helvetica", size=10, weight="bold")
    value_font = font.Font(family="Helvetica", size=9)
    static_str = f"Name: {static[1]} Birth:{static[2]} Nationality:{static[3]}"

    label_hello = tk.Label(root, text=static_str, font=bold_font)
    label_hello.place(relx=0.5, rely=0.1, anchor="center")
    style = ttk.Style(root)
    style.configure("Treeview.Heading", font=table_font)  # Apply the font to all headings

    tree = ttk.Treeview(root, columns=(
    "Year", "Position", "Rating", "Height", "Weight", "Worth", "Wage", "Jersey", "Team", "League"))

    # Remove the following line to exclude the "#0" column
    tree["show"] = "headings"

    tree.heading("Year", text="Year")
    tree.heading("Position", text="Position")
    tree.heading("Rating", text="Rating")
    tree.heading("Height", text="Height")
    tree.heading("Weight", text="Weight")
    tree.heading("Worth", text="Worth")
    tree.heading("Wage", text="Wage")
    tree.heading("Jersey", text="Jersey")
    tree.heading("Team", text="Team")
    tree.heading("League", text="League")

    tree.column("Year", anchor="center", width=50)
    tree.column("Position", anchor="center", width=110)
    tree.column("Rating", anchor="center", width=50)
    tree.column("Height", anchor="center", width=50)
    tree.column("Weight", anchor="center", width=50)
    tree.column("Worth", anchor="center", width=70)
    tree.column("Wage", anchor="center", width=50)
    tree.column("Jersey", anchor="center", width=50)
    tree.column("Team", anchor="center", width=180)
    tree.column("League", anchor="center", width=180)
    tree.tag_configure("value_font", font=value_font)
    tree.place(relx=0.5, rely=0.4, anchor="center")

    for i in dynamic:
        tree.insert("", "end", values=(i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]), tags=("value_font",))


def draw_choose_team():
    back_font = font.Font(family="Helvetica", size=12, weight="bold")
    button_back = tk.Button(root, text="Back", command=back_to_homepage, width=10, height=1, font=back_font)
    button_play_with_team = tk.Button(root, text="Play with team", command=lambda: start_game(team_name.get()), width=15, height=3, font=back_font)
    button_play_without_team = tk.Button(root, text="Play without team", command=lambda: start_game_without_team(), width=15, height=3, font=back_font)

    team_name = tk.Entry(root, width=25)

    # Centralize the widgets vertically
    button_back.place(relx=0.05, rely=0.1, anchor="w")
    team_name.place(relx=0.35, rely=0.4, anchor="center")
    button_play_with_team.place(relx=0.35, rely=0.5, anchor="center")
    button_play_without_team.place(relx=0.65, rely=0.5, anchor="center")


def register(entry_username, entry_password, entry_name):
    if backend.insert_user(entry_username, entry_password, entry_name):
        clear_root()
        draw_login_page()
    else:
        messagebox.showerror("Register Failed", "User already taken")


def draw_register_page():
    bold_font = font.Font(family="Helvetica", size=12, weight="bold")
    input_font = font.Font(family="Helvetica", size=11)
    back_font = font.Font(family="Helvetica", size=12, weight="bold")
    button_back = tk.Button(root, text="Back", command=login_page, width=10, height=1, font=back_font)
    button_back.place(x=20, y=20)
    label_username = tk.Label(root, text="Username:", font=bold_font)
    entry_username = tk.Entry(root, font=input_font)

    label_name = tk.Label(root, text="Name:", font=bold_font)
    entry_name = tk.Entry(root, font=input_font)

    label_password = tk.Label(root, text="Password:", font=bold_font)
    entry_password = tk.Entry(root, show="*", font=input_font)

    button_register = tk.Button(root, text="Register", width=13, command=lambda: register(entry_username.get(), entry_password.get(), entry_name.get()), font=bold_font)

    # Centralize the widgets
    label_username.place(relx=0.5, rely=0.3, anchor="center")
    entry_username.place(relx=0.5, rely=0.35, anchor="center")
    label_name.place(relx=0.5, rely=0.4, anchor="center")
    entry_name.place(relx=0.5, rely=0.45, anchor="center")
    label_password.place(relx=0.5, rely=0.5, anchor="center")
    entry_password.place(relx=0.5, rely=0.55, anchor="center")
    button_register.place(relx=0.5, rely=0.7, anchor="center")
    button_register = tk.Button(root, text="Register", command=lambda: register(entry_username.get(), entry_password.get(), entry_name.get()))


if __name__ == "__main__":
    backend.check()
    root = create_root()
    draw_login_page()
    root.mainloop()

