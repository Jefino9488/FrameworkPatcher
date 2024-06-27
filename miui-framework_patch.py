import os
import re
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def replace_string_in_file(file_path, search_string, replace_string):
    logging.info(f"Replacing string in file: {file_path}")
    with open(file_path, 'r') as file:
        content = file.read()

    modified_content = content.replace(search_string, replace_string)

    with open(file_path, 'w') as file:
        file.write(modified_content)
    logging.info(f"Completed string replacement in file: {file_path}")


def modify_smali_files(directories):
    classes_to_modify = [
        'android/inputmethodservice/InputMethodServiceInjector.smali',
        'android/view/DisplayInfoInjector$2.smali',
        'miui/util/HapticFeedbackUtil.smali'
    ]

    search_string = "com.baidu.input_mi"
    replace_string = "com.google.android.inputmethod.latin"

    for directory in directories:
        for class_file in classes_to_modify:
            file_path = os.path.join(directory, class_file)
            if os.path.exists(file_path):
                logging.info(f"Found file: {file_path}")
                if class_file in [
                    'android/inputmethodservice/InputMethodServiceInjector.smali',
                    'android/view/DisplayInfoInjector$2.smali',
                    'miui/util/HapticFeedbackUtil.smali'
                ]:
                    replace_string_in_file(file_path, search_string, replace_string)
            else:
                logging.warning(f"File not found: {file_path}")


if __name__ == "__main__":
    directories = ["miui_framework_classes"]
    modify_smali_files(directories)
