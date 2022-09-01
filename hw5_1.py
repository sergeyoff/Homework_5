#Напишите программу, удаляющую из текста все слова, содержащие "абв"

l = 'забвение и сабвей  переросло в слова зимбабвиец и гравюра'
l_word = l.split(' ')
l_frag = 'абв'
l_new = []
for word in l_word:
    if l_frag not in word:
        l_new.append(word)
l_new
' '.join(l_new)
print(l_new)
