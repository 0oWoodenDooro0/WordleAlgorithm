import allow_words
import wordle

# for answer in allow_words.words:
#     result = None
#     times = 0
#     while True:
#         guess = wordle.recommend_word(result)
#         color = wordle.check_color(answer, guess)
#         result = wordle.get_possible_result1(guess, color, result)
#         times += 1
#         if len(result) == 1 and answer in result:
#             if times > 6:
#                 print(answer)
#                 print(times)
#             break

for answer in allow_words.words:
    print(answer)
    result = None
    letter_count = None
    gray_letter_set = None
    times = 0
    flag = False
    while True:
        if flag:
            guess = wordle.recommend_word(result)
        else:
            guess = wordle.recommend_other_word(letter_count, gray_letter_set)
        print(guess)
        color = wordle.check_color(answer, guess)
        # print(color)
        result, letter_count, gray_letter_set, flag = wordle.get_possible_result2(guess, color,
                                                                                  result,
                                                                                  letter_count,
                                                                                  gray_letter_set)
        # print(result, flag, letter_count, gray_letter_set)
        times += 1
        if len(result) == 1 and answer in result:
            if times > 6:
                print(answer)
                print(times)
            break
