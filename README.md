# Framework`Patcher`
[![Modify Frameworks](https://github.com/Jefino9488/FrameworkPatcher/actions/workflows/patcher.yml/badge.svg)](https://github.com/Jefino9488/FrameworkPatcher/actions/workflows/patcher.yml) [![Website Deployment](https://github.com/Jefino9488/FrameworkPatcher/actions/workflows/deploy.yml/badge.svg)](https://github.com/Jefino9488/FrameworkPatcher/actions/workflows/deploy.yml)
## Description

This framework patcher patches miui/hyper frameworks 

 - `framework.jar`, `services.jar`, `miui-framework.jar`, `miui-services.jar `

Refer to the usage section to know how to use this patcher

## Supported Devices

 - All Xiaomi Devices
 - Only A14 - A15 devices are supported
 - use stock framework files `(modified files are not supported)`
 - recommended to use on CN Hyper OS

## Usage

- Visit the [Website of FrameworkPatcher](https://jefino9488.github.io/FrameworkPatcher/)  
- Provide the required direct URLs of the files.  
- Google Drive links are not supported.  
- Use [Android dumps](https://dumps.tadiphone.dev/dumps) URLs to get versionized zips.  
- Enter the device name and ROM version correctly.  
- Click on the **Build** button.  
- Navigate to the workflow to see the progress.  
- If the build is successful, download the patched files from the release section.

Alternatively, after cloning the repository, you can use the `LocalPatch.sh` script for local patching.  
**Ensure all required JAR files (e.g., `framework.jar`, `services.jar`, etc.) are placed in the directory before running the script.**

## Features

 - China Notification Fix
 - Fully Disabled signature verification (core patch)
 - disable secure flag
 - Add dex2oat compile

## Contributing

`FrameworkPatcher` is an open source project and your contribution is very much appreciated.
1. Fork the project
2. Create your feature branch (git checkout -b feature/featureName)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin feature/featureName)
5. Create a new Pull Request
6. Wait for the review
7. If the review is successful, the changes will be merged

## Credits

- [Xiaomi](https://xiaomi.com)
- [google](https://google.com)
- [CorePatch](https://github.com/LSPosed/CorePatch)
- and many more
