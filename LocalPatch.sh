7z x framework.jar -oframework
7z x services.jar -oservices
7z x miui-services.jar -omiui_services
7z x miui-framework.jar -omiui_framework

if [ -f "framework/classes.dex" ]; then
  java -jar baksmali.jar d -a 34 "framework/classes.dex" -o classes
else
  echo "framework/classes.dex not found, skipping decompile."
fi

for i in {2..5}; do
  if [ -f "framework/classes${i}.dex" ]; then
    java -jar baksmali.jar d -a 34 "framework/classes${i}.dex" -o "classes${i}"
  else
    echo "framework/classes${i}.dex not found, skipping decompile."
  fi
done

if [ -f "services/classes.dex" ]; then
  java -jar baksmali.jar d -a 34 "services/classes.dex" -o services_classes
else
  echo "services/classes.dex not found, skipping decompile."
fi

for i in {2..5}; do
  if [ -f "services/classes${i}.dex" ]; then
    java -jar baksmali.jar d -a 34 "services/classes${i}.dex" -o "services_classes${i}"
  else
    echo "services/classes${i}.dex not found, skipping decompile."
  fi
done

java -jar baksmali.jar d -a 34 miui_services/classes.dex -o miui_services_classes
java -jar baksmali.jar d -a 34 miui_framework/classes.dex -o miui_framework_classes

python3 framework_patch.py True
python3 services_patch.py True
python3 miui-service_Patch.py
python3 miui-framework_patch.py

if [ -d classes ]; then
  java -jar smali.jar a -a 34 classes -o framework/classes.dex
else
  echo "classes directory not found, skipping recompilation."
fi

for i in {2..5}; do
  if [ -d "classes$i" ]; then
    java -jar smali.jar a -a 34 "classes$i" -o "framework/classes$i.dex"
  else
    echo "classes$i directory not found, skipping recompilation."
  fi
done

if [ -d services_classes ]; then
  java -jar smali.jar a -a 34 services_classes -o services/classes.dex
else
  echo "services_classes directory not found, skipping recompilation."
fi

for i in {2..5}; do
  if [ -d "services_classes$i" ]; then
    java -jar smali.jar a -a 34 "services_classes$i" -o "services/classes$i.dex"
  else
    echo "services_classes$i directory not found, skipping recompilation."
  fi
done

if [ -d miui_services_classes ]; then
  java -jar smali.jar a -a 34 miui_services_classes -o miui_services/classes.dex
else
  echo "miui_services_classes directory not found, skipping recompilation."
fi

if [ -d miui_framework_classes ]; then
  java -jar smali.jar a -a 34 miui_framework_classes -o miui_framework/classes.dex
else
  echo "miui_framework_classes directory not found, skipping recompilation."
fi

cd framework
7z a -tzip ../framework_new.zip *
cd ../services
7z a -tzip ../services_new.zip *
cd ../miui_services
7z a -tzip ../miui_services_new.zip *
cd ../miui_framework
7z a -tzip ../miui_framework_new.zip *
cd ..

zipalign -f -p -v -z 4 framework_new.zip aligned_framework.jar
zipalign -f -p -v -z 4 services_new.zip aligned_services.jar
zipalign -f -p -v -z 4 miui_services_new.zip aligned_miui_services.jar
zipalign -f -p -v -z 4 miui_framework_new.zip aligned_miui_framework.jar

mkdir -p magisk_module/system/framework
mkdir -p magisk_module/system/system_ext/framework
cp aligned_framework.jar magisk_module/system/framework/framework.jar
cp aligned_services.jar magisk_module/system/framework/services.jar
cp aligned_miui_services.jar magisk_module/system/system_ext/framework/miui-services.jar
cp aligned_miui_framework.jar magisk_module/system/system_ext/framework/miui-framework.jar

cd magisk_module
zip -r ../moded_framework_services.zip *

cd ..
rm -rf framework services miui_services miui_framework
rm -rf classes classes2 classes3 classes4 classes5 services_classes services_classes2 services_classes3 services_classes4 services_classes5 miui_services_classes miui_framework_classes
rm -rf framework_new.zip services_new.zip miui_services_new.zip miui_framework_new.zip aligned_framework.jar aligned_services.jar aligned_miui_services.jar aligned_miui_framework.jar

echo "Cleanup complete."