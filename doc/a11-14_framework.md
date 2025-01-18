### **Modifications to framework.jar**

#### **File:** `classes3/android/util/apk/ApkSignatureVerifier.smali`  
**Method:** `getMinimumSignatureSchemeVersionForTargetSdk`  
- Change the return value to `0`. **Done**

---

#### **File:** `classes3/android/util/jar/StrictJarVerifier.smali`  
**Method:** `verifyMessageDigest`  
- Change the return value to `1`. **Done**

---

### **Modify isError Check**  
#### **File:** `classes3/android/util/apk/ApkSignatureVerifier.smali`  
**Method:** `verifySignatures`  
1. Find:  
   ```
   invoke-interface {v0}, Landroid/content/pm/parsing/result/ParseResult;->isError()Z
   move-result v1
   ```
2. Add the following code directly under it:  
   ```
   const/4 v1, 0x0
   ```  
**Done**

---

### **Add p3 Assignments**

1. **Search:**  
   ```
   invoke-static {p0, p1, p3}, Landroid/util/apk/ApkSignatureVerifier;->verifyV1Signature(Landroid/content/pm/parsing/result/ParseInput;Ljava/lang/String;Z)Landroid/content/pm/parsing/result/ParseResult;
   ```  
   **Above it, add:**  
   ```
   const/4 p3, 0x0
   ```  
   **Done**

2. **Search:**  
   ```
   invoke-static {p0, p1, p3}, Landroid/util/apk/ApkSignatureVerifier;->verifyV2Signature(Landroid/content/pm/parsing/result/ParseInput;Ljava/lang/String;Z)Landroid/content/pm/parsing/result/ParseResult;
   ```  
   **Above it, add:**  
   ```
   const/4 p3, 0x0
   ```  
   **Done**

3. **Search:**  
   ```
   invoke-static {p0, p1, p3}, Landroid/util/apk/ApkSignatureVerifier;->verifyV3Signature(Landroid/content/pm/parsing/result/ParseInput;Ljava/lang/String;Z)Landroid/content/pm/parsing/result/ParseResult;
   ```  
   **Above it, add:**  
   ```
   const/4 p3, 0x0
   ```  
   **Done**

4. **Search:**  
   ```
   invoke-static {p0, p1, p2, p3}, Landroid/util/apk/ApkSignatureVerifier;->verifyV3AndBelowSignatures(Landroid/content/pm/parsing/result/ParseInput;Ljava/lang/String;IZ)Landroid/content/pm/parsing/result/ParseResult;
   ```  
   **Above it, add:**  
   ```
   const/4 p3, 0x0
   ```  
   **Done**

5. **Search:**  
   ```
   invoke-static {p0, p1, p2, p3}, Landroid/util/apk/ApkSignatureVerifier;->verifyV4Signature(Landroid/content/pm/parsing/result/ParseInput;Ljava/lang/String;IZ)Landroid/content/pm/parsing/result/ParseResult;
   ```  
   **Above it, add:**  
   ```
   const/4 p3, 0x0
   ```  
   **Done**

---

### **PackageParser and SigningDetails Modifications**

#### **Files:**  
- `classes/android/content/pm/PackageParser$SigningDetails.smali`  
- `classes/android/content/pm/SigningDetails.smali`  

1. **Method:** `checkCapability`  
   - Change the return value to `1`. **Done**

2. **Method:** `checkCapabilityRecover`  
   - Change the return value to `1`. **Done**

---

### **ApplicationInfo Modification**

#### **File:** `classes/android/content/pm/ApplicationInfo.smali`  
**Method:** `isPackageWhitelistedForHiddenApis`  
- Change the return value to `1`. **Done**

---

### **StrictJarFile Modifications**

#### **Class:** `android.util.jar.StrictJarFile`  
1. **Search:**  
   ```
   invoke-virtual {p0, v5}, Landroid/util/jar/StrictJarFile;->findEntry(Ljava/lang/String;)Ljava/util/zip/ZipEntry;
   move-result-object v6
   ```  
2. **Delete the following:**  
   ```
   if-eqz v6, :cond_52
   :cond_52
   ```  
**Done**
