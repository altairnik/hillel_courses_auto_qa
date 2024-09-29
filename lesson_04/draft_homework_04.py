# task 1-3
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
# print(adwentures_of_tom_sawer)
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
# print(adwentures_of_tom_sawer)
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
# print(adwentures_of_tom_sawer)
adwentures_of_tom_sawer = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer)
# print(adwentures_of_tom_sawer)

# task 4
i = 0
for symbol in adwentures_of_tom_sawer:
    if symbol == 'h':
        i += 1
# print(f'There are {i} characters "h" in the text')
# print(adwentures_of_tom_sawer.count('h'))

# task 05
Upper_words = adwentures_of_tom_sawer.split()
word = 0
# test = ['Wer', 'wer', 'n', '.', 'Rt']
for elem in Upper_words:
    if elem.istitle():
        word += 1
# print(f'Number of words with capital letter - {word}')

# task 06
first_index = adwentures_of_tom_sawer.find('Tom')
second_index = adwentures_of_tom_sawer.find('Tom', first_index + len('Tom'), len(adwentures_of_tom_sawer))
# print(second_index)

# task 07
# adwentures_of_tom_sawer_sentences = None
# adwentures_of_tom_sawer = adwentures_of_tom_sawer. replace('. ', '.')
# print(adwentures_of_tom_sawer)
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')
# adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split()
print(adwentures_of_tom_sawer_sentences)
# тут у меня почету то в конце списка появилось пустое значение ¯\_(ツ)_/¯
# поетому я не нашел ничего лучшего, чем немножко нагомнокодить в 10 задании :-|
# print(adwentures_of_tom_sawer_sentences)

# task 08
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
# for elements in adwentures_of_tom_sawer_sentences:
#     print(elements)
# for index in adwentures_of_tom_sawer_sentences:
#     if index.startswith('By the time'):
#         print('Yes')
#     else:
#         print('No')

# # task 10
# Окуратно, тут код не приятно пахнет L:)
# если бы в 7 таске все было нормально то можно было сделать немного красивше)
# str = str(adwentures_of_tom_sawer_sentences[len(adwentures_of_tom_sawer_sentences) -1])
words = adwentures_of_tom_sawer_sentences[-2]
print(len(words))


