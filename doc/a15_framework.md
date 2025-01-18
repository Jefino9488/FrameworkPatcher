
### **A15 Framework Modifications**

#### **File:** `android.content.pm.PackageParser`

1. **Search:**  
   ```
   invoke-static {v2, v0, v1}, Landroid/util/apk/ApkSignatureVerifier;->unsafeGetCertsWithoutVerification(Landroid/content/pm/parsing/result/ParseInput;Ljava/lang/String;I)Landroid/content/pm/parsing/result/ParseResult;
   ```  
   **Above it, add:**  
   ```
   const/4 v1, 0x1
   ```  
   **Done**

2. **Search:**  
   ```
   "<manifest> specifies bad sharedUserId name \""
   ```  
   - Above this, you’ll find `if-nez v5, :cond_x`.  
   - **Above `if-nez v5, :cond_x`, add:**  
     ```
     const/4 v5, 0x1
     ```  
   **Done**

---

#### **File:** `android.content.pm.PackageParser$PackageParserException`

1. **Search:**  
   ```
   iput p1, p0, Landroid/content/pm/PackageParser$PackageParserException;->error:I
   ```  
   **Above it, add:**  
   ```
   const/4 p1, 0x0
   ```  
   **Done**

---

#### **File:** `android.content.pm.PackageParser$SigningDetails`  
- **Search for:** `checkCapability`  
  - You will find three methods.  
  - **Change the return value to `1` in all of them.**  
  **Done**

---

#### **File:** `android.content.pm.SigningDetails`  
- **Search for:** `checkCapability`  
  - You will find three methods.  
  - **Change the return value to `1` in all of them.**  
  **Done**

---

#### **File:** `android.content.pm.SigningDetails`  
- **Search for:** `hasAncestorOrSelf`  
  - **Change the return value to `1`.**  
  **Done**

---

#### **File:** `android.util.apk.ApkSignatureSchemeV2Verifier`

1. **Search:**  
   ```
   invoke-static {v8, v7}, Ljava/security/MessageDigest;->isEqual([B[B)Z
   ```  
   **Change:**  
   ```
   move-result v0
   ```  
   **To:**  
   ```
   const/4 v0, 0x1
   ```  
   **Done**

---

#### **File:** `android.util.apk.ApkSignatureSchemeV3Verifier`

1. **Search:**  
   ```
   invoke-static {v12, v6}, Ljava/security/MessageDigest;->isEqual([B[B)Z
   ```  
   **Change:**  
   ```
   move-result v0
   ```  
   **To:**  
   ```
   const/4 v0, 0x1
   ```  
   **Done**

---

#### **File:** `android.util.apk.ApkSignatureVerifier`

1. **Search for:** `getMinimumSignatureSchemeVersionForTargetSdk`  
   - **Change the return value to `0`.**  
   **Done**

2. **Search:**  
   ```
   invoke-static {p0, p1, p3}, Landroid/util/apk/ApkSignatureVerifier;->verifyV1Signature(Landroid/content/pm/parsing/result/ParseInput;Ljava/lang/String;Z)Landroid/content/pm/parsing/result/ParseResult;
   ```  
   **Above it, add:**  
   ```
   const/4 p3, 0x0
   ```  
   **Done**

---

#### **File:** `android.util.apk.ApkSigningBlockUtils`

1. **Search:**  
   ```
   invoke-static {v5, v6}, Ljava/security/MessageDigest;->isEqual([B[B)Z
   ```  
   - After this, change:  
     ```
     move-result v7
     ```  
     **To:**  
     ```
     const/4 v7, 0x1
     ```  
   **Done**

---

#### **File:** `android.util.jar.StrictJarVerifier`

1. **Search for:** `verifyMessageDigest`  
   - **Change the return value to `1`.**  
   **Done**

---

#### **File:** `android.util.jar.StrictJarFile`

1. **Search for:**  
   ```
   invoke-virtual {p0, v5}, Landroid/util/jar/StrictJarFile;->findEntry(Ljava/lang/String;)Ljava/util/zip/ZipEntry;
   ```  
   - After this, delete:  
     ```
     if-eqz v6, :cond_56
     :cond_56
     ```  
   **Done**

---

#### **File:** `com.android.internal.pm.pkg.parsing.ParsingPackageUtils`

1. **Search:**  
   ```
   "<manifest> specifies bad sharedUserId name \""
   ```  
   - Above this, you’ll find `if-eqz v4, :cond_x`.  
   - **Above `if-eqz v4, :cond_x`, add:**  
     ```
     const/4 v4, 0x0
     ```  
   **Done**

---