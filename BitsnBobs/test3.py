import os

delimiter = {
    "dot": ".",
    "dash": "-",
    "underscore": "_"
}

data = {
    "directory": "",
    "file_name": "",
    "base_name": "",
    "path_no_ext": "",
    "extension": "",
    "replace_name": "",
    "remove_string": "",
    "remove_first": "",
    "remove_last": "",
    "prefix": "",
    "suffix": "",
    "delimiter": "",
    "counter": ""
}

image_paths_list = ["C:/Users/fresh/Desktop/repos/easywatermark/images/_MG_1893_.jpg",
                    "C:/Users/fresh/Desktop/repos/easywatermark/images/_MG_1894_.jpg",
                    "C:/Users/fresh/Desktop/repos/easywatermark/images/_MG_1895_.jpg"]

box_replace_name = "kjhl"
box_prefix = ""
box_suffix = ""
dm = delimiter["underscore"]
counter = False


def run_rename(path, prefix, replace_name, base_name, suffix, count, extension):
    vars_list = []
    if replace_name:
        base_name = ""
        vars_list = [prefix, replace_name, base_name, suffix, count]
    else:
        vars_list = [prefix, base_name, suffix, count]

    used_vars = [var for var in vars_list if var]
    filename = dm.join(used_vars) + extension
    full_path = os.path.join(path, filename)

    print(full_path)

    # if replace_name:  # If the file name is being replaced, use these variables
    #     vars_list = [prefix, replace_name, suffix, count]
    # else:
    #     name_no_prefix = ""
    #     if base_name[0] == dm:
    #         if prefix:
    #             name_no_prefix = base_name.removeprefix(base_name[0])
    #             vars_list = [prefix, name_no_prefix, suffix, count]
    #             print(vars_list)
    #         else:
    #             vars_list = [base_name, suffix, count]
    #     else:
    #         vars_list = [base_name, suffix, count]
    #
    #     name_no_suffix = ""
    #     if base_name[-1] == dm:
    #         if suffix:
    #             name_no_suffix = name_no_prefix.removesuffix(base_name[-1])
    #             vars_list = [prefix, name_no_suffix, suffix, count]
    #             print(vars_list)
    #         else:
    #             vars_list = [prefix, base_name, count]
    #     else:
    #         vars_list = [prefix, base_name, count]


# Set data dictionary
def set_data(image_path):
    data["directory"], data["file_name"] = os.path.split(image_path)
    data["path no ext"], data["extension"] = os.path.splitext(image_path)
    data["base_name"] = data["file_name"].replace(data["extension"], "")
    data["delimiter"] = dm
    if box_replace_name:
        data["replace_name"] = box_replace_name
    if box_prefix:
        data["prefix"] = box_prefix
    if box_suffix:
        data["suffix"] = box_suffix
    if counter is True:
        data["counter"] = f"{index:04}"


index = 1
for image in image_paths_list:
    set_data(image)
    run_rename(data["directory"] + "/", data["prefix"], data["replace_name"], data["base_name"], data["suffix"],
               data["counter"],
               data["extension"])
    index += 1
