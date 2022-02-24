import allow_words
import wordle

for answer in ['abate']:
    print(answer)
    result = None
    times = 0
    while True:
        guess = wordle.recommend_word(result)
        print(guess)
        color = wordle.check_color(answer, guess)
        print(color)
        result = wordle.get_possible_result(guess, color, result)
        print(result)
        times += 1
        if len(result) == 1 and answer in result:
            print(times)
            break
