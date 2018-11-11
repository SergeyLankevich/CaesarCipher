key = input('Введите ключ для шифрования(букву алфавита):')
if key.isalpha() is True and len(key) == 1:
    with open('input.txt') as f_in:
        text = f_in.read()
        if text.isalpha() is True:
            lower_alphabet = 'abcdefghijklmnopqrstuvxwyz'
            upper_alphabet = lower_alphabet.upper()
            num_key = lower_alphabet.find(key.lower())
            new_lower_alphabet = lower_alphabet[num_key:] + lower_alphabet[:num_key]
            new_upper_alphabet = new_lower_alphabet.upper()
            for i in range(len(lower_alphabet)):
                text = text.replace(lower_alphabet[i], new_lower_alphabet[i])
                text = text.replace(upper_alphabet[i], new_upper_alphabet[i])
                i += 1
            with open('output.txt', 'w') as f_out:
                f_out.write(text)
        else:
            print('Некорректный ввод текста. Текст не должен содержать чисел! Шифр Цезаря не предполагает\n'
                  'кодирование цифр, так что, чтобы враг не разгадал ваш план по численным значениям,\n'
                  'рекомендуем прописывать их буквенно.')
else:
    print('Некорректный ввод ключа, он должен состоять из одной буквы латинского алфавита.')




