def calculate_field_based_f1_score(gt_jsons,
                                   pred_jsons,
                                   penalize_hallucinations: bool = False) -> float:
    ...
    fp = count_correct_fields

    if penalize_hallucinations:
        fp += count_hallucinated_fields
    ...