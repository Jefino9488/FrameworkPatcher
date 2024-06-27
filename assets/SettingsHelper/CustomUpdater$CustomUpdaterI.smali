# classes3.dex

.class Landroid/preference/CustomUpdater$CustomUpdaterI;
.super Landroid/preference/CustomUpdater;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Landroid/preference/CustomUpdater;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0xa
    name = "CustomUpdaterI"
.end annotation


# static fields
.field private static final TAG:Ljava/lang/String;


# instance fields
.field private mContext:Landroid/content/Context;

.field private mKeyList:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList",
            "<",
            "Ljava/lang/String;",
            ">;"
        }
    .end annotation
.end field

.field private mReceiver:Landroid/content/BroadcastReceiver;

.field private final mTransmiterReceivers:Landroid/util/ArrayMap;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Landroid/util/ArrayMap",
            "<",
            "Ljava/lang/Object;",
            "Landroid/preference/CustomUpdater$CustomObjectTransmitter;",
            ">;"
        }
    .end annotation
.end field

.field private final mUpdateReceivers:Landroid/util/ArrayMap;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Landroid/util/ArrayMap",
            "<",
            "Ljava/lang/Object;",
            "Landroid/preference/CustomUpdater$CustomReceiver;",
            ">;"
        }
    .end annotation
.end field


# direct methods
.method static constructor <clinit>()V
    .registers 1

    const-class v0, Landroid/preference/CustomUpdater;

    invoke-virtual {v0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v0

    sput-object v0, Landroid/preference/CustomUpdater$CustomUpdaterI;->TAG:Ljava/lang/String;

    return-void
.end method

.method constructor <init>()V
    .registers 2

    invoke-direct {p0}, Landroid/preference/CustomUpdater;-><init>()V

    new-instance v0, Landroid/preference/CustomUpdater$CustomUpdaterI$1;

    invoke-direct {v0, p0}, Landroid/preference/CustomUpdater$CustomUpdaterI$1;-><init>(Landroid/preference/CustomUpdater$CustomUpdaterI;)V

    iput-object v0, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mReceiver:Landroid/content/BroadcastReceiver;

    invoke-direct {p0}, Landroid/preference/CustomUpdater$CustomUpdaterI;->getContext()Landroid/content/Context;

    move-result-object v0

    iput-object v0, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mContext:Landroid/content/Context;

    new-instance v0, Landroid/util/ArrayMap;

    invoke-direct {v0}, Landroid/util/ArrayMap;-><init>()V

    iput-object v0, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mUpdateReceivers:Landroid/util/ArrayMap;

    new-instance v0, Landroid/util/ArrayMap;

    invoke-direct {v0}, Landroid/util/ArrayMap;-><init>()V

    iput-object v0, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mTransmiterReceivers:Landroid/util/ArrayMap;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mKeyList:Ljava/util/ArrayList;

    return-void
.end method

.method private Contains(Ljava/lang/String;)Z
    .registers 5

    iget-object v1, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mKeyList:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->size()I

    move-result v1

    if-lez v1, :cond_24

    if-eqz p1, :cond_24

    iget-object v1, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mKeyList:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :cond_10
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_24

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Ljava/lang/String;

    invoke-virtual {p1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_10

    const/4 v1, 0x1

    :goto_23
    return v1

    :cond_24
    const/4 v1, 0x0

    goto :goto_23
.end method

.method static synthetic access$000(Landroid/preference/CustomUpdater$CustomUpdaterI;Ljava/lang/String;)V
    .registers 2

    invoke-direct {p0, p1}, Landroid/preference/CustomUpdater$CustomUpdaterI;->applyCustomChange(Ljava/lang/String;)V

    return-void
.end method

.method private applyCustomChange(Ljava/lang/String;)V
    .registers 5

    iget-object v2, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mUpdateReceivers:Landroid/util/ArrayMap;

    monitor-enter v2

    const/4 v0, 0x0

    :goto_4
    :try_start_4
    iget-object v1, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mUpdateReceivers:Landroid/util/ArrayMap;

    invoke-virtual {v1}, Landroid/util/ArrayMap;->size()I

    move-result v1

    if-ge v0, v1, :cond_1a

    iget-object v1, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mUpdateReceivers:Landroid/util/ArrayMap;

    invoke-virtual {v1, v0}, Landroid/util/ArrayMap;->valueAt(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/preference/CustomUpdater$CustomReceiver;

    invoke-interface {v1, p1}, Landroid/preference/CustomUpdater$CustomReceiver;->onCustomChanged(Ljava/lang/String;)V

    add-int/lit8 v0, v0, 0x1

    goto :goto_4

    :cond_1a
    monitor-exit v2

    return-void

    :catchall_1c
    move-exception v1

    monitor-exit v2
    :try_end_1e
    .catchall {:try_start_4 .. :try_end_1e} :catchall_1c

    throw v1
.end method

.method private applyCustomTransmition(Ljava/lang/Object;)V
    .registers 5

    iget-object v2, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mTransmiterReceivers:Landroid/util/ArrayMap;

    monitor-enter v2

    const/4 v0, 0x0

    :goto_4
    :try_start_4
    iget-object v1, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mTransmiterReceivers:Landroid/util/ArrayMap;

    invoke-virtual {v1}, Landroid/util/ArrayMap;->size()I

    move-result v1

    if-ge v0, v1, :cond_1a

    iget-object v1, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mTransmiterReceivers:Landroid/util/ArrayMap;

    invoke-virtual {v1, v0}, Landroid/util/ArrayMap;->valueAt(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/preference/CustomUpdater$CustomObjectTransmitter;

    invoke-interface {v1, p1}, Landroid/preference/CustomUpdater$CustomObjectTransmitter;->onObjectArrived(Ljava/lang/Object;)V

    add-int/lit8 v0, v0, 0x1

    goto :goto_4

    :cond_1a
    monitor-exit v2

    return-void

    :catchall_1c
    move-exception v1

    monitor-exit v2
    :try_end_1e
    .catchall {:try_start_4 .. :try_end_1e} :catchall_1c

    throw v1
.end method

.method private getContext()Landroid/content/Context;
    .registers 11

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

.method private registerReseiver([Ljava/lang/String;Z)V
    .registers 10

    iget-object v4, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mUpdateReceivers:Landroid/util/ArrayMap;

    monitor-enter v4

    if-nez p2, :cond_c

    :try_start_5
    iget-object v3, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mContext:Landroid/content/Context;

    iget-object v5, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mReceiver:Landroid/content/BroadcastReceiver;

    invoke-virtual {v3, v5}, Landroid/content/Context;->unregisterReceiver(Landroid/content/BroadcastReceiver;)V

    :cond_c
    if-eqz p1, :cond_22

    array-length v5, p1

    const/4 v3, 0x0

    :goto_10
    if-ge v3, v5, :cond_22

    aget-object v1, p1, v3

    invoke-direct {p0, v1}, Landroid/preference/CustomUpdater$CustomUpdaterI;->Contains(Ljava/lang/String;)Z

    move-result v6

    if-nez v6, :cond_1f

    iget-object v6, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mKeyList:Ljava/util/ArrayList;

    invoke-virtual {v6, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    :cond_1f
    add-int/lit8 v3, v3, 0x1

    goto :goto_10

    :cond_22
    iget-object v3, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mKeyList:Ljava/util/ArrayList;

    invoke-virtual {v3}, Ljava/util/ArrayList;->size()I

    move-result v3

    if-eqz v3, :cond_68

    new-instance v0, Landroid/content/IntentFilter;

    invoke-direct {v0}, Landroid/content/IntentFilter;-><init>()V

    iget-object v3, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mKeyList:Ljava/util/ArrayList;

    invoke-virtual {v3}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v3

    :goto_35
    invoke-interface {v3}, Ljava/util/Iterator;->hasNext()Z

    move-result v5

    if-eqz v5, :cond_61

    invoke-interface {v3}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Ljava/lang/String;

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "my.settings.intent."

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    const-string v6, ".CHANGE"

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v0, v5}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    goto :goto_35

    :catchall_5e
    move-exception v3

    monitor-exit v4
    :try_end_60
    .catchall {:try_start_5 .. :try_end_60} :catchall_5e

    throw v3

    :cond_61
    :try_start_61
    iget-object v3, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mContext:Landroid/content/Context;

    iget-object v5, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mReceiver:Landroid/content/BroadcastReceiver;

    invoke-virtual {v3, v5, v0}, Landroid/content/Context;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;)Landroid/content/Intent;

    :cond_68
    monitor-exit v4
    :try_end_69
    .catchall {:try_start_61 .. :try_end_69} :catchall_5e

    return-void
.end method


# virtual methods
.method public addCustomObjectTransmitter(Landroid/preference/CustomUpdater$CustomObjectTransmitter;)V
    .registers 4

    iget-object v1, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mTransmiterReceivers:Landroid/util/ArrayMap;

    monitor-enter v1

    :try_start_3
    iget-object v0, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mTransmiterReceivers:Landroid/util/ArrayMap;

    invoke-virtual {v0, p1, p1}, Landroid/util/ArrayMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    monitor-exit v1

    return-void

    :catchall_a
    move-exception v0

    monitor-exit v1
    :try_end_c
    .catchall {:try_start_3 .. :try_end_c} :catchall_a

    throw v0
.end method

.method public addCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;Ljava/lang/String;)V
    .registers 5

    const/4 v0, 0x1

    new-array v0, v0, [Ljava/lang/String;

    const/4 v1, 0x0

    aput-object p2, v0, v1

    invoke-virtual {p0, p1, v0}, Landroid/preference/CustomUpdater$CustomUpdaterI;->addCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;[Ljava/lang/String;)V

    return-void
.end method

.method public addCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;[Ljava/lang/String;)V
    .registers 5

    iget-object v1, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mUpdateReceivers:Landroid/util/ArrayMap;

    invoke-virtual {v1}, Landroid/util/ArrayMap;->isEmpty()Z

    move-result v0

    iget-object v1, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mUpdateReceivers:Landroid/util/ArrayMap;

    invoke-virtual {v1, p1, p1}, Landroid/util/ArrayMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    invoke-direct {p0, p2, v0}, Landroid/preference/CustomUpdater$CustomUpdaterI;->registerReseiver([Ljava/lang/String;Z)V

    return-void
.end method

.method public beginChange(Ljava/lang/String;)V
    .registers 6

    iget-object v0, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mContext:Landroid/content/Context;

    new-instance v1, Landroid/content/Intent;

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "my.settings.intent."

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, ".CHANGE"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-direct {v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    invoke-virtual {v0, v1}, Landroid/content/Context;->sendBroadcast(Landroid/content/Intent;)V

    return-void
.end method

.method public beginTransmition(Ljava/lang/Object;)V
    .registers 2

    invoke-direct {p0, p1}, Landroid/preference/CustomUpdater$CustomUpdaterI;->applyCustomTransmition(Ljava/lang/Object;)V

    return-void
.end method

.method public removeCustomObjectTransmitter(Landroid/preference/CustomUpdater$CustomObjectTransmitter;)V
    .registers 4

    iget-object v1, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mTransmiterReceivers:Landroid/util/ArrayMap;

    monitor-enter v1

    :try_start_3
    iget-object v0, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mTransmiterReceivers:Landroid/util/ArrayMap;

    invoke-virtual {v0}, Landroid/util/ArrayMap;->isEmpty()Z

    move-result v0

    if-nez v0, :cond_10

    iget-object v0, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mTransmiterReceivers:Landroid/util/ArrayMap;

    invoke-virtual {v0, p1}, Landroid/util/ArrayMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    :cond_10
    monitor-exit v1

    return-void

    :catchall_12
    move-exception v0

    monitor-exit v1
    :try_end_14
    .catchall {:try_start_3 .. :try_end_14} :catchall_12

    throw v0
.end method

.method public removeCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;Ljava/lang/String;)V
    .registers 5

    const/4 v0, 0x1

    new-array v0, v0, [Ljava/lang/String;

    const/4 v1, 0x0

    aput-object p2, v0, v1

    invoke-virtual {p0, p1, v0}, Landroid/preference/CustomUpdater$CustomUpdaterI;->removeCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;[Ljava/lang/String;)V

    return-void
.end method

.method public removeCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;[Ljava/lang/String;)V
    .registers 9

    iget-object v3, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mUpdateReceivers:Landroid/util/ArrayMap;

    monitor-enter v3

    :try_start_3
    iget-object v2, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mUpdateReceivers:Landroid/util/ArrayMap;

    invoke-virtual {v2}, Landroid/util/ArrayMap;->isEmpty()Z

    move-result v0

    if-nez v0, :cond_30

    iget-object v2, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mUpdateReceivers:Landroid/util/ArrayMap;

    invoke-virtual {v2, p1}, Landroid/util/ArrayMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    array-length v4, p2

    const/4 v2, 0x0

    :goto_12
    if-ge v2, v4, :cond_24

    aget-object v1, p2, v2

    invoke-direct {p0, v1}, Landroid/preference/CustomUpdater$CustomUpdaterI;->Contains(Ljava/lang/String;)Z

    move-result v5

    if-eqz v5, :cond_21

    iget-object v5, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mKeyList:Ljava/util/ArrayList;

    invoke-virtual {v5, v1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    :cond_21
    add-int/lit8 v2, v2, 0x1

    goto :goto_12

    :cond_24
    const/4 v2, 0x0

    iget-object v4, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mUpdateReceivers:Landroid/util/ArrayMap;

    invoke-virtual {v4}, Landroid/util/ArrayMap;->isEmpty()Z

    move-result v4

    invoke-direct {p0, v2, v4}, Landroid/preference/CustomUpdater$CustomUpdaterI;->registerReseiver([Ljava/lang/String;Z)V

    :goto_2e
    monitor-exit v3

    return-void

    :cond_30
    iget-object v2, p0, Landroid/preference/CustomUpdater$CustomUpdaterI;->mKeyList:Ljava/util/ArrayList;

    invoke-virtual {v2}, Ljava/util/ArrayList;->clear()V

    goto :goto_2e

    :catchall_36
    move-exception v2

    monitor-exit v3
    :try_end_38
    .catchall {:try_start_3 .. :try_end_38} :catchall_36

    throw v2
.end method
