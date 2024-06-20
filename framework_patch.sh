#!/bin/bash

set -e

# Install dependencies
sudo apt update
sudo apt full-upgrade -y
sudo apt install -y default-jdk zipalign p7zip-full wget

# Download framework.jar
wget -O framework.jar "https://dumps.tadiphone.dev/dumps/redmi/xaga/-/raw/missi_phone_cn-user-14-UP1A.231005.007-V816.0.1.0.ULOCNXM-release-keys/system/system/framework/framework.jar"

# Clone smali repository
git clone --depth=1 https://github.com/JesusFreke/smali.git
cd smali
./gradlew build
cp smali/build/libs/smali-all-*.jar ../smali.jar
cp baksmali/build/libs/baksmali-all-*.jar ../baksmali.jar
cd ..

# Extract framework.jar
7z x framework.jar -oframework

# Decompile dex files using baksmali
java -jar baksmali.jar d -a 29 framework/classes.dex -o classes
java -jar baksmali.jar d -a 29 framework/classes2.dex -o classes2
java -jar baksmali.jar d -a 29 framework/classes3.dex -o classes3

# Modify smali files
# Ensure the paths and sed commands match the actual file structure and content
sed -i '/const\/4 v4, 0x0/ a\
invoke-static {v3}, Lcom/android/internal/util/framework/Android;->engineGetCertificateChain([Ljava/security/cert/Certificate;)[Ljava/security/cert/Certificate;\
move-result-object v3' classes/android/security/keystore2/AndroidKeyStoreSpi.smali

# Adjust the paths and context register placeholder
sed -i '/return-object/ i\
invoke-static {p0}, Lcom/android/internal/util/framework/Android;->onNewApp(Landroid/content/Context;)V' classes/android/app/Instrumentation.smali

# Adjust the paths and ensure the sed commands match the actual content
sed -i '/invoke-virtual {p0, p1, v0}, Landroid\/app\/ApplicationPackageManager;->hasSystemFeature(Ljava\/lang\/String;I)Z/ a\
invoke-static {v0, p1}, Lcom/android/internal/util/framework/Android;->hasSystemFeature(ZLjava\/lang\/String;)Z;\
move-result v0' classes/android/app/ApplicationPackageManager.smali

# Recompile dex files using smali
java -jar smali.jar a -a 29 classes -o framework/classes.dex
java -jar smali.jar a -a 29 classes2 -o framework/classes2.dex
java -jar smali.jar a -a 29 classes3 -o framework/classes3.dex

# Repackage framework.jar
7z a -tzip framework.zip framework/*
zipalign -f -p -v -z 4 framework.zip framework.jar
