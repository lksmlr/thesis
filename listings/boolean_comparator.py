class BooleanComparator(Comparator):
    def compare(self, pred_value: str, gt_value: str) -> Dict:
        is_correct = pred_value == gt_value
        ...