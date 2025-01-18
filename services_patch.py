import os
import logging
import re
import sys
import utils

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
defaultcore = sys.argv[1].lower() == 'true'
disable_flag_secure = sys.argv[2].lower() == 'true'

def modify_install_package_helper(file_path):
    logging.info(f"Modifying preparePackageLI in {file_path}")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    in_method = False
    const_string_index = None
    target_register = None
    last_if_eqz_index = None

    for i, line in enumerate(lines):
        if re.match(r'\.method.*preparePackageLI\(.*\)', line) and "private" in line:
            logging.info("Found the method: preparePackageLI.")
            in_method = True

        if in_method:
            if re.search(r'invoke-interface \{v7\}, Lcom/android/server/pm/pkg/AndroidPackage;->isLeavingSharedUser\(\)Z', line):
                logging.info(f"Found invoke-interface at line {i + 1}: {line.strip()}")
                const_string_index = i
                break

            if "if-eqz" in line:
                last_if_eqz_index = i
                match = re.search(r'if-eqz (\w+),', line)
                if match:
                    target_register = match.group(1)

    if last_if_eqz_index is not None and const_string_index is not None and last_if_eqz_index < const_string_index:
        logging.info(f"Modifying 'if-eqz' at line {last_if_eqz_index + 1}: {lines[last_if_eqz_index].strip()}")
        modified_lines = (
            lines[:last_if_eqz_index]
            + [f"    const/4 {target_register}, 0x1\n"]
            + lines[last_if_eqz_index:]
        )
    else:
        logging.warning("Failed to find a valid 'if-eqz' before the const-string.")
        modified_lines = lines

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
    logging.info(f"Completed modification for preparePackageLI in {file_path}")

def modify_smali_files(directories):
    for directory in directories:
        logging.info(f"Scanning directory: {directory}")
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".smali"):
                    filepath = os.path.join(root, file)
                    utils.patch(filepath)
        # a14
        package_manager_service_utils = os.path.join(directory, 'com/android/server/pm/PackageManagerServiceUtils.smali') #14,15 common
        install_package_helper = os.path.join(directory, 'com/android/server/pm/InstallPackageHelper.smali')
        #a15
        Key_Set_Manager_Service = os.path.join(directory, 'com/android/server/pm/KeySetManagerService.smali')
        #...
        verification_params = os.path.join(directory, 'com/android/server/pm/VerificationParams.smali')
        device_policy_cache_impl = os.path.join(directory, 'com/android/server/devicepolicy/DevicePolicyCacheImpl.smali')
        device_policy_manager_service = os.path.join(directory, 'com/android/server/devicepolicy/DevicePolicyManagerService.smali')
        window_state = os.path.join(directory, 'com/android/server/wm/WindowState.smali')
        window_surface_controller = os.path.join(directory, 'com/android/server/wm/WindowSurfaceController.smali')
        if defaultcore:
            if os.path.exists(package_manager_service_utils):
                logging.info(f"Found file: {package_manager_service_utils}")
                utils.modify_file(package_manager_service_utils, "services")
            else:
                logging.warning(f"File not found: {package_manager_service_utils}")

            if os.path.exists(install_package_helper):
                logging.info(f"Found file: {install_package_helper}")
                modify_install_package_helper(install_package_helper)
                utils.modify_file(install_package_helper, "services")
            else:
                logging.warning(f"File not found: {install_package_helper}")
            if os.path.exists(Key_Set_Manager_Service):
                logging.info(f"Found file: {Key_Set_Manager_Service}")
                utils.modify_file(Key_Set_Manager_Service, "services")
            else:
                logging.warning(f"File not found: {Key_Set_Manager_Service}")
        if disable_flag_secure:
            if os.path.exists(verification_params):
                logging.info(f"Found file: {verification_params}")
                utils.modify_file(verification_params, "services")
            else:
                logging.warning(f"File not found: {verification_params}")

            if os.path.exists(window_state):
                logging.info(f"Found file: {window_state}")
                utils.modify_file(window_state, "services")
            else:
                logging.warning(f"File not found: {window_state}")

            if os.path.exists(window_surface_controller):
                logging.info(f"Found file: {window_surface_controller}")
                utils.modify_file(window_surface_controller, "services")
            else:
                logging.warning(f"File not found: {window_surface_controller}")

            if os.path.exists(device_policy_manager_service) :
                logging.info(f"Found file: {device_policy_manager_service}")
                utils.modify_file(device_policy_manager_service, "services")
            else:
                logging.warning(f"File not found: {device_policy_manager_service}")

            if os.path.exists(device_policy_cache_impl):
                logging.info(f"Found file: {device_policy_cache_impl}")
                utils.modify_file(device_policy_cache_impl, "services")
            else:
                logging.warning(f"File not found: {device_policy_cache_impl}")

if __name__ == "__main__":
    directories = ["services_classes", "services_classes2", "services_classes3", "services_classes4", "services_classes5"]
    logging.info("Starting smali modification process...")
    modify_smali_files(directories)
    logging.info("Smali modification process completed.")
