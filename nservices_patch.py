import os
import re
import shutil
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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
        "canSkipForcedPackageVerification": re.compile(
            r'\.method.*canSkipForcedPackageVerification\(Lcom/android/server/pm/parsing/pkg/AndroidPackage;\)Z'),
        "checkDowngrade": re.compile(
            r'\.method public static checkDowngrade\(Lcom/android/server/pm/parsing/pkg/AndroidPackage;Landroid/content/pm/PackageInfoLite;\)V'),
        "compareSignatures": re.compile(
            r'\.method public static compareSignatures\(\[Landroid/content/pm/Signature;\[Landroid/content/pm/Signature;\)I'),
        "isApkVerityEnabled": re.compile(r'\.method static isApkVerityEnabled\(\)Z'),
        "isDowngradePermitted": re.compile(r'\.method public static isDowngradePermitted\(IZ\)Z'),
        "verifySignatures": re.compile(
            r'\.method public static verifySignatures\(Lcom/android/server/pm/PackageSetting;Lcom/android/server/pm/SharedUserSetting;Lcom/android/server/pm/PackageSetting;Landroid/content/pm/SigningDetails;ZZZ\)Z'),
        "isVerificationEnabled": re.compile(
            r'\.method private isVerificationEnabled\(Landroid/content/pm/PackageInfoLite;I\)Z'),
        "doesSignatureMatchForPermissions": re.compile(
            r'\.method private doesSignatureMatchForPermissions\(Ljava/lang/String;Lcom/android/server/pm/parsing/pkg/ParsedPackage;I\)Z')
    }

    for line in lines:
        if in_method:
            if line.strip() == '.end method':
                # Add method body based on the identified method type
                modified_lines.append(method_start_line)  # Add the .method line
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
                elif method_type == "compareSignatures":
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
                in_method = False
                method_type = None
            else:
                continue

        for key, pattern in method_patterns.items():
            if pattern.search(line):
                in_method = True
                method_type = key
                method_start_line = line  # Save the .method line
                break

        if not in_method:
            modified_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
    logging.info(f"Completed modification for file: {file_path}")


def modify_invoke_interface(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        modified_lines.append(line)
        if 'Lcom/android/server/pm/pkg/AndroidPackage;->isPersistent()Z' in line:
            for j in range(i + 1, min(i + 4, len(lines))):
                if re.match(r'\s*move-result\s+(v\d+)', lines[j]):
                    variable = re.search(r'\s*move-result\s+(v\d+)', lines[j]).group(1)
                    logging.info(f"Replacing line: {lines[j].strip()} with const/4 {variable}, 0x1")
                    modified_lines[-1] = line  # Restore the original line
                    modified_lines.append(f"    const/4 {variable}, 0x0\n")
                    i = j  # Skip the move-result line
                    break
        i += 1

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
    logging.info(f"Completed modification for file: {file_path}")


def modify_parsing_package_utils(file_path):
    logging.info(f"Modifying ParsingPackageUtils file: {file_path}")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if "invoke-static {p0, p1, v0}, Landroid/util/apk/ApkSignatureVerifier;->unsafeGetCertsWithoutVerification(Landroid/content/pm/parsing/result/ParseInput;Ljava/lang/String;I)Landroid/content/pm/parsing/result/ParseResult;" in line:
            logging.info("Found target line in ParsingPackageUtils.smali")
            modified_lines.append("    const/4 v0, 0x1\n")
        modified_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
    logging.info(f"Completed modification for ParsingPackageUtils file: {file_path}")


def copy_and_replace_files(source_dir, target_dirs):
    for target_dir in target_dirs:
        target_policy_dir = os.path.join(target_dir, "com/android/server/policy")
        if os.path.exists(target_policy_dir):
            logging.info(f"Copying files from {source_dir} to {target_policy_dir}")
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    src_file = os.path.join(root, file)
                    dst_file = os.path.join(target_policy_dir, os.path.relpath(src_file, source_dir))
                    dst_dir = os.path.dirname(dst_file)
                    if not os.path.exists(dst_dir):
                        os.makedirs(dst_dir)
                    shutil.copy2(src_file, dst_file)
                    logging.info(f"Copied {src_file} to {dst_file}")
        else:
            logging.warning(f"Target directory does not exist: {target_policy_dir}")


def modify_smali_files(directories):
    for directory in directories:
        # Define paths for services.jar smali files
        package_manager_service_utils = os.path.join(directory,
                                                     'com/android/server/pm/PackageManagerServiceUtils.smali')
        install_package_helper = os.path.join(directory, 'com/android/server/pm/InstallPackageHelper.smali')
        verification_params = os.path.join(directory, 'com/android/server/pm/VerificationParams.smali')
        parsing_package_utils = os.path.join(directory, 'com/android/server/pm/pkg/parsing/ParsingPackageUtils.smali')
        package_info_utils = os.path.join(directory, 'com/android/server/pm/InstallPackageHelper.smali')

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

        if os.path.exists(parsing_package_utils):
            logging.info(f"Found file: {parsing_package_utils}")
            modify_parsing_package_utils(parsing_package_utils)
        else:
            logging.warning(f"File not found: {parsing_package_utils}")
        if os.path.exists(package_info_utils):
            logging.info(f"Found file: {package_info_utils}")
            modify_invoke_interface(package_info_utils)
        else:
            logging.warning(f"File not found: {package_info_utils}")


if __name__ == "__main__":
    directories = ["services_classes", "services_classes2", "services_classes3", "services_classes4"]
