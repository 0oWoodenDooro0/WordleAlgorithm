import allow_words
import wordle

# count = {}
# for answer in allow_words.words:
#     result = None
#     times = 0
#     while True:
#         guess = wordle.recommend_word(result)
#         color = wordle.check_color(answer, guess)
#         result = wordle.get_possible_result1(guess, color, result)
#         times += 1
#         if guess == answer:
#             count = wordle.count(count, times)
#             break
#
# print("Solution1:", sorted([(key, value) for key, value in count.items()]), "\nsum:", len(allow_words.words))

count = {}
for answer in ['boost']:
    guess = None
    result = None
    letter_count = None
    gray_letter_set = None
    times = 0
    flag = False
    while True:
        if flag:
            guess = wordle.recommend_word(result)
        else:
            guess = wordle.recommend_other_word(letter_count, gray_letter_set, guess)
        print(guess)
        color = wordle.check_color(answer, guess)
        print(color)
        result, letter_count, gray_letter_set, flag = wordle.get_possible_result2(guess, color, times,
                                                                                  result,
                                                                                  letter_count,
                                                                                  gray_letter_set)
        times += 1
        if guess == answer:
            count = wordle.count(count, times)
            break

print("Solution2:", sorted([(key, value) for key, value in count.items()]), "\nsum:", len(allow_words.words))

# Solution2: [(1, 1), (2, 1), (3, 86), (4, 965), (5, 984), (6, 230), (7, 37), (8, 5)] 2, 5
# Solution2: [(1, 1), (2, 1), (3, 101), (4, 952), (5, 932), (6, 279), (7, 37), (8, 6)] 3 6
# Solution2: [(1, 1), (2, 1), (3, 781), (4, 1102), (5, 347), (6, 62), (7, 13), (8, 1), (9, 1)] 3 100
# Solution2: [(1, 1), (2, 1), (3, 880), (4, 988), (5, 330), (6, 84), (7, 16), (8, 6), (9, 2), (10, 1)] 3, 500
# Solution2: [(1, 1), (2, 1), (3, 869), (4, 1016), (5, 329), (6, 69), (7, 18), (8, 6)] 2 500
