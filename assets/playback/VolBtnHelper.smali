# classes.dex

.class public Lcom/android/server/policy/VolBtnHelper;
.super Ljava/lang/Object;
.source "VolBtnHelper.java"

# interfaces
.implements Landroid/preference/CustomUpdater$CustomReceiver;


# static fields
.field private static final instance:Lcom/android/server/policy/VolBtnHelper;

.field public static mIsVolLongPressed:Z = false

.field public static mVolBtnMusicControls:Z = false

.field public static mVolBtnTimeout:I = 0x0

.field public static mVolBtnVibrate:Z = false

.field public static mVolBtnVolDown:I = 0x0

.field public static mVolBtnVolUp:I = 0x0

.field private static final sKeys:Ljava/lang/String; = "lock_screen_volume"


# direct methods
.method static constructor <clinit>()V
    .registers 1

    .prologue
    .line 8
    new-instance v0, Lcom/android/server/policy/VolBtnHelper;

    invoke-direct {v0}, Lcom/android/server/policy/VolBtnHelper;-><init>()V

    sput-object v0, Lcom/android/server/policy/VolBtnHelper;->instance:Lcom/android/server/policy/VolBtnHelper;

    return-void
.end method

.method private constructor <init>()V
    .registers 3

    .prologue
    .line 14
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    .line 15
    invoke-static {}, Landroid/preference/CustomUpdater;->getInstance()Landroid/preference/CustomUpdater;

    move-result-object v0

    const-string/jumbo v1, "lock_screen_volume"

    invoke-virtual {v0, p0, v1}, Landroid/preference/CustomUpdater;->addCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;Ljava/lang/String;)V

    .line 16
    const-string/jumbo v0, "lock_screen_volume"

    invoke-virtual {p0, v0}, Lcom/android/server/policy/VolBtnHelper;->onCustomChanged(Ljava/lang/String;)V

    .line 17
    return-void
.end method

.method private update()V
    .registers 6

    .prologue
    const/4 v3, 0x1

    .line 20
    const-string/jumbo v4, "volbtn_music_controls"

    invoke-static {v4, v3}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v4

    if-ne v4, v3, :cond_43

    :goto_a
    sput-boolean v3, Lcom/android/server/policy/VolBtnHelper;->mVolBtnMusicControls:Z

    .line 21
    const-string/jumbo v3, "volbtn_timeout"

    const/16 v4, 0x1f4

    invoke-static {v3, v4}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v0

    .line 22
    .local v0, "intofSettings":I
    if-nez v0, :cond_19

    .line 23
    const/16 v0, 0x1f4

    .line 25
    :cond_19
    sput v0, Lcom/android/server/policy/VolBtnHelper;->mVolBtnTimeout:I

    .line 26
    const-string/jumbo v3, "volbtn_vol_up"

    const/16 v4, 0x57

    invoke-static {v3, v4}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v1

    .line 27
    .local v1, "intofSettings2":I
    if-nez v1, :cond_28

    .line 28
    const/16 v1, 0x57

    .line 30
    :cond_28
    sput v1, Lcom/android/server/policy/VolBtnHelper;->mVolBtnVolUp:I

    .line 31
    const-string/jumbo v3, "volbtn_vol_down"

    const/16 v4, 0x58

    invoke-static {v3, v4}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v2

    .line 32
    .local v2, "intofSettings3":I
    if-nez v2, :cond_37

    .line 33
    const/16 v2, 0x58

    .line 35
    :cond_37
    sput v2, Lcom/android/server/policy/VolBtnHelper;->mVolBtnVolDown:I

    .line 36
    const-string/jumbo v3, "volbtn_vibrate"

    invoke-static {v3}, Landroid/preference/SettingsHelper;->getBoolofSettings(Ljava/lang/String;)Z

    move-result v3

    sput-boolean v3, Lcom/android/server/policy/VolBtnHelper;->mVolBtnVibrate:Z

    .line 37
    return-void

    .line 20
    .end local v0  # "intofSettings":I
    .end local v1  # "intofSettings2":I
    .end local v2  # "intofSettings3":I
    :cond_43
    const/4 v3, 0x0

    goto :goto_a
.end method


# virtual methods
.method public onCustomChanged(Ljava/lang/String;)V
    .registers 3
    .param p1, "key"  # Ljava/lang/String;

    .prologue
    .line 41
    const-string/jumbo v0, "lock_screen_volume"

    invoke-virtual {p1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_c

    .line 42
    invoke-direct {p0}, Lcom/android/server/policy/VolBtnHelper;->update()V

    .line 43
    :cond_c
    return-void
.end method
