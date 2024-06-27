# classes.dex

.class public Lcom/android/server/policy/PhoneWindowManager$MusicPrev;
.super Ljava/lang/Object;
.source "PhoneWindowManager.java"

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/server/policy/PhoneWindowManager;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x1
    name = "MusicPrev"
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/server/policy/PhoneWindowManager;


# direct methods
.method public constructor <init>(Lcom/android/server/policy/PhoneWindowManager;)V
    .registers 2
    .param p1, "this$0"  # Lcom/android/server/policy/PhoneWindowManager;

    .prologue
    .line 215
    iput-object p1, p0, Lcom/android/server/policy/PhoneWindowManager$MusicPrev;->this$0:Lcom/android/server/policy/PhoneWindowManager;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 3

    .prologue
    .line 218
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager$MusicPrev;->this$0:Lcom/android/server/policy/PhoneWindowManager;

    sget v1, Lcom/android/server/policy/VolBtnHelper;->mVolBtnVolDown:I

    invoke-virtual {v0, v1}, Lcom/android/server/policy/PhoneWindowManager;->sendMediaButtonEvent(I)V

    .line 219
    const/4 v0, 0x1

    sput-boolean v0, Lcom/android/server/policy/VolBtnHelper;->mIsVolLongPressed:Z

    .line 220
    return-void
.end method
