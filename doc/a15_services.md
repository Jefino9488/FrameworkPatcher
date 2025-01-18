### **Services.jar (A15) Modifications**

#### **Methods:**

1. **Method:** `checkDowngrade`  
   - **Change the return value to:**  
     ```
     return-void
     ```  
   **Done**

2. **Method:** `shouldCheckUpgradeKeySetLocked`  
   - **Change the return value to:**  
     ```
     return 0
     ```  
   **Done**

3. **Method:** `verifySignatures`  
   - **Change the return value to:**  
     ```
     return 0
     ```  
   **Done**

4. **Method:** `compareSignatures`  
   - **Change the return value to:**  
     ```
     return 0
     ```  
   **Done**

5. **Method:** `matchSignaturesCompat`  
   - **Change the return value to:**  
     ```
     return 1
     ```  
   **Done**

---

#### **Class: `com.android.server.pm.InstallPackageHelper`**

1. **Search for:**  
   ```
   invoke-interface {v7}, Lcom/android/server/pm/pkg/AndroidPackage;->isLeavingSharedUser()Z
   ```  
   - Above this line, locate:  
     ```
     if-eqz v12, :cond_xx
     ```  
   - **Above `if-eqz v12, :cond_xx`, add:**  
     ```
     const/4 v12, 0x1
     ```  
   **Done**

---

#### **Class: `com.android.server.pm.ReconcilePackageUtils`**

1. **In the Method:** `.method static constructor <clinit>()V`  
   - **Change:**  
     ```
     const/4 v0, 0x0
     ```  
   - **To:**  
     ```
     const/4 v0, 0x1
     ```  
   **Done**
