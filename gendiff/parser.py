def build_diff_item(key, status, old_value, new_value=None):
    return {
        "key": key,
        "status": status,
        "old_value": str(old_value).lower(),
        "new_value": str(new_value).lower(),
    }


def generate_diff(obj1: dict, obj2: dict) -> str:
    # determining key groups with sets
    keys_set1 = set(obj1.keys())
    keys_set2 = set(obj2.keys())
    all_keys = keys_set1 | keys_set2
    set1_complement = keys_set1 - keys_set2
    set2_complement = keys_set2 - keys_set1

    # create an inner function to avoid passing objects back and forth
    def get_key_content(key):
        if key in set1_complement:
            return (key, "removed", obj1[key], None)
        elif key in set2_complement:
            return (key, "added", None, obj2[key])
        else:
            if obj1[key] == obj2[key]:
                return (key, "unchanged", obj1[key], obj2[key])
            else:
                return (key, "changed", obj1[key], obj2[key])

    # get list of statuses
    content = list(map(get_key_content, sorted(all_keys)))
    diff = []
    for item in content:
        key, status, old_value, new_value = item
        diff.append(build_diff_item(key, status, old_value, new_value))

    string_view = generate_str_view(diff)
    return string_view


def generate_str_view(diff_obj) -> str:
    if not diff_obj:
        return "{}"

    result = []
    # two spaces
    indent = "  "
    for item in diff_obj:
        item_string = ""
        old_value_template = f"{item['key']}: {item['old_value']}"
        new_value_template = f"{item['key']}: {item['new_value']}"

        # still can be simplified
        if item["status"] == "changed":
            item_string = (
                f"{indent}- {old_value_template}\n"
                f"{indent}+ {new_value_template}"
            )
        elif item["status"] == "added":
            item_string = f"{indent}+ {new_value_template}"
        elif item["status"] == "unchanged":
            item_string = f"{indent}  {old_value_template}"
        elif item["status"] == "removed":
            item_string = f"{indent}- {old_value_template}"
        result.append(item_string)

    formatted_result = "\n".join(result)
    return "{\n" + formatted_result + "\n}"
