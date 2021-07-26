def word_repeated(string):
    if string != '':
        repeated_word = ''
        str_arr = string.replace(',', '').split(' ')
        for i in range(0, len(str_arr)):
            counter_word = 1
            for j in range(0,len(str_arr)):
                if str_arr[i] == str_arr[j]:
                    counter_word += 1
                if counter_word == 3:
                    repeated_word = str_arr[i]
                    return  repeated_word
        return 'No repeated words'
    else:
        raise Exception('String is empty')


if __name__ == '__main__':
    rep_word = word_repeated('my name is hadi nofal , hadi is software engineer , is')
    print(rep_word)