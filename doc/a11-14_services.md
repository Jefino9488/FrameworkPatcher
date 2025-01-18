### **Services.jar Modifications**

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

#### **Additional Modifications:**

1. **Search for:**  
   ```
   invoke-interface {v4}, Lcom/android/server/pm/pkg/AndroidPackage;->isPersistent()Z
   ```  
   - Below this, locate:  
     ```
     move-result v2
     ```  
   - **Under it, add:**  
     ```
     const/4 v2, 0x0
     ```  
   **Done**
