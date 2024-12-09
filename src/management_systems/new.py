import requests
import json

response = requests.get("https://coderbyte.com/api/challenges/json/wizard-list")
# response = requests.get("https://coderbyte.com/api/challenges/json/date-list")
data = response.json()

# write your solution here
# print the response data 
# print("Orijinal data: ", json.dumps(data, indent=4))

# Function to sort dictionary keys case-insensitivity 
def sort_keys_case_insensitive(d):
    if isinstance(d, dict):
        return{k: sort_keys_case_insensitive(v) for k, v in sorted(d.items(), key=lambda item: item[0].lower())}
    elif isinstance(d, list):
        return [sort_keys_case_insensitive(i) for i in d]
    else:
        return d


# Helper function to convert dict to hashable type
def make_hashable(d):
    if isinstance(d, dict):
        return tuple(sorted((k, make_hashable(v)) for k, v in d.items()))
    elif isinstance(d, list):
        return tuple(make_hashable(i) for i in d)
    else:
        return d


# Function to remove dulicate dictionaries from list 
def remove_duplicate_dicts(lst):
    seen = []
    seen_set = set()
    for d in lst:
        d_hashable = make_hashable(d)
        if d_hashable not in seen_set:
            seen.append(d)
            seen_set.add(d_hashable)
    return seen


# Helper function to check if a dictionary or list is empty after removing empty properties 
def is_non_empty(d):
    if isinstance(d, dict):
        return any(v not in ("", None) for v in d.values())
    elif isinstance(d, list):
        return any(v not in ("", None) for v in d)
    return d not in ("", None)


# # Function to remove dict properties with all values set an empty string or None
def remove_empty_properties(d):
    if isinstance(d, dict):
        cleaned_dict = {}
        for k, v in d.items():
            if v not in ("", None):
                if isinstance(v, dict):
                    v = remove_empty_properties(v)
                    if is_non_empty(v):
                        cleaned_dict[k] = v
                elif isinstance(v, list):
                    v = remove_empty_properties(v)
                    if v:
                        cleaned_dict[k] = v
                else:
                    cleaned_dict[k] = v
            else:
                print(f"Removing properties: {k} with value: {v}")
        return cleaned_dict
    elif isinstance(d, list):
        return [remove_empty_properties(i) for i in d if i not in ("", None)]
    else:
        return d                          

# # Function to remove dict properties with all values set an empty string or None
# def remove_empty_properties(d):
#     if isinstance(d, dict):
#         return {k: remove_empty_properties(v) for k, v in d.items() if v not in ("", None) and not (isinstance(v, dict) and all(val in ("", None) for val in v.values()))}
#     elif isinstance(d, list):
#         return [remove_empty_properties(i) for i in d if i not in ("", None)]
#     else:
#         return d

# print("Sorted data:" , json.dumps(sorted_data, indent=4))
# Function to flatted nested lists and dicts 
# def flatten_data(d):
#     if isinstance(d, dict):
#         return {k: flatten_data(v) for k, v in d.items()}
#     elif isinstance(d, list):
#         return [flatten_data(i) for i in d]
#     else:
#         return d



# Remove duplicate dictionaries from list, varFilterCg and __define-ocg__
def process_nested_data(d):
    if isinstance(d, dict):
        return {k: process_nested_data(v) for k, v in d.items()}
    elif isinstance(d, list):
        varFiltersCg = remove_duplicate_dicts(d)  # __define-ocg__
        return [process_nested_data(i) for i in varFiltersCg]
    else:
        return d

# Sort keys case-insensivity
sorted_data = sort_keys_case_insensitive(data)

# # Flatten the data
# flattened_data = flatten_data(sorted_data)

processed_data = process_nested_data(sorted_data)
# print("Processed data: ", json.dumps(processed_data, indent=4))
# Remove empty properties 
final_data = remove_empty_properties(processed_data)
# print("Final data: ", json.dumps(final_data, indent=4))
# Convert back to JSON format
json_output = json.dumps(final_data, indent=4)

# print(json_output)
print("JSON output: ", json_output)
print(response)






