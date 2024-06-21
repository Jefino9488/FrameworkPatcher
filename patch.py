import os
import re

def modify_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    in_method = False
    method_type = None

    method_patterns = {
        "checkCapability": re.compile(r'\.method public .*checkCapability\(.*\)Z'),
        "checkCapabilityRecover": re.compile(r'\.method public .*checkCapabilityRecover\(.*\)Z'),
        "hasAncestorOrSelf": re.compile(r'\.method public .*hasAncestorOrSelf\(.*\)Z')
    }

    for line in lines:
        if in_method:
            if line.strip() == '.end method':
                # Add method body based on the identified method type
                if method_type == "checkCapability":
                    modified_lines.append("    .registers 4\n")
                elif method_type == "checkCapabilityRecover":
                    modified_lines.append("    .registers 4\n")
                    modified_lines.append("    .annotation system Ldalvik/annotation/Throws;\n")
                    modified_lines.append("        value = {\n")
                    modified_lines.append("            Ljava/security/cert/CertificateException;\n")
                    modified_lines.append("        }\n")
                    modified_lines.append("    .end annotation\n")
                elif method_type == "hasAncestorOrSelf":
                    modified_lines.append("    .registers 6\n")

                modified_lines.append("    const/4 v0, 0x1\n")
                modified_lines.append("    return v0\n")
                modified_lines.append(line)  # Add the .end method line
                in_method = False
                method_type = None
            else:
                continue

        for key, pattern in method_patterns.items():
            if pattern.search(line):
                in_method = True
                method_type = key
                break

        if in_method and line.strip() != ".end method":
            modified_lines.append(line)
        elif not in_method:
            modified_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

def modify_smali_files(directories):
    for directory in directories:
        signing_details = os.path.join(directory, 'android/content/pm/SigningDetails.smali')
        package_parser_signing_details = os.path.join(directory, 'android/content/pm/PackageParser$SigningDetails.smali')

        if os.path.exists(signing_details):
            modify_file(signing_details)
        if os.path.exists(package_parser_signing_details):
            modify_file(package_parser_signing_details)

if __name__ == "__main__":
    directories = ["classes", "classes2", "classes3"]
    modify_smali_files(directories)
