import allow_words


# 計算出所有字母在單字庫中出現的頻率
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


# 檢查顏色(相同的字母 guess不可超過answer的數量)
def check_color(answer, guess):
    answer_list = list(answer)
    color_list = ['⬜', '⬜', '⬜', '⬜', '⬜']
    for i in range(5):  # 確認字母與位置相同
        if guess[i] == answer[i] and guess[i] in answer_list:
            color_list[i] = '🟩'
            answer_list.remove(guess[i])
    for i in range(5):  # 尋找向同位置以外的相同字母
        for j in range(5):
            if guess[i] == answer[j] and i != j and guess[i] in answer_list and color_list[i] != '🟩':
                color_list[i] = '🟨'
                answer_list.remove(guess[i])
                break
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


# 以單字出現頻率回傳較多未出現字母之單字
def recommend_other_word(letter_count, gray_letter_set, last_guess):
    if letter_count is None:
        letter_count = {}
    if gray_letter_set is None:
        gray_letter_set = set()
    word_list = set(allow_words.words)
    letter_dict = get_frequency()
    recommend_other_word_list = []
    for word in word_list:
        letter = set()
        f = 0
        if word == last_guess:
            break
        for i in range(5):
            if word[i] not in gray_letter_set and word[i] not in letter_count and word[i] not in letter:
                f += letter_dict[word[i]]
                letter.add(word[i])
        recommend_other_word_list.append((word, f))
    recommend_other_word_list.sort(key=lambda x: x[1], reverse=True)
    return recommend_other_word_list[0][0]


# 統計所有資料
def count(count_dict, times):
    if times in count_dict:
        count_dict[times] += 1
    else:
        count_dict[times] = 1
    return count_dict


# 依照顏色來判斷可能得結果 Solution1
def get_possible_result1(guess, color, result=None):
    if result is None:
        result = set(allow_words.words)
    remove_result = {guess}
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


# 前三次先找出不同的字母再判斷可能得結果 Solution2
def get_possible_result2(guess, color, times, result=None, letter_count=None, gray_letter_set=None):
    if result is None:
        result = set(allow_words.words)
    if letter_count is None:
        letter_count = {}
    if gray_letter_set is None:
        gray_letter_set = set()
    remove_result = {guess}
    green = ['-', '-', '-', '-', '-']
    yellow = ['-', '-', '-', '-', '-']
    gray = ['-', '-', '-', '-', '-']
    letter_current_count = {}

    for i in range(5):
        if color[i] == '🟩':
            green[i] = guess[i]
            if guess[i] in letter_current_count:
                letter_current_count[guess[i]] += 1
            else:
                letter_current_count[guess[i]] = 1
        elif color[i] == '🟨':
            yellow[i] = guess[i]
            if guess[i] in letter_current_count:
                letter_current_count[guess[i]] += 1
            else:
                letter_current_count[guess[i]] = 1
        else:
            gray[i] = guess[i]
            if gray[i] not in letter_current_count:
                gray_letter_set.add(gray[i])

    for letter in letter_current_count:
        if letter not in letter_count:
            letter_count[letter] = 1
        elif letter_current_count[letter] > letter_count[letter]:
            letter_count[letter] = letter_current_count[letter]

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
                if gray[i] != '-' and gray[i] in word and gray[i] not in letter_current_count:
                    remove_result.add(word)
                    break
                for j in letter_current_count:
                    if word.count(j) < letter_current_count[j]:
                        remove_result.add(word)
                        break

    is_letter_over_three = True

    if times <= 3 and len(result) >= 100:
        is_letter_over_three = False

    return result.difference(remove_result), letter_count, gray_letter_set, is_letter_over_three
