def calculate_field_based_f1_score(gt_jsons,
                                   pred_jsons,
                                   penalize_halluzinations: bool = False) -> float:
    ...
    fp = count_correct_fields

    if penalize_halluzinations:
        fp += count_halluzinated_fields
    ...