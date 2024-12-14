if [ -d classes ]; then
  java -jar smali.jar a -a 35 classes -o framework/classes.dex
else
  echo "classes directory not found, skipping recompilation."
fi

for i in {2..5}; do
  if [ -d "classes$i" ]; then
    java -jar smali.jar a -a 35 "classes$i" -o "framework/classes$i.dex"
  else
    echo "classes$i directory not found, skipping recompilation."
  fi
done

if [ -d services_classes ]; then
  java -jar smali.jar a -a 35 services_classes -o services/classes.dex
else
  echo "services_classes directory not found, skipping recompilation."
fi

for i in {2..5}; do
  if [ -d "services_classes$i" ]; then
    java -jar smali.jar a -a 35 "services_classes$i" -o "services/classes$i.dex"
  else
    echo "services_classes$i directory not found, skipping recompilation."
  fi
done

cd framework
7z a -tzip ../framework_new.zip *
cd ../services
7z a -tzip ../services_new.zip *
cd ..

zipalign -f -p -v -z 4 framework_new.zip aligned_framework.jar
zipalign -f -p -v -z 4 services_new.zip aligned_services.jar


mkdir -p magisk_module/system/framework
cp aligned_framework.jar magisk_module/system/framework/framework.jar
cp aligned_services.jar magisk_module/system/framework/services.jar

cd magisk_module
zip -r ../moded_framework_services.zip *

cd ..

echo "Cleanup complete."