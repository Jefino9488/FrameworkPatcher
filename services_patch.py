import os
import re
import logging
import sys
import utils

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def modify_smali_files(directories):
    for directory in directories:
        logging.info(f"Scanning directory: {directory}")
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".smali"):
                    filepath = os.path.join(root, file)
                    utils.patch(filepath)
        install_package_helper = os.path.join(directory, 'com/android/server/pm/InstallPackageHelper.smali')
        verification_params = os.path.join(directory, 'com/android/server/pm/VerificationParams.smali')
        device_policy_cache_impl = os.path.join(directory, 'com/android/server/devicepolicy/DevicePolicyCacheImpl.smali')
        device_policy_manager_service = os.path.join(directory, 'com/android/server/devicepolicy/DevicePolicyManagerService.smali')
        window_state = os.path.join(directory, 'com/android/server/wm/WindowState.smali')
        window_surface_controller = os.path.join(directory, 'com/android/server/wm/WindowSurfaceController.smali')
        package_manager_service_utils = os.path.join(directory, 'com/android/server/pm/PackageManagerServiceUtils.smali')
        if os.path.exists(package_manager_service_utils):
            logging.info(f"Found file: {package_manager_service_utils}")
            utils.modify_file(package_manager_service_utils)
        else:
            logging.warning(f"File not found: {package_manager_service_utils}")

        if os.path.exists(install_package_helper):
            logging.info(f"Found file: {install_package_helper}")
            utils.modify_file(install_package_helper)
        else:
            logging.warning(f"File not found: {install_package_helper}")

        if os.path.exists(verification_params):
            logging.info(f"Found file: {verification_params}")
            utils.modify_file(verification_params)
        else:
            logging.warning(f"File not found: {verification_params}")

        if os.path.exists(window_state):
            logging.info(f"Found file: {window_state}")
            utils.modify_file(window_state)
        else:
            logging.warning(f"File not found: {window_state}")

        if os.path.exists(window_surface_controller):
            logging.info(f"Found file: {window_surface_controller}")
            utils.modify_file(window_surface_controller)
        else:
            logging.warning(f"File not found: {window_surface_controller}")

        if os.path.exists(device_policy_manager_service):
            logging.info(f"Found file: {device_policy_manager_service}")
            utils.modify_file(device_policy_manager_service)
        else:
            logging.warning(f"File not found: {device_policy_manager_service}")

        if os.path.exists(device_policy_cache_impl):
            logging.info(f"Found file: {device_policy_cache_impl}")
            utils.modify_file(device_policy_cache_impl)
        else:
            logging.warning(f"File not found: {device_policy_cache_impl}")

if __name__ == "__main__":
    directories = ["services_classes", "services_classes2", "services_classes3", "services_classes4", "services_classes5"]
    logging.info("Starting smali modification process...")
    modify_smali_files(directories)
    logging.info("Smali modification process completed.")
