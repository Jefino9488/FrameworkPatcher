import os
import re
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def modify_file(file_path):
    logging.info(f"Modifying file: {file_path}")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    pattern = re.compile(r'invoke-static \{v2, v0, v1\}, Landroid/util/apk/ApkSignatureVerifier;->unsafeGetCertsWithoutVerification\(Landroid/content/pm/parsing/result/ParseInput;Ljava/lang/String;I\)Landroid/content/pm/parsing/result/ParseResult;')

    for line in lines:
        if pattern.search(line):
            logging.info(f"Found target line. Adding line above it.")
            modified_lines.append("    const/4 v1, 0x1\n")
        modified_lines.append(line)

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

def modify_apk_signature_scheme_v2_verifier(file_path):
    logging.info(f"Modifying ApkSignatureSchemeV2Verifier file: {file_path}")
    modify_invoke_static(file_path)

def modify_apk_signature_scheme_v3_verifier(file_path):
    logging.info(f"Modifying ApkSignatureSchemeV3Verifier file: {file_path}")
    modify_invoke_static(file_path)

def modify_apk_signing_block_utils(file_path):
    logging.info(f"Modifying ApkSigningBlockUtils file: {file_path}")
    modify_invoke_static(file_path)

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
                    modified_lines[-1] = line  # Restore the original line
                    modified_lines.append(f"    const/4 {variable}, 0x1\n")
                    i = j  # Skip the move-result line
                    break
        i += 1

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
    logging.info(f"Completed modification for file: {file_path}")

def modify_smali_files(directories):
    for directory in directories:
        signing_details = os.path.join(directory, 'android/content/pm/SigningDetails.smali')
        package_parser_signing_details = os.path.join(directory, 'android/content/pm/PackageParser$SigningDetails.smali')
        apk_signature_verifier = os.path.join(directory, 'android/util/apk/ApkSignatureVerifier.smali')
        apk_signature_scheme_v2_verifier = os.path.join(directory, 'android/util/apk/ApkSignatureSchemeV2Verifier.smali')
        apk_signature_scheme_v3_verifier = os.path.join(directory, 'android/util/apk/ApkSignatureSchemeV3Verifier.smali')
        apk_signing_block_utils = os.path.join(directory, 'android/util/apk/ApkSigningBlockUtils.smali')
        package_parser = os.path.join(directory, 'android/content/pm/PackageParser.smali')
        package_parser_exception = os.path.join(directory, 'android/content/pm/PackageParser$PackageParserException.smali')

        if os.path.exists(signing_details):
            logging.info(f"Found file: {signing_details}")
            modify_file(signing_details)
        else:
            logging.warning(f"File not found: {signing_details}")
        if os.path.exists(package_parser_signing_details):
            logging.info(f"Found file: {package_parser_signing_details}")
            modify_file(package_parser_signing_details)
        else:
            logging.warning(f"File not found: {package_parser_signing_details}")
        if os.path.exists(apk_signature_verifier):
            logging.info(f"Found file: {apk_signature_verifier}")
            modify_file(apk_signature_verifier)
        else:
            logging.warning(f"File not found: {apk_signature_verifier}")
        if os.path.exists(apk_signature_scheme_v2_verifier):
            logging.info(f"Found file: {apk_signature_scheme_v2_verifier}")
            modify_apk_signature_scheme_v2_verifier(apk_signature_scheme_v2_verifier)
        else:
            logging.warning(f"File not found: {apk_signature_scheme_v2_verifier}")
        if os.path.exists(apk_signature_scheme_v3_verifier):
            logging.info(f"Found file: {apk_signature_scheme_v3_verifier}")
            modify_apk_signature_scheme_v3_verifier(apk_signature_scheme_v3_verifier)
        else:
            logging.warning(f"File not found: {apk_signature_scheme_v3_verifier}")
        if os.path.exists(apk_signing_block_utils):
            logging.info(f"Found file: {apk_signing_block_utils}")
            modify_apk_signing_block_utils(apk_signing_block_utils)
        else:
            logging.warning(f"File not found: {apk_signing_block_utils}")
        if os.path.exists(package_parser):
            logging.info(f"Found file: {package_parser}")
            modify_file(package_parser)
        else:
            logging.warning(f"File not found: {package_parser}")
        if os.path.exists(package_parser_exception):
            logging.info(f"Found file: {package_parser_exception}")
            modify_exception_file(package_parser_exception)
        else:
            logging.warning(f"File not found: {package_parser_exception}")

if __name__ == "__main__":
    directories = ["classes", "classes2", "classes3", "classes4"]
    modify_smali_files(directories)
