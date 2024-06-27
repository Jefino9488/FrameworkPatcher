# classes3.dex

.class public final Landroid/preference/SettingsHelper;
.super Ljava/lang/Object;


# static fields
.field private static sCR:Landroid/content/ContentResolver;

.field private static sCon:Landroid/content/Context;


# direct methods
.method public constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method private static createContext()Landroid/content/Context;
    .registers 10

    const/4 v1, 0x0

    :try_start_1
    const-string v8, "android.app.AppGlobals"

    invoke-static {v8}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v0

    const-string v8, "getInitialApplication"

    const/4 v9, 0x0

    new-array v9, v9, [Ljava/lang/Class;

    invoke-virtual {v0, v8, v9}, Ljava/lang/Class;->getMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v5

    new-instance v8, Ljava/lang/Object;

    invoke-direct {v8}, Ljava/lang/Object;-><init>()V

    const/4 v9, 0x0

    new-array v9, v9, [Ljava/lang/Object;

    invoke-virtual {v5, v8, v9}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v7

    instance-of v8, v7, Landroid/app/Application;

    if-eqz v8, :cond_29

    check-cast v7, Landroid/app/Application;

    const-string v8, "android"

    const/4 v9, 0x2

    invoke-virtual {v7, v8, v9}, Landroid/app/Application;->createPackageContext(Ljava/lang/String;I)Landroid/content/Context;
    :try_end_28
    .catch Ljava/lang/ClassNotFoundException; {:try_start_1 .. :try_end_28} :catch_2a
    .catch Ljava/lang/NoSuchMethodException; {:try_start_1 .. :try_end_28} :catch_33
    .catch Ljava/lang/IllegalAccessException; {:try_start_1 .. :try_end_28} :catch_3c
    .catch Ljava/lang/reflect/InvocationTargetException; {:try_start_1 .. :try_end_28} :catch_45
    .catch Landroid/content/pm/PackageManager$NameNotFoundException; {:try_start_1 .. :try_end_28} :catch_4e

    move-result-object v1

    :cond_29
    :goto_29
    return-object v1

    :catch_2a
    move-exception v0

    const-string v8, "myapp"

    const-string v9, "No find AppGlobals.class"

    invoke-static {v8, v9}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_29

    :catch_33
    move-exception v4

    const-string v8, "myapp"

    const-string v9, "No find getInitialApplication method "

    invoke-static {v8, v9}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_29

    :catch_3c
    move-exception v2

    const-string v8, "myapp"

    const-string v9, "No invoke metod "

    invoke-static {v8, v9}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_29

    :catch_45
    move-exception v3

    const-string v8, "myapp"

    const-string v9, "No invoke metod "

    invoke-static {v8, v9}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_29

    :catch_4e
    move-exception v6

    const-string v8, "myapp"

    const-string v9, "CreateContext error"

    invoke-static {v8, v9}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_29
.end method

.method public static getAnimId(I)I
    .registers 7

    const-string v4, "system_animation"

    invoke-static {v4}, Landroid/preference/SettingsHelper;->getStringofSettings(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v2

    if-eqz v2, :cond_52

    const-string v4, "stock"

    invoke-virtual {v2, v4}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-nez v4, :cond_52

    invoke-static {}, Landroid/preference/SettingsHelper;->getCon()Landroid/content/Context;

    move-result-object v4

    invoke-virtual {v4}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    invoke-virtual {v1, p0}, Landroid/content/res/Resources;->getResourceName(I)Ljava/lang/String;

    move-result-object v3

    if-eqz v3, :cond_52

    const-string v4, "/"

    invoke-virtual {v3, v4}, Ljava/lang/String;->indexOf(Ljava/lang/String;)I

    move-result v0

    if-lez v0, :cond_52

    add-int/lit8 v4, v0, 0x1

    invoke-virtual {v3}, Ljava/lang/String;->length()I

    move-result v5

    invoke-virtual {v3, v4, v5}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object v3

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v4, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    const-string v5, "_"

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    const-string v4, "anim"

    const-string v5, "android"

    invoke-virtual {v1, v2, v4, v5}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v0

    if-eqz v0, :cond_52

    move p0, v0

    :cond_52
    return p0
.end method

.method public static getBoolofSettings(Ljava/lang/String;)Z
    .registers 4

    const/4 v0, 0x1

    const/4 v1, 0x0

    invoke-static {}, Landroid/preference/SettingsHelper;->getCR()Landroid/content/ContentResolver;

    move-result-object v2

    invoke-static {v2, p0, v1}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v2

    if-ne v2, v0, :cond_d

    :goto_c
    return v0

    :cond_d
    move v0, v1

    goto :goto_c
.end method

.method public static getBoolofSettings(Ljava/lang/String;I)Z
    .registers 4

    const/4 v0, 0x1

    invoke-static {}, Landroid/preference/SettingsHelper;->getCR()Landroid/content/ContentResolver;

    move-result-object v1

    invoke-static {v1, p0, p1}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1

    if-ne v1, v0, :cond_c

    :goto_b
    return v0

    :cond_c
    const/4 v0, 0x0

    goto :goto_b
.end method

.method private static getCR()Landroid/content/ContentResolver;
    .registers 1

    sget-object v0, Landroid/preference/SettingsHelper;->sCR:Landroid/content/ContentResolver;

    if-nez v0, :cond_e

    invoke-static {}, Landroid/preference/SettingsHelper;->getCon()Landroid/content/Context;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    sput-object v0, Landroid/preference/SettingsHelper;->sCR:Landroid/content/ContentResolver;

    :cond_e
    sget-object v0, Landroid/preference/SettingsHelper;->sCR:Landroid/content/ContentResolver;

    return-object v0
.end method

.method public static getCon()Landroid/content/Context;
    .registers 1

    sget-object v0, Landroid/preference/SettingsHelper;->sCon:Landroid/content/Context;

    if-nez v0, :cond_a

    invoke-static {}, Landroid/preference/SettingsHelper;->createContext()Landroid/content/Context;

    move-result-object v0

    sput-object v0, Landroid/preference/SettingsHelper;->sCon:Landroid/content/Context;

    :cond_a
    sget-object v0, Landroid/preference/SettingsHelper;->sCon:Landroid/content/Context;

    return-object v0
.end method

.method public static getIntofSettings(Ljava/lang/String;)I
    .registers 3

    invoke-static {}, Landroid/preference/SettingsHelper;->getCR()Landroid/content/ContentResolver;

    move-result-object v0

    const/4 v1, 0x0

    invoke-static {v0, p0, v1}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    return v0
.end method

.method public static getIntofSettings(Ljava/lang/String;I)I
    .registers 3

    invoke-static {}, Landroid/preference/SettingsHelper;->getCR()Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {v0, p0, p1}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    return v0
.end method

.method public static getIntofSettingsForUser(Ljava/lang/String;II)I
    .registers 4

    invoke-static {}, Landroid/preference/SettingsHelper;->getCR()Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {v0, p0, p1, p2}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    return v0
.end method

.method public static getIntofSettingss(Ljava/lang/String;)I
    .registers 3

    invoke-static {}, Landroid/preference/SettingsHelper;->getCR()Landroid/content/ContentResolver;

    move-result-object v0

    const/4 v1, 0x0

    invoke-static {v0, p0, v1}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    return v0
.end method

.method public static getLongofSettings(Ljava/lang/String;)J
    .registers 5

    invoke-static {}, Landroid/preference/SettingsHelper;->getCR()Landroid/content/ContentResolver;

    move-result-object v0

    const-wide/16 v2, 0x0

    invoke-static {v0, p0, v2, v3}, Landroid/provider/Settings$System;->getLong(Landroid/content/ContentResolver;Ljava/lang/String;J)J

    move-result-wide v0

    return-wide v0
.end method

.method public static getLongofSettings(Ljava/lang/String;J)J
    .registers 6

    invoke-static {}, Landroid/preference/SettingsHelper;->getCR()Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {v0, p0, p1, p2}, Landroid/provider/Settings$System;->getLong(Landroid/content/ContentResolver;Ljava/lang/String;J)J

    move-result-wide v0

    return-wide v0
.end method

.method public static getStringofSettings(Ljava/lang/String;)Ljava/lang/String;
    .registers 2

    invoke-static {}, Landroid/preference/SettingsHelper;->getCR()Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {v0, p0}, Landroid/provider/Settings$System;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    return-object v0
.end method

.method public static getStringofSettings(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    .registers 4

    invoke-static {}, Landroid/preference/SettingsHelper;->getCR()Landroid/content/ContentResolver;

    move-result-object v1

    invoke-static {v1, p0}, Landroid/provider/Settings$System;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    if-nez v0, :cond_b

    :goto_a
    return-object p1

    :cond_b
    move-object p1, v0

    goto :goto_a
.end method

.method public static putBoolinSettings(Ljava/lang/String;Z)V
    .registers 4

    invoke-static {}, Landroid/preference/SettingsHelper;->getCR()Landroid/content/ContentResolver;

    move-result-object v1

    if-eqz p1, :cond_b

    const/4 v0, 0x1

    :goto_7
    invoke-static {v1, p0, v0}, Landroid/provider/Settings$System;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    return-void

    :cond_b
    const/4 v0, 0x0

    goto :goto_7
.end method

.method public static putIntinSettings(Ljava/lang/String;I)V
    .registers 3

    invoke-static {}, Landroid/preference/SettingsHelper;->getCR()Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {v0, p0, p1}, Landroid/provider/Settings$System;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    return-void
.end method

.method public static putLonginSettings(Ljava/lang/String;J)V
    .registers 4

    invoke-static {}, Landroid/preference/SettingsHelper;->getCR()Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {v0, p0, p1, p2}, Landroid/provider/Settings$System;->putLong(Landroid/content/ContentResolver;Ljava/lang/String;J)Z

    return-void
.end method

.method public static putStringinSettings(Ljava/lang/String;Ljava/lang/String;)V
    .registers 3

    invoke-static {}, Landroid/preference/SettingsHelper;->getCR()Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {v0, p0, p1}, Landroid/provider/Settings$System;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Z

    return-void
.end method
