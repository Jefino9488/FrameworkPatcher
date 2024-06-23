echo Decompiling classes.dex
java -jar smali/baksmali/build/libs/baksmali.jar d -a 34 framework/classes.dex -o classes
echo Decompiling classes2.dex
java -jar smali/baksmali/build/libs/baksmali.jar d -a 34 framework/classes2.dex -o classes2
echo Decompiling classes3.dex
java -jar smali/baksmali/build/libs/baksmali.jar d -a 34 framework/classes3.dex -o classes3