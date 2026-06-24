import pandas as pd
import json
import re

def get_normalized_list(list) :
    # with open("initial_list.json", "w") as json_file:
    #     json.dump(list, json_file, indent=4)

    # 1. Sort by length (shortest first) so root brands become keys first
    sorted_list = sorted(pd.DataFrame(list).dropna()[0], key=len)
    mapped_names = {}

    # 2. Match names based on shared starting words (case-insensitive)
    for name in sorted_list:
        found_match = False
        normalized_name = name.strip()

        for canonical in mapped_names.keys():
            pattern = rf'^{re.escape(canonical.strip())}(\b|$)'
            if re.match(pattern, normalized_name, flags=re.IGNORECASE):
                mapped_names[name] = canonical
                found_match = True
                break

        # If it's a completely new brand name, it becomes its own canonical root
        if not found_match:
            mapped_names[name] = name

    # with open("final_list.json", "w") as json_file:
    #     json.dump(mapped_names, json_file, indent=4)

    return mapped_names
