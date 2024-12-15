import logging
import re


def patch(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    if not any('invoke-custom' in line for line in lines):
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
                        modified_lines.append("     const/4 v0, 0x0\n")
                        modified_lines.append("    return-object v0\n")
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
    original_registers_line = ""

    method_patterns = {
        "checkCapability": re.compile(r'\.method.*checkCapability\(.*\)Z'),
        "checkCapabilityRecover": re.compile(r'\.method.*checkCapabilityRecover\(.*\)Z'),
        "hasAncestorOrSelf": re.compile(r'\.method.*hasAncestorOrSelf\(.*\)Z'),
        "getMinimumSignatureSchemeVersionForTargetSdk": re.compile(r'\.method.*getMinimumSignatureSchemeVersionForTargetSdk\(I\)I'),
        "isPackageWhitelistedForHiddenApis": re.compile(r'\.method.*isPackageWhitelistedForHiddenApis\(.*\)Z'),
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
            if line.strip().startswith('.registers'):
                original_registers_line = line
                continue

            if line.strip() == '.end method':
                modified_lines.append(method_start_line)
                if method_type in [
                    "checkCapability", "checkCapabilityRecover", "hasAncestorOrSelf",
                    "getMinimumSignatureSchemeVersionForTargetSdk", "isPackageWhitelistedForHiddenApis",
                    "matchSignatureInSystem", "matchSignaturesCompat", "matchSignaturesRecover",
                    "canSkipForcedPackageVerification", "checkDowngrade", "compareSignatures",
                    "isApkVerityEnabled", "isDowngradePermitted", "verifySignatures",
                    "isVerificationEnabled", "doesSignatureMatchForPermissions", "isScreenCaptureAllowed",
                    "getScreenCaptureDisabled", "setScreenCaptureDisabled", "isSecureLocked",
                    "setSecure", "shouldCheckUpgradeKeySetLocked"
                ]:
                    logging.info(f"Modifying method body for {method_type}")

                    if method_type == "checkCapability":
                        modified_lines.append(original_registers_line)
                        modified_lines.append("    const/4 v0, 0x1\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "checkCapabilityRecover":
                        modified_lines.append(original_registers_line)
                        modified_lines.append("    .annotation system Ldalvik/annotation/Throws;\n")
                        modified_lines.append("        value = {\n")
                        modified_lines.append("            Ljava/security/cert/CertificateException;\n")
                        modified_lines.append("        }\n")
                        modified_lines.append("    .end annotation\n")
                        modified_lines.append("    const/4 v0, 0x1\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "hasAncestorOrSelf":
                        modified_lines.append(original_registers_line)
                        modified_lines.append("    const/4 v0, 0x1\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "getMinimumSignatureSchemeVersionForTargetSdk":
                        modified_lines.append(original_registers_line)
                        modified_lines.append("    const/4 v0, 0x0\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "isPackageWhitelistedForHiddenApis":
                        modified_lines.append(original_registers_line)
                        modified_lines.append("    const/4 v0, 0x1\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "matchSignatureInSystem":
                        modified_lines.append("    .registers 3\n")
                        modified_lines.append("    const/4 p0, 0x0\n")
                        modified_lines.append("    return p0\n")
                    elif method_type == "matchSignaturesCompat":
                        modified_lines.append("    .registers 5\n")
                        modified_lines.append("    const/4 v0, 0x0\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "matchSignaturesRecover":
                        modified_lines.append("    .registers 5\n")
                        modified_lines.append("    const/4 v0, 0x0\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "canSkipForcedPackageVerification":
                        modified_lines.append("    .registers 3\n")
                        modified_lines.append("    const/4 v0, 0x1\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "checkDowngrade":
                        modified_lines.append("    .registers 2\n")
                        modified_lines.append("    .annotation system Ldalvik/annotation/Throws;\n")
                        modified_lines.append("        value = {\n")
                        modified_lines.append("            Lcom/android/server/pm/PackageManagerException;\n")
                        modified_lines.append("        }\n")
                        modified_lines.append("    .end annotation\n")
                        modified_lines.append("    return-void\n")
                    elif method_type == "compareSignatures":
                        modified_lines.append("    .registers 3\n")
                        modified_lines.append("    const/4 v0, 0x0\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "isApkVerityEnabled":
                        modified_lines.append("    .registers 1\n")
                        modified_lines.append("    const/4 v0, 0x0\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "isDowngradePermitted":
                        modified_lines.append("    .registers 3\n")
                        modified_lines.append("    const/4 v0, 0x1\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "verifySignatures":
                        modified_lines.append("    .registers 21\n")
                        modified_lines.append("    .annotation system Ldalvik/annotation/Throws;\n")
                        modified_lines.append("        value = {\n")
                        modified_lines.append("            Lcom/android/server/pm/PackageManagerException;\n")
                        modified_lines.append("        }\n")
                        modified_lines.append("    .end annotation\n")
                        modified_lines.append("    const/4 v1, 0x0\n")
                        modified_lines.append("    return v1\n")
                    elif method_type == "isVerificationEnabled":
                        modified_lines.append("    .registers 4\n")
                        modified_lines.append("    const/4 v0, 0x0\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "doesSignatureMatchForPermissions":
                        modified_lines.append("    .registers 11\n")
                        modified_lines.append("    const/4 v0, 0x1\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "isScreenCaptureAllowed":
                        modified_lines.append("    .registers 4\n")
                        modified_lines.append("    const/4 v0, 0x1\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "getScreenCaptureDisabled":
                        modified_lines.append("    .registers 5\n")
                        modified_lines.append("    const/4 v0, 0x1\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "setScreenCaptureDisabled":
                        modified_lines.append("    .registers 6\n")
                        modified_lines.append("    return-void\n")
                    elif method_type == "isSecureLocked":
                        modified_lines.append("    .registers 6\n")
                        modified_lines.append("    const/4 v0, 0x0\n")
                        modified_lines.append("    return v0\n")
                    elif method_type == "setSecure":
                        modified_lines.append("    .registers 14\n")
                        modified_lines.append("    return-void\n")
                    elif method_type == "shouldCheckUpgradeKeySetLocked":
                        modified_lines.append("    .registers 3\n")
                        modified_lines.append("    const/4 v0, 0x0\n")
                        modified_lines.append("    return v0\n")

                in_method = False
                method_type = None
                original_registers_line = ""
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
