import { useState, useRef } from 'react'
import { Octokit } from "https://esm.sh/@octokit/core";
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Button } from "@/components/ui/button"
import { AlertCircle, Download, GitBranch } from 'lucide-react'
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"

const App = () => {
  const [frameworkJarUrl, setFrameworkJarUrl] = useState('')
  const [servicesJarUrl, setServicesJarUrl] = useState('')
  const [miuiServicesJarUrl, setMiuiServicesJarUrl] = useState('')
  const [miuiFrameworkJarUrl, setMiuiFrameworkJarUrl] = useState('')
  const [androidApiLevel, setAndroidApiLevel] = useState('34')
  const [core, setCore] = useState('true')
  const [customDeviceName, setCustomDeviceName] = useState('')
  const [customVersion, setCustomVersion] = useState('')
  const [isCN, setIsCN] = useState('true')

  const formRef = useRef(null)
  const GITHUB_TOKEN = import.meta.env.VITE_GITHUB_TOKEN;
  const REPO_OWNER = 'Jefino9488'
  const REPO_NAME = 'FrameworkPatcher'
  const WORKFLOW_ID = 'patcher.yml'

  const octokit = new Octokit({
    auth: GITHUB_TOKEN
  })

  const isDumpUrl = (url) => {
    return url.startsWith('https://dumps.tadiphone.dev/dumps/') ||
           url === 'https://drive.usercontent.google.com/download?id=1-CQY_wMkr3SSlA7DTJPCjzVoNIjWtOcR&export=download&authuser=0';
  };

  const isBlockedUrl = (url) => {
    return url.startsWith('https://www.mediafire.com/') ||
           (url.startsWith('https://drive.google.com/') && !url.includes('/view?')) ||
           url.startsWith('https://drive.google.com/file/d/') ||
           url.startsWith('https://drive.google.com/uc?') ||
           url.startsWith('https://drive.google.com/open?id=') ||
           url.startsWith('https://drive.proton.me/');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (isBlockedUrl(frameworkJarUrl) || isBlockedUrl(servicesJarUrl) || isBlockedUrl(miuiServicesJarUrl) || isBlockedUrl(miuiFrameworkJarUrl)) {
      window.alert('The provided URL is not allowed.');
      return;
    }

    let deviceName = customDeviceName;
    let version = customVersion;

    if (frameworkJarUrl.startsWith('https://dumps.tadiphone.dev/dumps/')) {
      if (!customVersion) {
        const versionMatch = frameworkJarUrl.match(/V([^/]+)\/system/);
        if (versionMatch) {
          version = versionMatch[1];
        }
      }

      if (!customDeviceName) {
        const deviceNameMatch = frameworkJarUrl.match(/redmi\/([^/]+)\/-/);
        if (deviceNameMatch) {
          deviceName = deviceNameMatch[1];
        }
      }

      try {
        const releasesResponse = await octokit.request('GET /repos/{owner}/{repo}/releases', {
          owner: REPO_OWNER,
          repo: REPO_NAME
        });

        const releases = releasesResponse.data;
        const matchingRelease = releases.find(release => release.name === `moded_${deviceName}_${version}`);

        if (matchingRelease) {
          window.alert('Build already exists for this device and version. Opening releases page.');
          window.open(matchingRelease.html_url, '_blank');
          return;
        }

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
            core: core,
            custom_device_name: deviceName,
            custom_version: version,
            isCN: isCN
          }
        });

        if (response.status === 204) {
          window.alert('Build started! Wait for 5 - 10 minutes and check the releases page.');
          setFrameworkJarUrl('');
          setServicesJarUrl('');
          setMiuiServicesJarUrl('');
          setMiuiFrameworkJarUrl('');
          setAndroidApiLevel('34');
          setCore('true');
          setCustomDeviceName('');
          setCustomVersion('');
          setIsCN('true');
        } else {
          console.error('Error triggering GitHub Action:', response.status);
        }
      } catch (error) {
        console.error('Error triggering GitHub Action:', error);
      }
    } else {
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
            core: core,
            custom_device_name: customDeviceName,
            custom_version: customVersion,
            isCN: isCN
          }
        });

        if (response.status === 204) {
          window.alert('Build started! Wait for 5 - 10 minutes and check the releases page.');
          setFrameworkJarUrl('');
          setServicesJarUrl('');
          setMiuiServicesJarUrl('');
          setMiuiFrameworkJarUrl('');
          setAndroidApiLevel('34');
          setCore('true');
          setCustomDeviceName('');
          setCustomVersion('');
          setIsCN('true');
        } else {
          console.error('Error triggering GitHub Action:', response.status);
        }
      } catch (error) {
        console.error('Error triggering GitHub Action:', error);
      }
    }
  };

  const handleRedirect = () => {
    window.open('https://github.com/Jefino9488/FrameworkPatcher/releases', '_blank');
  };

  const handleRedirectBuild = () => {
    window.open('https://github.com/Jefino9488/FrameworkPatcher/actions/workflows/patcher.yml', '_blank');
  };

  return (
    <div className="bg-[#0d0d0d] min-h-screen text-white">
      <div className="container mx-auto p-4">
        <Card className="bg-[#1a1a1a] text-white border-[#2a2a2a]">
          <CardHeader>
            <CardTitle className="text-2xl font-bold text-center">Modify Framework and Services</CardTitle>
          </CardHeader>
          <CardContent>
            <form ref={formRef} onSubmit={handleSubmit} className="space-y-6">
              <div className="space-y-4">
                <h3 className="text-lg font-semibold text-[#d1d5db]">JAR URLs</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="space-y-2">
                    <Label htmlFor="framework-jar-url-input" className="text-[#d1d5db]">Framework JAR URL</Label>
                    <Input
                      type="url"
                      id="framework-jar-url-input"
                      value={frameworkJarUrl}
                      onChange={(e) => setFrameworkJarUrl(e.target.value)}
                      required
                      className="bg-[#2a2a2a] text-white border-[#3a3a3a] focus:border-[#4a4a4a]"
                    />
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="services-jar-url-input" className="text-[#d1d5db]">Services JAR URL</Label>
                    <Input
                      type="url"
                      id="services-jar-url-input"
                      value={servicesJarUrl}
                      onChange={(e) => setServicesJarUrl(e.target.value)}
                      required
                      className="bg-[#2a2a2a] text-white border-[#3a3a3a] focus:border-[#4a4a4a]"
                    />
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="miui-services-jar-url-input" className="text-[#d1d5db]">MIUI Services JAR URL</Label>
                    <Input
                      type="url"
                      id="miui-services-jar-url-input"
                      value={miuiServicesJarUrl}
                      onChange={(e) => setMiuiServicesJarUrl(e.target.value)}
                      required
                      className="bg-[#2a2a2a] text-white border-[#3a3a3a] focus:border-[#4a4a4a]"
                    />
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="miui-framework-jar-url-input" className="text-[#d1d5db]">MIUI Framework JAR URL</Label>
                    <Input
                      type="url"
                      id="miui-framework-jar-url-input"
                      value={miuiFrameworkJarUrl}
                      onChange={(e) => setMiuiFrameworkJarUrl(e.target.value)}
                      required
                      className="bg-[#2a2a2a] text-white border-[#3a3a3a] focus:border-[#4a4a4a]"
                    />
                  </div>
                </div>
              </div>

              <div className="space-y-4">
                <h3 className="text-lg font-semibold text-[#d1d5db]">Additional Settings</h3>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  <div className="space-y-2">
                    <Label htmlFor="android-api-level-input" className="text-[#d1d5db]">Android Version</Label>
                    <Select value={androidApiLevel} onValueChange={setAndroidApiLevel}>
                      <SelectTrigger id="android-api-level-input" className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectValue placeholder="Select API Level" />
                      </SelectTrigger>
                      <SelectContent className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectItem value="34">14</SelectItem>
                        <SelectItem value="35">15</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="core-select" className="text-[#d1d5db]">Core Patch</Label>
                    <Select value={core} onValueChange={setCore}>
                      <SelectTrigger id="core-select" className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectValue placeholder="Select Core Patch" />
                      </SelectTrigger>
                      <SelectContent className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectItem value="true">Apply</SelectItem>
                        <SelectItem value="false">Do Not Apply</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="is-cn-select" className="text-[#d1d5db]">Is CN</Label>
                    <Select value={isCN} onValueChange={setIsCN}>
                      <SelectTrigger id="is-cn-select" className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectValue placeholder="Select Is CN" />
                      </SelectTrigger>
                      <SelectContent className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectItem value="true">True</SelectItem>
                        <SelectItem value="false">False</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                </div>

                {!isDumpUrl(frameworkJarUrl) && (
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="space-y-2">
                      <Label htmlFor="custom-device-name-input" className="text-[#d1d5db]">Custom Device Name</Label>
                      <Input
                        type="text"
                        id="custom-device-name-input"
                        value={customDeviceName}
                        onChange={(e) => setCustomDeviceName(e.target.value)}
                        required
                        placeholder="xaga"
                        className="bg-[#2a2a2a] text-white border-[#3a3a3a] focus:border-[#4a4a4a]"
                      />
                    </div>
                    <div className="space-y-2">
                      <Label htmlFor="custom-version-input" className="text-[#d1d5db]">Custom Version</Label>
                      <Input
                        type="text"
                        id="custom-version-input"
                        value={customVersion}
                        onChange={(e) => setCustomVersion(e.target.value)}
                        required
                        placeholder="V14.0.8.0.TKHCNXM"
                        className="bg-[#2a2a2a] text-white border-[#3a3a3a] focus:border-[#4a4a4a]"
                      />
                    </div>
                  </div>
                )}
              </div>

              <Button type="submit" className="w-full bg-[#3a3a3a] text-white hover:bg-[#4a4a4a]">Start Build</Button>
            </form>
          </CardContent>
          <CardFooter className="flex flex-col items-center space-y-4">
            <Alert className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
              <AlertCircle className="h-4 w-4" />
              <AlertTitle>Note</AlertTitle>
              <AlertDescription>
                All builds are available on the releases page
              </AlertDescription>
            </Alert>
            <div className="flex space-x-4">
              <Button onClick={handleRedirect} variant="outline" className="bg-[#2a2a2a] hover:bg-[#3a3a3a] text-white border-[#3a3a3a]">
                <Download className="mr-2 h-4 w-4" /> Go to releases
              </Button>
              <Button onClick={handleRedirectBuild} variant="outline" className="bg-[#2a2a2a] hover:bg-[#3a3a3a] text-white border-[#3a3a3a]">
                <GitBranch className="mr-2 h-4 w-4" /> Build Status
              </Button>
            </div>
          </CardFooter>
        </Card>
      </div>
    </div>
  )
}

export default App

