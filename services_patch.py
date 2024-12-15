import os
import re
import shutil
import logging
import sys
isCN = sys.argv[2].lower() == 'true'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def prepatch(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    if not any('invoke-custom' in line for line in lines):
        logging.info(f"No invoke-custom found in file: {filepath}. Skipping modification.")
        return

    modified_lines = []
    in_method = False
    method_type = None
    method_patterns = {
        "equals": re.compile(r'\.method.*equals\(Ljava/lang/Object;\)Z'),
        "hashCode": re.compile(r'\.method.*hashCode\(\)I'),
        "toString": re.compile(r'\.method.*toString\(\)Ljava/lang/String;')
    }
    registers_line = ""

    for line in lines:
        if in_method:
            if line.strip().startswith('.registers'):
                registers_line = line
                continue

            if line.strip() == '.end method':
                if method_type in method_patterns:
                    logging.info(f"Clearing method body for {method_type}")
                    modified_lines.append(registers_line)
                    if method_type == "hashCode":
                        modified_lines.append("    const/4 v0, 0x0\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "equals":
                        modified_lines.append("    const/4 v0, 0x0\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "toString":
                        modified_lines.append("    const/4 v0, 0x0\n")
                        modified_lines.append("    return v0\n")
                in_method = False
                method_type = None
                registers_line = ""
            else:
                continue

        for key, pattern in method_patterns.items():
            if pattern.search(line):
                logging.info(f"Found method {key}. Clearing method content.")
                in_method = True
                method_type = key
                modified_lines.append(line)  # Add method declaration to output
                break

        if not in_method:
            modified_lines.append(line)

    with open(filepath, 'w') as file:
        file.writelines(modified_lines)
    logging.info(f"Completed modification for file: {filepath}")

def modify_file(file_path):
    logging.info(f"Modifying file: {file_path}")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    in_method = False
    method_type = None
    method_start_line = ""

    method_patterns = {
        "matchSignatureInSystem": re.compile(r'\.method.*matchSignatureInSystem\(.*\)Z'),
        "matchSignaturesCompat": re.compile(r'\.method.*matchSignaturesCompat\(.*\)Z'),
        "matchSignaturesRecover": re.compile(r'\.method.*matchSignaturesRecover\(.*\)Z'),
        "canSkipForcedPackageVerification": re.compile(r'\.method.*canSkipForcedPackageVerification\(.*\)Z'),
        "checkDowngrade": re.compile(r'\.method.*checkDowngrade\(.*\)V'),
        "compareSignatures": re.compile(r'\.method.*compareSignatures\(.*\)I'),
        "isApkVerityEnabled": re.compile(r'\.method.*isApkVerityEnabled\(.*\)Z'),
        "isDowngradePermitted": re.compile(r'\.method.*isDowngradePermitted\(.*\)Z'),
        "verifySignatures": re.compile(r'\.method.*verifySignatures\(.*\)Z'),
        "isVerificationEnabled": re.compile(r'\.method.*isVerificationEnabled\(.*\)Z'),
        "doesSignatureMatchForPermissions": re.compile(r'\.method.*doesSignatureMatchForPermissions\(.*\)Z'),
        "isScreenCaptureAllowed": re.compile(r'\.method.*isScreenCaptureAllowed\(.*\)Z'),
        "getScreenCaptureDisabled": re.compile(r'\.method.*getScreenCaptureDisabled\(.*\)Z'),
        "setScreenCaptureDisabled": re.compile(r'\.method.*setScreenCaptureDisabled\(.*\)V'),
        "isSecureLocked": re.compile(r'\.method.*isSecureLocked\(.*\)Z'),
        "setSecure": re.compile(r'\.method.*setSecure\(.*\)V'),
        "shouldCheckUpgradeKeySetLocked": re.compile(r'\.method.*shouldCheckUpgradeKeySetLocked\(.*\)Z')
    }

    for line in lines:
        if in_method:
            if line.strip() == '.end method':
                modified_lines.append(method_start_line)
                if method_type == "matchSignatureInSystem":
                    logging.info(f"Modifying method body for {method_type}")
                    modified_lines.append("    .registers 3\n")
                    modified_lines.append("    const/4 p0, 0x0\n")
                    modified_lines.append("    return p0\n")
                elif method_type == "matchSignaturesCompat":
                    logging.info(f"Modifying method body for {method_type}")
                    modified_lines.append("    .registers 5\n")
                    modified_lines.append("    const/4 v0, 0x0\n")
                    modified_lines.append("    return v0\n")
                elif method_type == "matchSignaturesRecover":
                    logging.info(f"Modifying method body for {method_type}")
                    modified_lines.append("    .registers 5\n")
                    modified_lines.append("    const/4 v0, 0x0\n")
                    modified_lines.append("    return v0\n")
                elif method_type == "canSkipForcedPackageVerification":
                    logging.info(f"Modifying method body for {method_type}")
                    modified_lines.append("    .registers 3\n")
                    modified_lines.append("    const/4 v0, 0x1\n")
                    modified_lines.append("    return v0\n")
                elif method_type == "checkDowngrade":
                    logging.info(f"Modifying method body for {method_type}")
                    modified_lines.append("    .registers 2\n")
                    modified_lines.append("    .annotation system Ldalvik/annotation/Throws;\n")
                    modified_lines.append("        value = {\n")
                    modified_lines.append("            Lcom/android/server/pm/PackageManagerException;\n")
                    modified_lines.append("        }\n")
                    modified_lines.append("    .end annotation\n")
                    modified_lines.append("    return-void\n")
                elif method_type == "compareSignatures" and isCN:
                    logging.info(f"Modifying method body for {method_type}")
                    modified_lines.append("    .registers 3\n")
                    modified_lines.append("    const/4 v0, 0x0\n")
                    modified_lines.append("    return v0\n")
                elif method_type == "isApkVerityEnabled":
                    logging.info(f"Modifying method body for {method_type}")
                    modified_lines.append("    .registers 1\n")
                    modified_lines.append("    const/4 v0, 0x0\n")
                    modified_lines.append("    return v0\n")
                elif method_type == "isDowngradePermitted":
                    logging.info(f"Modifying method body for {method_type}")
                    modified_lines.append("    .registers 3\n")
                    modified_lines.append("    const/4 v0, 0x1\n")
                    modified_lines.append("    return v0\n")
                elif method_type == "verifySignatures":
                    logging.info(f"Modifying method body for {method_type}")
                    modified_lines.append("    .registers 21\n")
                    modified_lines.append("    .annotation system Ldalvik/annotation/Throws;\n")
                    modified_lines.append("        value = {\n")
                    modified_lines.append("            Lcom/android/server/pm/PackageManagerException;\n")
                    modified_lines.append("        }\n")
                    modified_lines.append("    .end annotation\n")
                    modified_lines.append("    const/4 v1, 0x0\n")
                    modified_lines.append("    return v1\n")
                elif method_type == "isVerificationEnabled":
                    logging.info(f"Modifying method body for {method_type}")
                    modified_lines.append("    .registers 4\n")
                    modified_lines.append("    const/4 v0, 0x0\n")
                    modified_lines.append("    return v0\n")
                elif method_type == "doesSignatureMatchForPermissions":
                    logging.info(f"Modifying method body for {method_type}")
                    modified_lines.append("    .registers 11\n")
                    modified_lines.append("    const/4 v0, 0x1\n")
                    modified_lines.append("    return v0\n")
                elif method_type == "isScreenCaptureAllowed":
                    logging.info(f"Modifying method body for {method_type}")
                    modified_lines.append("    .registers 4\n")
                    modified_lines.append("    const/4 v0, 0x1\n")
                    modified_lines.append("    return v0\n")
                elif method_type == "getScreenCaptureDisabled":
                    logging.info(f"Modifying method body for {method_type}")
                    modified_lines.append("    .registers 5\n")
                    modified_lines.append("    const/4 v0, 0x1\n")
                    modified_lines.append("    return v0\n")
                elif method_type == "setScreenCaptureDisabled":
                    logging.info(f"Modifying method body for {method_type}")
                    modified_lines.append("    .registers 6\n")
                    modified_lines.append("    return-void\n")
                elif method_type == "isSecureLocked":
                    logging.info(f"Modifying method body for {method_type}")
                    modified_lines.append("    .registers 6\n")
                    modified_lines.append("    const/4 v0, 0x0\n")
                    modified_lines.append("    return v0\n")
                elif method_type == "setSecure":
                    logging.info(f"Modifying method body for {method_type}")
                    modified_lines.append("    .registers 14\n")
                    modified_lines.append("    return-void\n")
                elif method_type == "shouldCheckUpgradeKeySetLocked":
                    logging.info(f"Modifying method body for {method_type}")
                    modified_lines.append("    .registers 3\n")
                    modified_lines.append("    const/4 v0, 0x0\n")
                    modified_lines.append("    return v0\n")
                in_method = False
                method_type = None
            else:
                continue

        for key, pattern in method_patterns.items():
            if pattern.search(line):
                in_method = True
                method_type = key
                method_start_line = line
                break

        if not in_method:
            modified_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
    logging.info(f"Completed modification for file: {file_path}")


def modify_smali_files(directories):
    core = sys.argv[1].lower() == 'true'
    for directory in directories:
        package_manager_service_utils = os.path.join(directory,
                                                     'com/android/server/pm/PackageManagerServiceUtils.smali')
        install_package_helper = os.path.join(directory, 'com/android/server/pm/InstallPackageHelper.smali')
        verification_params = os.path.join(directory, 'com/android/server/pm/VerificationParams.smali')
        device_policy_cache_impl = os.path.join(directory, 'com/android/server/devicepolicy/DevicePolicyCacheImpl.smali')
        device_policy_manager_service = os.path.join(directory, 'com/android/server/devicepolicy/DevicePolicyManagerService.smali')
        window_state = os.path.join(directory, 'com/android/server/wm/WindowState.smali')
        window_surface_controller = os.path.join(directory, 'com/android/server/wm/WindowSurfaceController.smali')
        pre_patch1 = os.path.join(directory, 'android/hardware/input/KeyboardLayoutPreviewDrawable$GlyphDrawable.smali')
        pre_patch2 = os.path.join(directory, 'android/hardware/input/PhysicalKeyLayout$EnterKey.smali')
        pre_patch3 = os.path.join(directory, 'android/hardware/input/PhysicalKeyLayout$LayoutKey.smali')
        pre_patch4 = os.path.join(directory, 'android/media/MediaRouter2$InstanceInvalidatedCallbackRecord.smali')
        pre_patch5 = os.path.join(directory, 'android/media/MediaRouter2$PackageNameUserHandlePair.smali')
        pre_patch6 = os.path.join(directory, 'com/android/server/BinaryTransparencyService$Digest.smali')
        pre_patch7 = os.path.join(directory, 'com/android/server/inputmethod/AdditionalSubtypeMapRepository$WriteTask.smali')
        pre_patch8 = os.path.join(directory, 'com/android/server/policy/PhoneWindowManager$SwitchKeyboardLayoutMessageObject.smali')
        pre_patch9 = os.path.join(directory, '')
        if os.path.exists(pre_patch1):
            prepatch(pre_patch1)
        if os.path.exists(pre_patch2):
            prepatch(pre_patch2)
        if os.path.exists(pre_patch3):
            prepatch(pre_patch3)
        if os.path.exists(pre_patch4):
            prepatch(pre_patch4)
        if os.path.exists(pre_patch5):
            prepatch(pre_patch5)
        if os.path.exists(pre_patch6):
            prepatch(pre_patch6)
        if os.path.exists(pre_patch7):
            prepatch(pre_patch7)
        if os.path.exists(pre_patch8):
            prepatch(pre_patch8)
        if os.path.exists(pre_patch9):
            prepatch(pre_patch9)

        if os.path.exists(package_manager_service_utils):
            logging.info(f"Found file: {package_manager_service_utils}")
            modify_file(package_manager_service_utils)
        else:
            logging.warning(f"File not found: {package_manager_service_utils}")

        if os.path.exists(install_package_helper):
            logging.info(f"Found file: {install_package_helper}")
            modify_file(install_package_helper)
        else:
            logging.warning(f"File not found: {install_package_helper}")

        if os.path.exists(verification_params):
            logging.info(f"Found file: {verification_params}")
            modify_file(verification_params)
        else:
            logging.warning(f"File not found: {verification_params}")

        if os.path.exists(window_state):
            logging.info(f"Found file: {window_state}")
            modify_file(window_state)
        else:
            logging.warning(f"File not found: {window_state}")

        if os.path.exists(window_surface_controller):
            logging.info(f"Found file: {window_surface_controller}")
            modify_file(window_surface_controller)
        else:
            logging.warning(f"File not found: {window_surface_controller}")

        if os.path.exists(device_policy_manager_service):
            logging.info(f"Found file: {device_policy_manager_service}")
            modify_file(device_policy_manager_service)
        else:
            logging.warning(f"File not found: {device_policy_manager_service}")

        if os.path.exists(device_policy_cache_impl):
            logging.info(f"Found file: {device_policy_cache_impl}")
            modify_file(device_policy_cache_impl)
        else:
            logging.warning(f"File not found: {device_policy_cache_impl}")

if __name__ == "__main__":
    directories = ["services_classes", "services_classes2", "services_classes3", "services_classes4", "services_classes5"]
    modify_smali_files(directories)