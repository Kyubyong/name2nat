from name2nat import Name2nat

my_nanat = Name2nat()

names = ["Donald Trump", # American
         "Moon Jae-in", # Korean
         "Shinzo Abe", # Japanese
         "Xi Jinping", # Chinese
         "Joko Widodo", # Indonesian
         "Angela Merkel", # German
         "Emmanuel Macron", # French
         "Kyubyong Park", # Korean
         "Yamamoto Yu", # Japanese
         "Sara Abbas"] # Chinese
result = my_nanat(names, top_n=3)
print(result)
# (name, [(nationality, prob), ...])
# Note that prob of 1.0 indicates the name exists
# in Wikipedia.
# [
# ('Donald Trump', [('American', 1.0)])
# ('Moon Jae-in', [('Korean', 1.0)])
# ('Shinzo Abe', [('Japanese', 1.0)])
# ('Xi Jinping', [('Chinese', 1.0)])
# ('Joko Widodo', [('Indonesian', 1.0)])
# ('Angela Merkel', [('German', 1.0)])
# ('Emmanuel Macron', [('French', 1.0)])
# ('Kyubyong Park', [('Korean', 0.9985014200210571), ('American', 0.000289416522718966), ('Bhutanese', 0.00025851925602182746)])
# ('Yamamoto Yu', [('Japanese', 0.7050493359565735), ('Taiwanese', 0.12779785692691803), ('Chinese', 0.04263153299689293)])
# ('Jing Xu', [('Chinese', 0.8626819252967834), ('Taiwanese', 0.09901007264852524), ('American', 0.022995812818408012)])
# ]