from rapidfuzz import fuzz

class NameComparator(Comparator):
    def __init__(self, threshold=0.80):
        self.threshold = threshold

    def compare(self, pred_value: str, gt_value: str) -> Dict:
        # calculate levenshtein-similarity
        similarity = fuzz.ratio(pred_value.lower(), gt_value.lower()) / 100.0
        is_correct = similarity >= self.threshold

        ...