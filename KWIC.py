import streamlit as st

def get_sentence(txt):
    lineset = []
    pre = 0
    for j, char in enumerate(txt):
        flag = (j == len(txt) - 1)
        if char == '\n' or flag:
            sentence = txt[pre:j + flag]
            lineset.append(sentence)
            pre = j + 1
    return lineset

def sentence_to_words(lineset):
    words_set = []
    for sentence in lineset:
        x = 0
        y = 0
        result = []
        for i in sentence:
            if i == ' ' or i == ',' or i == '.' or i == '、':
                if x != 0:  # 第二格单词前面存在空格需往后移一格，剔除空格
                    q = sentence[x + 1:y:1]
                    x = y  # 记录位置，从x处继续提取
                    result.append(q)
                elif x == 0:  # 第一个单词前没有空格
                    q = sentence[x:y:1]
                    x = y
                    result.append(q)
            if y == len(sentence) - 1:  # 用于提取最后一个单词
                q = sentence[x + 1:y + 1:1]
                result.append(q)
            y = y + 1
        for i in result:
            if i == '':
                result.remove('')
        words_set.append(result)
    return words_set

def words_shift(words):
    words_shifted = []
    words_shifted = words[1:]
    words_shifted.append(words[0])
    return words_shifted

def alphabetizer(circle_list):
    circle_list_sorted = []
    for words in circle_list:
        if len(circle_list_sorted) == 0:
            circle_list_sorted.append(words)
        else:
            j = 0
            for words_sorted in circle_list_sorted:
                print(words_sorted[0][0] + '\n')
                print(words[0][0])
                if words_sorted[0][0] >= words[0][0]:
                    break
                j += 1
            circle_list_sorted.insert(j, words)
    return circle_list_sorted

def kwic(txt):
    lineset = get_sentence(txt)
    words_set = sentence_to_words(lineset)
    kwic_list = []
    for i, words in enumerate(words_set):
        circle_list = []
        temp_words = words
        for j in range(len(words)):
            circle_list.append(temp_words)
            temp_words =words_shift(temp_words)
        circle_list = alphabetizer(circle_list)
        kwic_list.append(circle_list)
    return kwic_list

txt = st.text_area('请输入文本', '')
kwic_list = kwic(txt)
st.write('kwic结果')
for idx, line_kwic in enumerate(kwic_list):
    st.write('第 {} 行kwic结果：'.format(idx + 1))
    for words in line_kwic:
        result = ''
        for word in words:
            result = result + word + ' '
        st.write(result + '\n')