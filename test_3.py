# coding:utf-8

def level_3(state, c):
    if not c.isalpha():  # 先判断字符是否为是字母
        return state

    if state: # 如果元组不为空
        chars_found, state_lower, upper_count = state
    else:
        state_lower = ""
        upper_count = 0
        chars_found = ""

    if c.islower():  # 如果字符是小写字母
        if upper_count == 3:  # 如果大写字母的数量为3
            if state_lower:  # 如果找到符合条件的小写字母
                chars_found += state_lower

            state_lower = c
        else:  
            state_lower = ""

        upper_count = 0

    else:
        upper_count += 1

    return chars_found, state_lower, upper_count

if __name__ == "__main__":
    with open('character.txt') as f:
        s = f.read()
    s += "x" # 最右边添加一个小写字母
    print reduce(level_3, s, ())[0]
