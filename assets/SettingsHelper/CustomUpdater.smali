# classes3.dex

.class public abstract Landroid/preference/CustomUpdater;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Landroid/preference/CustomUpdater$CustomUpdaterI;,
        Landroid/preference/CustomUpdater$CustomObjectTransmitter;,
        Landroid/preference/CustomUpdater$CustomReceiver;
    }
.end annotation


# static fields
.field private static customUpdater:Landroid/preference/CustomUpdater;


# direct methods
.method public constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static getInstance()Landroid/preference/CustomUpdater;
    .registers 1

    sget-object v0, Landroid/preference/CustomUpdater;->customUpdater:Landroid/preference/CustomUpdater;

    if-nez v0, :cond_b

    new-instance v0, Landroid/preference/CustomUpdater$CustomUpdaterI;

    invoke-direct {v0}, Landroid/preference/CustomUpdater$CustomUpdaterI;-><init>()V

    sput-object v0, Landroid/preference/CustomUpdater;->customUpdater:Landroid/preference/CustomUpdater;

    :cond_b
    sget-object v0, Landroid/preference/CustomUpdater;->customUpdater:Landroid/preference/CustomUpdater;

    return-object v0
.end method


# virtual methods
.method public abstract addCustomObjectTransmitter(Landroid/preference/CustomUpdater$CustomObjectTransmitter;)V
.end method

.method public abstract addCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;Ljava/lang/String;)V
.end method

.method public abstract addCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;[Ljava/lang/String;)V
.end method

.method public abstract beginChange(Ljava/lang/String;)V
.end method

.method public abstract beginTransmition(Ljava/lang/Object;)V
.end method

.method public abstract removeCustomObjectTransmitter(Landroid/preference/CustomUpdater$CustomObjectTransmitter;)V
.end method

.method public abstract removeCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;Ljava/lang/String;)V
.end method

.method public abstract removeCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;[Ljava/lang/String;)V
.end method
