# src/domain_rules.py

from typing import Dict, List, Tuple

def apply_domain_rules(scores_dict: Dict[str, float]) -> Tuple[str, List[str]]:
    """
    Determine the highest-priority label as 'primary' with domain logic:
      1) Money Movement-Inbound
      2) Money Movement-Outbound
      3) Commitment Change
      4) Fee Payment
      5) Closing Notice
      6) AU Transfer
      7) Adjustments
    Remaining labels become 'sub-requests'.
    """
    if not scores_dict:
        return None, []

    # sort by confidence descending
    sorted_labels = sorted(scores_dict.items(), key=lambda x: x[1], reverse=True)

    priority_order = [
        "Money Movement-Inbound",
        "Money Movement-Outbound",
        "Commitment Change",
        "Fee Payment",
        "Closing Notice",
        "AU Transfer",
        "Adjustments",
    ]

    primary = None
    sub_list = []
    for label, _ in sorted_labels:
        if primary is None and label in priority_order:
            primary = label
        else:
            sub_list.append(label)

    return primary, sub_list
