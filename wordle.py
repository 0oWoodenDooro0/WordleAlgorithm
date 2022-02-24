import allow_words


# 計算出所有字母在單字中的出現的頻率
def get_frequency():
    letter_dict = {}

    for answer in allow_words.words:
        times = {}
        for i in range(5):
            if answer[i] not in letter_dict:
                letter_dict[answer[i]] = 1
                times[answer[i]] = 1
            elif answer[i] not in times:
                letter_dict[answer[i]] += 1
                times[answer[i]] = 1

    for i in letter_dict:
        letter_dict[i] = letter_dict[i] / len(allow_words.words)

    return letter_dict


# 確認是否是單字
def is_word(guess):
    if guess in allow_words.words + allow_words.allow:
        return True
    else:
        return False


# 檢查顏色
def check_color(answer, guess):
    answer_list = list(answer)
    color_list = ['⬜', '⬜', '⬜', '⬜', '⬜']
    for i in range(5):
        for j in range(5):
            if guess[i] == answer[j] and answer[j] in answer_list:
                print(guess[i], answer[j], i, j, answer_list)
                if i == j:
                    color_list[i] = '🟩'
                    answer_list.remove(answer[j])
                elif color_list[i] != '🟩':
                    color_list[i] = '🟨'
                    answer_list.remove(answer[j])
    return ''.join(map(str, color_list))


# 以單字出現頻率回傳最有可能的單字
def recommend_word(word_list=None):
    if word_list is None:
        word_list = set(allow_words.words)
    letter_dict = get_frequency()
    recommend_word_list = []
    for word in word_list:
        letter = set()
        f = 0
        for i in range(5):
            if word[i] not in letter:
                f += letter_dict[word[i]]
                letter.add(word[i])
        recommend_word_list.append((word, f))
    recommend_word_list.sort(key=lambda x: x[1], reverse=True)
    return recommend_word_list[0][0]


# 依照顏色來判斷可能得結果
def get_possible_result(guess, color, result=None):
    if result is None:
        result = set(allow_words.words)
    remove_result = set()
    green = ['-', '-', '-', '-', '-']
    yellow = ['-', '-', '-', '-', '-']
    gray = ['-', '-', '-', '-', '-']
    letter_count = {}
    for i in range(5):
        if color[i] == '🟩':
            green[i] = guess[i]
            if guess[i] in letter_count:
                letter_count[guess[i]] += 1
            else:
                letter_count[guess[i]] = 1
        elif color[i] == '🟨':
            yellow[i] = guess[i]
            if guess[i] in letter_count:
                letter_count[guess[i]] += 1
            else:
                letter_count[guess[i]] = 1
        else:
            gray[i] = guess[i]

    if green != ['-', '-', '-', '-', '-']:
        for word in result:
            for i in range(5):
                if green[i] != '-' and green[i] != word[i]:
                    remove_result.add(word)
                    break

    if yellow != ['-', '-', '-', '-', '-']:
        for word in result:
            for i in range(5):
                if yellow[i] != '-' and yellow[i] not in word:
                    remove_result.add(word)
                    break
                elif yellow[i] != '-' and yellow[i] == word[i]:
                    remove_result.add(word)
                    break

    if gray != ['-', '-', '-', '-', '-']:
        for word in result:
            for i in range(5):
                if gray[i] != '-' and gray[i] in word and gray[i] not in letter_count:
                    remove_result.add(word)
                    break
                for j in letter_count:
                    if word.count(j) < letter_count[j]:
                        remove_result.add(word)
                        break

    return result.difference(remove_result)
