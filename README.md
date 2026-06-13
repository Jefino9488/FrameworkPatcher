# ⚠️ Repository Archived – Moved to FrameworksForge

**This repository has been archived and is no longer maintained here.**  
All future development, issues, and pull requests will happen in the new organization:

👉 **[github.com/FrameworksForge](https://github.com/FrameworksForge)**

Please update your bookmarks and local remotes accordingly.

---

# Framework`Patcher`

[![Modify Frameworks](https://github.com/FrameworksForge/FrameworkPatcher/actions/workflows/patcher.yml/badge.svg)](https://github.com/FrameworksForge/FrameworkPatcher/actions/workflows/patcher.yml)  
[![Website Deployment](https://github.com/FrameworksForge/FrameworkPatcher/actions/workflows/deploy.yml/badge.svg)](https://github.com/FrameworksForge/FrameworkPatcher/actions/workflows/deploy.yml)

## Description

This framework patcher patches MIUI/HyperOS frameworks:

- `framework.jar`
- `services.jar`
- `miui-framework.jar`
- `miui-services.jar`

Refer to the **Usage** section to learn how to use this patcher.

## Supported Devices

- All Xiaomi devices  
- Only Android 14–15 devices are supported  
- Use **stock framework files** (modified files are not supported)  
- Recommended to use on **China HyperOS**

## Usage

- Visit the [FrameworkPatcher Website](https://frameworksforge.github.io/FrameworkPatcher/).  
- Provide the required **direct URLs of the files**, including Google Drive links with "Anyone with the link" download permissions enabled.  
- Ensure that the links are shared properly to allow public access.  
- Enter the device name and ROM version correctly.  
- Click on the **Build** button.  
- Navigate to the workflow to see the progress.  
- If the build is successful, download the patched files from the release section.

Alternatively, after cloning the repository, you can use the `LocalPatch.sh` script for local patching.  
**Ensure all required JAR files (e.g., `framework.jar`, `services.jar`, etc.) are placed in the directory before running the script.**

## Features

- China Notification Fix  
- Fully disabled signature verification (core patch)  
- Disable secure flag  
- Add dex2oat compile

## Contributing

`FrameworkPatcher` is an open source project and your contribution is very much appreciated.  
**Please submit contributions to the new repository:**  
[https://github.com/FrameworksForge/FrameworkPatcher](https://github.com/FrameworksForge/FrameworkPatcher)

1. Fork the project  
2. Create your feature branch (`git checkout -b feature/featureName`)  
3. Commit your changes (`git commit -am 'Add some feature'`)  
4. Push to the branch (`git push origin feature/featureName`)  
5. Create a new Pull Request  
6. Wait for the review  
7. If the review is successful, the changes will be merged

## Credits

- [CorePatch](https://github.com/LSPosed/CorePatch)  
- [Super_Cat07](https://t.me/Super_Cat07) for the original method on A9–A14  
- [Cazymods](https://t.me/not_aric) for contributing the `isPersistent` method  
- [MMETMA](https://t.me/MMETMA2) for resolving bootloop issues on A15 and providing shared UID methods  
- [PappLaci](https://t.me/PappLaci) for fixing Google Play Services issues on A15

---

**Note:** This README now points to the active repository under [FrameworksForge](https://github.com/FrameworksForge). The old repository (`Jefino9488/FrameworkPatcher`) is archived and read-only.
