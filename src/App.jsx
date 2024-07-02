import { useState, useRef } from 'react';
import './App.css';
import { Octokit } from "https://esm.sh/@octokit/core";

const App = () => {
  const [frameworkJarUrl, setFrameworkJarUrl] = useState('');
  const [servicesJarUrl, setServicesJarUrl] = useState('');
  const [miuiServicesJarUrl, setMiuiServicesJarUrl] = useState('');
  const [miuiFrameworkJarUrl, setMiuiFrameworkJarUrl] = useState('');
  const [androidApiLevel, setAndroidApiLevel] = useState('34');
  const [corePatch, setCorePatch] = useState('apply');
  const [customDeviceName, setCustomDeviceName] = useState('');
  const [customVersion, setCustomVersion] = useState('');

  const formRef = useRef(null);
  const GITHUB_TOKEN = import.meta.env.VITE_GITHUB_TOKEN;
  const REPO_OWNER = 'Jefino9488';
  const REPO_NAME = 'FrameworkPatcher';
  const WORKFLOW_ID = 'patcher.yml';

  const octokit = new Octokit({
    auth: GITHUB_TOKEN
  });

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await octokit.request('POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches', {
        owner: REPO_OWNER,
        repo: REPO_NAME,
        workflow_id: WORKFLOW_ID,
        ref: 'main',
        inputs: {
          framework_jar_url: frameworkJarUrl,
          services_jar_url: servicesJarUrl,
          miui_services_jar_url: miuiServicesJarUrl,
          miui_framework_jar_url: miuiFrameworkJarUrl,
          android_api_level: androidApiLevel,
          core_patch: corePatch,
          custom_device_name: customDeviceName,
          custom_version: customVersion
        }
      });

      if (response.status === 204) {
        window.alert('Build started! Wait for 5 - 10 minutes and check the releases page.');
        setFrameworkJarUrl('');
        setServicesJarUrl('');
        setMiuiServicesJarUrl('');
        setMiuiFrameworkJarUrl('');
        setAndroidApiLevel('34');
        setCorePatch('apply');
        setCustomDeviceName('');
        setCustomVersion('');
      } else {
        console.error('Error triggering GitHub Action:', response.status);
      }
    } catch (error) {
      console.error('Error triggering GitHub Action:', error);
    }
  };

  const handleRedirect = () => {
    window.open('https://github.com/Jefino9488/FrameworkPatcher/releases', '_blank');
  };

  const handleRedirectBuild = () => {
    window.open('https://github.com/Jefino9488/FrameworkPatcher/actions/workflows/patcher.yml', '_blank');
  };

  return (
      <div id="root">
          <h1 id="h">Modify Framework and Services</h1>
          <br/>
          <form ref={formRef} onSubmit={handleSubmit}>
              <div>
                  <h2>JAR URLs</h2>
                  <label htmlFor="framework-jar-url-input">Framework JAR URL:</label>
                  <input type="url" id="framework-jar-url-input" value={frameworkJarUrl}
                         onChange={(e) => setFrameworkJarUrl(e.target.value)} required/>

                  <label htmlFor="services-jar-url-input">Services JAR URL:</label>
                  <input type="url" id="services-jar-url-input" value={servicesJarUrl}
                         onChange={(e) => setServicesJarUrl(e.target.value)} required/>

                  <label htmlFor="miui-services-jar-url-input">MIUI Services JAR URL:</label>
                  <input type="url" id="miui-services-jar-url-input" value={miuiServicesJarUrl}
                         onChange={(e) => setMiuiServicesJarUrl(e.target.value)} required/>

                  <label htmlFor="miui-framework-jar-url-input">MIUI Framework JAR URL:</label>
                  <input type="url" id="miui-framework-jar-url-input" value={miuiFrameworkJarUrl}
                         onChange={(e) => setMiuiFrameworkJarUrl(e.target.value)} required/>
              </div>

              <div>
                  <h2>Additional Settings</h2>
                  <label htmlFor="android-api-level-input">Android API Level:</label>
                  <input type="number" id="android-api-level-input" value={androidApiLevel}
                         onChange={(e) => setAndroidApiLevel(e.target.value)} required/>

                  <label htmlFor="core-patch-select">Core Patch:</label>
                  <select id="core-patch-select" value={corePatch} onChange={(e) => setCorePatch(e.target.value)}
                          required>
                      <option value="apply">Apply</option>
                      <option value="do_not_apply">Do Not Apply</option>
                  </select>

                  <label htmlFor="custom-device-name-input">Custom Device Name (optional):</label>
                  <input type="text" id="custom-device-name-input" value={customDeviceName}
                         onChange={(e) => setCustomDeviceName(e.target.value)}/>

                  <label htmlFor="custom-version-input">Custom Version (optional):</label>
                  <input type="text" id="custom-version-input" value={customVersion}
                         onChange={(e) => setCustomVersion(e.target.value)}/>
              </div>
          </form>
          <div>
              <button type="submit">Start Build</button>
          </div>
          <p>All builds are available on the releases page</p>
          <div id="root1">
              <button onClick={handleRedirect}>Go to releases</button>
              <button onClick={handleRedirectBuild}>Build Status</button>
          </div>
      </div>
  );
};

export default App;
