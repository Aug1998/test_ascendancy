import pandas as pd
import json

def get_normalized_list(list) :
    # 1. Sort by lenghortest first) so root brands become keys first
    sorted_list = sorted(pd.DataFrame(list).dropna()[0], key=len)
    mapped_names = {}

    # 2. Match names based on shared starting words
    for name in sorted_list:
        found_match = False
        
        for canonical in mapped_names.keys():
            # Check if the name starts with the canonical root name
            if name.startswith(canonical):
                mapped_names[name] = canonical
                found_match = True
                break
                
        # If it's a completely new brand name, it becomes its own canonical root
        if not found_match:
            mapped_names[name] = name

    with open("datas.json", "w") as json_file:
        json.dump(mapped_names, json_file, indent=4)

    return mapped_names
