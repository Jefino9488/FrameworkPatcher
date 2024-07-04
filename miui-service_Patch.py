import os
import re
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def modify_file(file_path, search_pattern, add_line_template):
    logging.info(f"Modifying file: {file_path}")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        modified_lines.append(line)
        match = re.search(search_pattern, line)
        if match:
            vX = match.group(1)
            add_line = add_line_template.format(vX=vX)
            logging.info(f"Found pattern in file: {file_path} with variable {vX}")
            modified_lines.append(add_line + '\n')

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
    logging.info(f"Completed modification for file: {file_path}")


def replace_string_in_file(file_path, search_string, replace_string):
    logging.info(f"Replacing string in file: {file_path}")
    with open(file_path, 'r') as file:
        content = file.read()

    modified_content = content.replace(search_string, replace_string)

    with open(file_path, 'w') as file:
        file.write(modified_content)
    logging.info(f"Completed string replacement in file: {file_path}")


def replace_method_body(file_path, method_signature, new_body):
    logging.info(f"Replacing method body in file: {file_path}")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    in_method = False
    for line in lines:
        if in_method:
            if line.strip() == '.end method':
                modified_lines.append(new_body)
                modified_lines.append(line)
                in_method = False
            continue

        if method_signature in line:
            in_method = True
            continue

        modified_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
    logging.info(f"Completed method body replacement in file: {file_path}")


def modify_smali_files(directories):
    classes_to_modify = [
        'com/android/server/AppOpsServiceStubImpl.smali',
        'com/android/server/alarm/AlarmManagerServiceStubImpl.smali',
        'com/android/server/am/BroadcastQueueModernStubImpl.smali',
        'com/android/server/am/ProcessManagerService.smali',
        'com/android/server/am/ProcessSceneCleaner.smali',
        'com/android/server/job/JobServiceContextImpl.smali',
        'com/android/server/notification/NotificationManagerServiceImpl.smali',
        'com/miui/server/greeze/GreezeManagerService.smali',
        'miui/app/ActivitySecurityHelper.smali',
        'com/android/server/am/ActivityManagerServiceImpl.smali',
        'com/android/server/ForceDarkAppListManager.smali',
        'com/android/server/am/ActivityManagerServiceImpl$1.smali',
        'com/android/server/input/InputManagerServiceStubImpl.smali',
        'com/android/server/inputmethod/InputMethodManagerServiceImpl.smali',
        'com/android/server/wm/MiuiSplitInputMethodImpl.smali'
    ]

    search_pattern = r'sget-boolean (v\d+), Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z'
    add_line_template = '    const/4 {vX}, 0x1'

    search_string = "com.baidu.input_mi"
    replace_string = "com.google.android.inputmethod.latin"

    for directory in directories:
        for class_file in classes_to_modify:
            file_path = os.path.join(directory, class_file)
            if os.path.exists(file_path):
                logging.info(f"Found file: {file_path}")
                modify_file(file_path, search_pattern, add_line_template)
                if class_file in [
                    'com/android/server/am/ActivityManagerServiceImpl$1.smali',
                    'com/android/server/input/InputManagerServiceStubImpl.smali',
                    'com/android/server/inputmethod/InputMethodManagerServiceImpl.smali',
                    'com/android/server/wm/MiuiSplitInputMethodImpl.smali'
                ]:
                    replace_string_in_file(file_path, search_string, replace_string)
            else:
                logging.warning(f"File not found: {file_path}")

        # Replace method body for com/android/server/wm/WindowManagerServiceImpl.smali
        wm_service_impl_path = os.path.join(directory, 'com/android/server/wm/WindowManagerServiceImpl.smali')
        if os.path.exists(wm_service_impl_path):
            logging.info(f"Found file: {wm_service_impl_path}")
            method_signature = ".method public notAllowCaptureDisplay(Lcom/android/server/wm/RootWindowContainer;I)Z"
            new_body = """
    .registers 9

    const/4 v0, 0x0

    return v0
.end method
"""
            replace_method_body(wm_service_impl_path, method_signature, new_body)
        else:
            logging.warning(f"File not found: {wm_service_impl_path}")


if __name__ == "__main__":
    directories = ["miui_services_classes"]
    modify_smali_files(directories)
