import allow_words
import wordle

for answer in allow_words.words:
    result = None
    times = 0
    while True:
        guess = wordle.recommend_word(result)
        # print(guess)
        color = wordle.check_color(answer, guess)
        # print(color)
        result = wordle.get_possible_result(guess, color, result)
        # print(result)
        times += 1
        if len(result) == 1 and answer in result:
            if times > 6:
                print(answer)
                print(times)
            break
