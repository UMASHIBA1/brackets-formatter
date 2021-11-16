def formatter(raw_texts):
    formatted_text = ""
    tab_num = 0
    for raw_text in raw_texts:
        if raw_text == "(" or raw_text == "{" or raw_text == "[":
            tab_num += 1
            tab_str = "\t" * tab_num
            formatted_bracket = raw_text + "\n" + tab_str
            formatted_text += formatted_bracket
        elif raw_text == ")" or raw_text == "}" or raw_text == "]":
            tab_num -= 1
            tab_str = "\t" * tab_num
            formatted_bracket = "\n" + tab_str + raw_text
            formatted_text += formatted_bracket
        elif raw_text == ",":
            tab_str = "\t" * tab_num
            formatted_text += ",\n" + tab_str
        else:
            formatted_text += raw_text
    return formatted_text


# target_textにフォーマットしたい文字列を入れてください
target_text = "sample(1,2,3,4,[1,2,3], sample2{w:0, e:1})"

print(formatter(target_text))
