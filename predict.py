from name2nat import Name2nat

my_name2nat = Name2nat()

# test data
names = open("nana/test.src", 'r', encoding='utf8').read().splitlines()

results = my_name2nat(names, top_n=5, use_dict=False) # use_dict: dictionary retrieval. we don't want it for model prediction.
with open("test.pred", "w", encoding="utf8") as fout:
    for r in results:
        preds = r[-1]
        preds = ",".join(each[0] for each in preds)
        fout.write(preds + "\n")
