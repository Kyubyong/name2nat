'''
precision @ {1,2,3,4,5}
'''
import argparse

def calc_precision(hits, total):
    return 100 * round(hits / total, 3)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gt", type=str, help="ground truth file path")
    parser.add_argument("--pred", type=str, help="prediction file path")
    hp = parser.parse_args()

    preds = open(hp.pred, "r", encoding="utf8").read().strip().splitlines()
    gts = open(hp.gt, "r", encoding="utf8").read().strip().splitlines()

    assert len(preds)==len(gts)

    hits1, hits2, hits3, hits4, hits5 = 0, 0, 0, 0, 0
    for pred, gt in zip(preds, gts):
        columns = pred.split(",")
        if gt in columns[:1]: hits1 += 1
        if gt in columns[:2]: hits2 += 1
        if gt in columns[:3]: hits3 += 1
        if gt in columns[:4]: hits4 += 1
        if gt in columns[:5]: hits5 += 1

    print("precision@1={}/{}={}".format(hits1, len(gts), calc_precision(hits1, len(gts))))
    print("precision@2={}/{}={}".format(hits2, len(gts), calc_precision(hits2, len(gts))))
    print("precision@3={}/{}={}".format(hits3, len(gts), calc_precision(hits3, len(gts))))
    print("precision@4={}/{}={}".format(hits4, len(gts), calc_precision(hits4, len(gts))))
    print("precision@5={}/{}={}".format(hits5, len(gts), calc_precision(hits5, len(gts))))

