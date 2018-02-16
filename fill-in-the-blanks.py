import sys


blank1 = ["___1___", "___1___s", "___1___.",
          "___1___?", "___1___!", "___1___,"]

blank2 = ["___2___", "___2___s", "___2___.",
          "___2___?", "___2___!", "___2___,"]

blank3 = ["___3___", "___3___s", "___3___.",
          "___3___?", "___3___!", "___3___,"]

blank4 = ["___4___", "___4___s", "___4___.",
          "___4___?", "___4___!", "___4___,"]


easy_level = "Python is an interpreted high-level programming ___1___ for " \
             "general-purpose programming. " \
             "In python is recommended to know the basics of ___2___ since " \
             "every keyword and the most part " \
             "of the python community discussions are in ___2___.\n" \
             "Like JavaScript and other languages, python also have " \
             "___3___s that you can assign to lists, strings, " \
             "etc....Python have two types of loop, we have the for loops, " \
             "and the ___4___ loops. "

easy_level_answer = ["language", "english", "variable", "while"]

medium_level = "Hypertext Markup Language (HTML) is the standard markup " \
               "language for creating web ___1___ " \
               "and web applications. With Cascading Style Sheets (CSS) " \
               "and ___2___ it forms a triad of " \
               "cornerstone technologies for the World Wide Web.\n" \
               "Web browsers receive ___3___ documents from a web server or" \
               " from local storage and render them into " \
               "multimedia web pages. HTML describes the ___4___ of a web" \
               " page semantically " \
               "and originally included cues for the appearance of " \
               "the document."

medium_level_answer = ["pages", "JavaScript", "HTML", "structures"]

hard_level = "In python you can create an iterator object from a list by " \
             "passing the given list to the ___1___ " \
             "function. If a function contains at least one yield statement" \
             ", it becomes a ___2___ function.\n" \
             "The lambda operator or lambda function is a way to create " \
             "small anonymous functions, " \
             "i.e. functions without a ___3___. ___4___ is a null operation," \
             " when it is executed, nothing happens,\n" \
             "it is useful as a placeholder when a statement is required" \
             " syntactically, but no code needs to be executed."


hard_level_answer = ["iter()", "generator", "name", "Pass"]


def play_game():
    # the function that starts the game

    destiny = raw_input("Hello, so its you the chosen one, the great warrior "
                        "of knowledge, i was imagining someone "
                        "stronger and prettiest, but ok. "
                        "You accept your destiny, your prophecy, "
                        "your fate? Yes/No \n").lower()
    if destiny == "yes" or destiny == "y":
        print "So you accepted the adventure, reaching places that no man or" \
              " women has been before, "
        choose_lvl()
    else:
        print "Weak..."


def choose_lvl():

    # Function that ask the user for a level

    pick_level = raw_input("choose yor level: Easy, Medium, or if you dare,"
                           " Hard \n").lower()
    if pick_level == "easy":
        return fill_blanks(easy_level, pick_level)
    if pick_level == "medium":
        return fill_blanks(medium_level, pick_level)
    if pick_level == "hard":
        return fill_blanks(hard_level, pick_level)
    else:
        print "Sorry i didn't understand, type again please."
        return choose_lvl()


def lvl_answers(user_input, word_index, pick_level):
    # take as inputs the chosen level, the word in question, and the user_input
    # to compare. Assimilates the right answers for that level

    if pick_level == "easy":
        if user_input == easy_level_answer[word_index]:
            return True
    if pick_level == "medium":
        if user_input == medium_level_answer[word_index]:
            return True
    if pick_level == "hard":
        if user_input == hard_level_answer[word_index]:
            return True
    return False


def special_blank(word):
    # takes an input, the blank to be replaced, then verifies if it contain any
    # special termination, if so, return the special termination

    last_letter = word[len(word) - 1]
    if last_letter == 's':
        return 's'
    if last_letter == '.':
        return '.'
    if last_letter == '!':
        return '!'
    if last_letter == '?':
        return '?'
    if last_letter == ';':
        return ';'
    else:
        return ""


def wrong_answer(life, level_text, pick_level):
    # Take as inputs, level, level text, and the level picked, the function is
    # called when the user misses the answers, it discount 1 in life, and check
    # if the user are out of lives, if so, the game over function is called

    life -= 1
    if life == 0:
        game_over(level_text, pick_level)
    print "Wrong, mann, lets try again dude"
    return life


def life_initialize(pick_level):
    easy_life, medium_life, hard_life = 4, 3, 2
    if pick_level == "easy":
        return easy_life
    if pick_level == "medium":
        return medium_life
    if pick_level == "hard":
        return hard_life


def game_over(level_text, pick_level):

    # Take as inputs the level text, the picked level, this function tells the
    # player that the game is over and ask if he wanna try again, if so, return
    # the choose_lvl function.

    print "Game Over!"
    try_again = raw_input("Wanna try again? Y/N \n").lower()
    if try_again == "y":
        level_text = " ".join(level_text)
        return fill_blanks(level_text, pick_level)
    else:
        try_again = raw_input("Wanna play another level? Y/N \n").lower()
        if try_again == "y":
            return choose_lvl()
        else:
            sys.exit(0)


def blank_handler_first(blank_controller, pick_level, answer1, replaced, word,
                        life, level_text):

    # Take as inputs, blank controller(check if the blank was already answered)
    #  , the level picked, the blank controller
    # answer index, "replaced" string, the word, the number of lives, and the
    # level text, the function checks if
    # the question was already asked/answered , if not, will be asked the
    # answer for the blank in occasion, if the
    # answer its right, the user input is add to replaced, if not, life is
    # discounted by 1 when wrong_answer
    # function is called

    word_index = 0
    if blank_controller[answer1] == "":
        while True:
            user_input = raw_input("What you think its ___1___? you have "
                                   + str(life) + " Life points left \n")
            if lvl_answers(user_input, word_index, pick_level):
                replaced.append(user_input + str(special_blank(word)))
                blank_controller[answer1] = user_input
                return replaced, blank_controller, life
            life = wrong_answer(life, level_text, pick_level)
    replaced.append(blank_controller[answer1] + str(special_blank(word)))
    return replaced, blank_controller, life


def blank_handler_others(blank_controller, answer1, answer2,
                         level_text_to_print, life, pick_level, word, replaced,
                         level_text, word_index, blank):

    # Pretty much the same thing as blank_handler_first, but the difference is
    #  that prints the level text filed with the previously
    #  answers before asking the user answer for the next blank

    blank_number = str(answer2 + 1)
    if blank_controller[answer2] == "":
        for key, item in enumerate(level_text_to_print):
            if item in blank:
                level_text_to_print[key] = blank_controller[answer1] \
                                           + str(special_blank(item))
        level_text_to_print = " ".join(level_text_to_print)
        print ('\n#####  RIGHT! #####\n\n') + level_text_to_print + '\n'
        level_text_to_print = level_text_to_print.split()
        while True:
            user_input = raw_input("What you think its ___" + blank_number +
                                   "___? you have "
                                   + str(life) + " Life points left \n")
            if lvl_answers(user_input, word_index, pick_level):
                replaced.append(user_input + str(special_blank(word)))
                blank_controller[answer2] = user_input
                return replaced, blank_controller, level_text_to_print, life
            life = wrong_answer(life, level_text, pick_level)
    replaced.append(blank_controller[answer2] + str(special_blank(word)))
    return replaced, blank_controller, level_text_to_print, life


def blank_replacer(level_text, blank_controller, life, pick_level, replaced,
                   level_text_to_print):

    # That's the function that brings all together, checking every word and
    # fillings the blanks.

    second_index, third_index, fourth_index = 1, 2, 3
    answer1, answer2, answer3, answer4 = 0, 1, 2, 3
    for word in level_text:
        blank_resolved = False
        if word in blank1:
            replaced, blank_controller, life = blank_handler_first(
                blank_controller, pick_level, answer1, replaced, word, life,
                level_text)
            blank_resolved = True
        if word in blank2:
            replaced, blank_controller, level_text_to_print, life = \
                blank_handler_others(blank_controller, answer1, answer2,
                                     level_text_to_print, life,
                                     pick_level, word, replaced,
                                     level_text, second_index, blank1)
            blank_resolved = True
        if word in blank3:
            replaced, blank_controller, level_text_to_print, life = \
                blank_handler_others(blank_controller, answer2, answer3,
                                     level_text_to_print, life,
                                     pick_level, word, replaced,
                                     level_text, third_index, blank2)
            blank_resolved = True
        if word in blank4:
            replaced, blank_controller, level_text_to_print, life = \
                blank_handler_others(blank_controller, answer3, answer4,
                                     level_text_to_print, life,
                                     pick_level, word, replaced,
                                     level_text, fourth_index, blank3)
            blank_resolved = True
        if not blank_resolved:
            replaced.append(word)
    return replaced


def fill_blanks(level_text, pick_level):
    # takes two inputs, the level chosen and the text of the respective level.
    # Creates an empty list named replaced, verifies level text word by word,
    # if the word is not a blank to fill, add word to replaced, if its a blank,
    # ask the user the answer for that blank, if the user input is the right
    # answer, add the user input to replaced, if not, the user is asked to try
    # again, with 1 life less. At the end, if the user scores all 4 answers,
    # game is closed. If the user lost all lives, will be asked to him if he
    # wanna try again.

    life = life_initialize(pick_level)
    print level_text + "\n"
    replaced = []
    level_text = level_text.split()
    level_text_to_print = level_text
    blank_controller = ["", "", "", ""]
    replaced = blank_replacer(level_text, blank_controller, life, pick_level,
                              replaced, level_text_to_print)
    replaced = " ".join(replaced)
    print "\n $#$##$#$#$#$#$#$#$  YOU  WIN !! #$#$#$#$#$#$$#\n\n"
    print replaced + "\n\n"
    try_again = raw_input("Wanna play another level? Y/N \n")
    if try_again == "y" or try_again == "Y":
        return choose_lvl()
    else:
        sys.exit(0)


play_game()
