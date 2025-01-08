import os
import re
import logging
import shutil
import sys
import utils

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
defaultcore = sys.argv[1].lower() == 'true'
core = sys.argv[2].lower() == 'true'

def modify_package_parser(file_path):
    logging.info(f"Modifying PackageParser file: {file_path}")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    pattern = re.compile(
        r'invoke-static \{v2, v0, v1\}, Landroid/util/apk/ApkSignatureVerifier;->unsafeGetCertsWithoutVerification\(Landroid/content/pm/parsing/result/ParseInput;Ljava/lang/String;I\)Landroid/content/pm/parsing/result/ParseResult;')

    for line in lines:
        if pattern.search(line):
            logging.info(f"Found target line. Adding line above it.")
            modified_lines.append("    const/4 v1, 0x1\n")
        modified_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
    logging.info(f"Completed modification for file: {file_path}")

def modify_is_error(file_path):
    logging.info(f"Modifying file: {file_path}")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    invoke_pattern = r'invoke-interface \{v0\}, Landroid/content/pm/parsing/result/ParseResult;->isError\(\)Z'
    move_result_pattern = r'\s*move-result\s+(v\d+)'
    modified_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]
        modified_lines.append(line)

        if re.search(invoke_pattern, line):
            j = i + 1

            while j < len(lines) and lines[j].strip() == "":
                modified_lines.append(lines[j])
                j += 1

            if j < len(lines):
                move_result_match = re.match(move_result_pattern, lines[j])
                if move_result_match:
                    modified_lines.append(lines[j])
                    register = move_result_match.group(1)
                    modified_lines.append(f"    const/4 {register}, 0x0\n")
                    i = j

        i += 1

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

    logging.info(f"Completed modification for file: {file_path}")

def modify_exception_file(file_path):
    logging.info(f"Modifying exception file: {file_path}")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if re.search(r'iput p1, p0, Landroid/content/pm/PackageParser\$PackageParserException;->error:I', line):
            logging.info(f"Adding line above 'iput' in {file_path}")
            modified_lines.append("    const/4 p1, 0x0\n")
        modified_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
    logging.info(f"Completed modification for file: {file_path}")

def modify_apk_signature_verifier(file_path, scheme_version):
    logging.info(f"Modifying ApkSignatureVerifier file for scheme {scheme_version}: {file_path}")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []

    if scheme_version == 'v1':
        pattern = re.compile(
            r'invoke-static \{p0, p1, p3\}, Landroid/util/apk/ApkSignatureVerifier;->verifyV1Signature\(Landroid/content/pm/parsing/result/ParseInput;Ljava/lang/String;Z\)Landroid/content/pm/parsing/result/ParseResult;')
    elif scheme_version == 'v2':
        pattern = re.compile(
            r'invoke-static \{p0, p1, p3\}, Landroid/util/apk/ApkSignatureVerifier;->verifyV2Signature\(Landroid/content/pm/parsing/result/ParseInput;Ljava/lang/String;Z\)Landroid/content/pm/parsing/result/ParseResult;')
    elif scheme_version == 'v3':
        pattern = re.compile(
            r'invoke-static \{p0, p1, p3\}, Landroid/util/apk/ApkSignatureVerifier;->verifyV3Signature\(Landroid/content/pm/parsing/result/ParseInput;Ljava/lang/String;Z\)Landroid/content/pm/parsing/result/ParseResult;')
    elif scheme_version == 'v3_and_below':
        pattern = re.compile(
            r'invoke-static \{p0, p1, p3\}, Landroid/util/apk/ApkSignatureVerifier;->verifyV3AndBelowSignatures\(Landroid/content/pm/parsing/result/ParseInput;Ljava/lang/String;Z\)Landroid/content/pm/parsing/result/ParseResult;')
    else:
        raise ValueError(f"Unsupported scheme version: {scheme_version}")

    for line in lines:
        if pattern.search(line):
            logging.info(f"Found target line for scheme {scheme_version}. Adding line above it.")
            modified_lines.append("    const/4 p3, 0x0\n")
        modified_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
    logging.info(f"Completed modification for file: {file_path}")


def modify_invoke_static(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        modified_lines.append(line)
        if 'Ljava/security/MessageDigest;->isEqual([B[B)Z' in line:
            for j in range(i + 1, min(i + 4, len(lines))):
                if re.match(r'\s*move-result\s+(v\d+)', lines[j]):
                    variable = re.search(r'\s*move-result\s+(v\d+)', lines[j]).group(1)
                    logging.info(f"Replacing line: {lines[j].strip()} with const/4 {variable}, 0x1")
                    modified_lines[-1] = line
                    modified_lines.append(f"    const/4 {variable}, 0x1\n")
                    i = j
                    break
        i += 1

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
    logging.info(f"Completed modification for file: {file_path}")


def modify_strict_jar_file(file_path):
    logging.info(f"Processing file: {file_path}")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    i = 0

    invoke_virtual_pattern = re.compile(
        r'invoke-virtual \{p0, v5\}, Landroid/util/jar/StrictJarFile;->findEntry\(Ljava/lang/String;\)Ljava/util/zip/ZipEntry;')
    if_eqz_pattern = re.compile(r'if-eqz v\d+, :cond_\w+')
    label_pattern = re.compile(r':cond_\w+')

    while i < len(lines):
        line = lines[i]

        if invoke_virtual_pattern.search(line):
            modified_lines.append(line)
            i += 1

            while i < len(lines):
                next_line = lines[i]

                if if_eqz_pattern.search(next_line):
                    logging.info(f"Removing line: {next_line.strip()}")
                    i += 1

                    while i < len(lines):
                        next_line = lines[i]
                        if label_pattern.search(next_line):
                            logging.info(f"Removing line: {next_line.strip()}")
                            i += 1
                            break
                        else:
                            modified_lines.append(next_line)
                        i += 1
                    break

                modified_lines.append(next_line)
                i += 1

        else:
            modified_lines.append(line)
            i += 1

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

    logging.info(f"Modification completed for file: {file_path}")

def modify_smali_files(directories):
    for directory in directories:
        logging.info(f"Scanning directory: {directory}")
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".smali"):
                    filepath = os.path.join(root, file)
                    utils.patch(filepath)
        signing_details = os.path.join(directory, 'android/content/pm/SigningDetails.smali')
        package_parser_signing_details = os.path.join(directory,
                                                      'android/content/pm/PackageParser$SigningDetails.smali')
        apk_signature_verifier = os.path.join(directory, 'android/util/apk/ApkSignatureVerifier.smali')
        apk_signature_scheme_v2_verifier = os.path.join(directory, 'android/util/apk/ApkSignatureSchemeV2Verifier.smali')
        apk_signature_scheme_v3_verifier = os.path.join(directory, 'android/util/apk/ApkSignatureSchemeV3Verifier.smali')
        Apk_Signing_Block_Utils = os.path.join(directory, 'android/util/apk/ApkSigningBlockUtils.smali')
        package_parser = os.path.join(directory, 'android/content/pm/PackageParser.smali')
        package_parser_exception = os.path.join(directory,
                                                'android/content/pm/PackageParser$PackageParserException.smali')
        Strict_Jar_Verifier = os.path.join(directory,'android/util/jar/StrictJarVerifier.smali')
        strict_jar_file = os.path.join(directory, 'android/util/jar/StrictJarFile.smali')
        application_info = os.path.join(directory, 'android/content/pm/ApplicationInfo.smali')
        if defaultcore:
            if os.path.exists(signing_details):
                logging.info(f"Found file: {signing_details}")
                utils.modify_file(signing_details, "framework")
            else:
                logging.warning(f"File not found: {signing_details}")
            if os.path.exists(package_parser_signing_details):
                logging.info(f"Found file: {package_parser_signing_details}")
                utils.modify_file(package_parser_signing_details, "framework")
            else:
                logging.warning(f"File not found: {package_parser_signing_details}")
            if os.path.exists(application_info):
                logging.info(f"Found file: {application_info}")
                utils.modify_file(application_info, "framework")
        if core and defaultcore:
            if os.path.exists(apk_signature_scheme_v2_verifier):
                logging.info(f"Found file: {apk_signature_scheme_v2_verifier}")
                modify_invoke_static(apk_signature_scheme_v2_verifier)
            else:
                logging.warning(f"File not found: {apk_signature_scheme_v2_verifier}")
            if os.path.exists(apk_signature_scheme_v3_verifier):
                logging.info(f"Found file: {apk_signature_scheme_v3_verifier}")
                modify_invoke_static(apk_signature_scheme_v3_verifier)
            else:
                logging.warning(f"File not found: {apk_signature_scheme_v3_verifier}")
            if os.path.exists(apk_signature_verifier):
                logging.info(f"Found file: {apk_signature_verifier}")
                modify_apk_signature_verifier(apk_signature_verifier, 'v1')
                modify_apk_signature_verifier(apk_signature_verifier, 'v2')
                modify_apk_signature_verifier(apk_signature_verifier, 'v3')
                modify_apk_signature_verifier(apk_signature_verifier, 'v3_and_below')
                modify_is_error(apk_signature_verifier)
                utils.modify_file(apk_signature_verifier, "framework")
            else:
                logging.warning(f"File not found: {apk_signature_verifier}")
            if os.path.exists(Strict_Jar_Verifier):
                logging.info(f"Found file: {Strict_Jar_Verifier}")
                utils.modify_file(Strict_Jar_Verifier, "framework")
            else:
                logging.warning(f"File not found: {Strict_Jar_Verifier}")
            if os.path.exists(Apk_Signing_Block_Utils):
                modify_invoke_static(Apk_Signing_Block_Utils)
            if os.path.exists(package_parser):
                logging.info(f"Found file: {package_parser}")
                modify_package_parser(package_parser)
            else:
                logging.warning(f"File not found: {package_parser}")
            if os.path.exists(package_parser_exception):
                logging.info(f"Found file: {package_parser_exception}")
                modify_exception_file(package_parser_exception)
            else:
                logging.warning(f"File not found: {package_parser_exception}")
            if os.path.exists(strict_jar_file):
                logging.info(f"Found file: {strict_jar_file}")
                modify_strict_jar_file(strict_jar_file)
            else:
                logging.warning(f"File not found: {strict_jar_file}")


if __name__ == "__main__":
    directories = ["classes", "classes2", "classes3", "classes4", "classes5"]
    modify_smali_files(directories)