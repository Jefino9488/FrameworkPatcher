#!/bin/bash

7z x framework.jar -oframework
7z x services.jar -oservices

if [ -f "framework/classes.dex" ]; then
  java -jar smali/baksmali/build/libs/baksmali.jar d -a 34 "framework/classes.dex" -o classes
else
  echo "framework/classes.dex not found, skipping decompilation."
fi

for i in {2..5}; do
  if [ -f "framework/classes${i}.dex" ]; then
    java -jar smali/baksmali/build/libs/baksmali.jar d -a 34 "framework/classes${i}.dex" -o "classes${i}"
  else
    echo "framework/classes${i}.dex not found, skipping decompilation."
  fi
done

if [ -f "services/classes.dex" ]; then
  java -jar smali/baksmali/build/libs/baksmali.jar d -a 34 "services/classes.dex" -o services_classes
else
  echo "services/classes.dex not found, skipping decompilation."
fi

for i in {2..5}; do
  if [ -f "services/classes${i}.dex" ]; then
    java -jar smali/baksmali/build/libs/baksmali.jar d -a 34 "services/classes${i}.dex" -o "services_classes${i}"
  else
    echo "services/classes${i}.dex not found, skipping decompilation."
  fi
done
