SKIPMOUNT=false
PROPFILE=true
POSTFSDATA=true
LATESTARTSERVICE=true

DEX2OAT_PATH="/apex/com.android.art/bin/dex2oat"

print_modname() {
  ui_print "********************************"
  ui_print "  Framework and Services Patcher"
  ui_print "********************************"
}

on_install() {
  ui_print "- Extracting module files..."
  unzip -o "$ZIPFILE" 'system/*' -d $MODPATH

  DIRS_TO_PROCESS="$MODPATH/system/framework $MODPATH/system/system_ext/framework"

  ui_print "- Generating .oat files in framework/oat/ folder..."

  for DIR in $DIRS_TO_PROCESS; do
    OAT_DIR="$DIR/oat"
    mkdir -p "$OAT_DIR"

    for JAR in "$DIR"/*.jar; do
      if [ -f "$JAR" ]; then
        OAT_FILE="$OAT_DIR/$(basename "$JAR").oat"
        ui_print "-- Processing $(basename "$JAR")..."

        if [ -x "$DEX2OAT_PATH" ]; then
          "$DEX2OAT_PATH" --dex-file="$JAR" --oat-file="$OAT_FILE" --instruction-set=arm64
          if [ $? -eq 0 ]; then
            ui_print "-- Successfully generated $(basename "$OAT_FILE") in $OAT_DIR."
          else
            ui_print "-- Failed to process $(basename "$JAR")."
          fi
        else
          ui_print "-- dex2oat not found at $DEX2OAT_PATH."
          ui_print "-- Skipping $(basename "$JAR")."
        fi
      fi
    done
  done

  ui_print "- OAT file generation completed."
}

set_permissions() {
  set_perm_recursive "$MODPATH" 0 0 0755 0644
}