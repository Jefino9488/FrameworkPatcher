import { useState, useRef } from 'react';
import { Octokit } from 'https://esm.sh/@octokit/core';
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Button } from '@/components/ui/button';
import { AlertCircle, Download, GitBranch, Info } from 'lucide-react';
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert';
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/components/ui/tooltip';

const App = () => {
  const [frameworkJarUrl, setFrameworkJarUrl] = useState('');
  const [servicesJarUrl, setServicesJarUrl] = useState('');
  const [miuiServicesJarUrl, setMiuiServicesJarUrl] = useState('');
  const [miuiFrameworkJarUrl, setMiuiFrameworkJarUrl] = useState('');
  const [androidApiLevel, setAndroidApiLevel] = useState('34');
  const [isCN, setIsCN] = useState('true');
  const [defaultcore, setDefaultCore] = useState('true');
  const [core, setCore] = useState('false');
  const [fixNotification, setFixNotification] = useState('true');
  const [addGboard, setAddGboard] = useState('false');
  const [disableFlagSecure, setDisableFlagSecure] = useState('true');
  const [multiFloatingWindow, setMultiFloatingWindow] = useState('true');
  const [customDeviceName, setCustomDeviceName] = useState('');
  const [customVersion, setCustomVersion] = useState('');
  const formRef = useRef(null);
  const GITHUB_TOKEN = import.meta.env.VITE_GITHUB_TOKEN;
  const REPO_OWNER = 'Jefino9488';
  const REPO_NAME = 'FrameworkPatcher';
  const WORKFLOW_ID = 'patcher.yml';
  const octokit = new Octokit({
    auth: GITHUB_TOKEN,
  });
  const isBlockedUrl = (url) => {
    const allowedDomains = [
      'https://github.com/',
      'https://drive.google.com/',
      'https://dumps.tadiphone.dev/dumps/',
      'https://www.tgxlink.workers.dev/',
      'https://publicbotshub.blogspot.com/',
    ];
    return !allowedDomains.some((domain) => url.startsWith(domain));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (
      isBlockedUrl(frameworkJarUrl) ||
      isBlockedUrl(servicesJarUrl) ||
      isBlockedUrl(miuiServicesJarUrl) ||
      isBlockedUrl(miuiFrameworkJarUrl)
    ) {
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
    }

    const jarUrls = {
      framework_jar_url: frameworkJarUrl,
      services_jar_url: servicesJarUrl,
      miui_services_jar_url: miuiServicesJarUrl,
      miui_framework_jar_url: miuiFrameworkJarUrl,
    };

    const features = {
      isCN: isCN,
      defaultcore: defaultcore,
      core: core,
      fixNotification: fixNotification,
      addGboard: addGboard,
      disableFlagSecure: disableFlagSecure,
      multiFloatingWindow: multiFloatingWindow,
    };

    const jarUrlsJson = JSON.stringify(jarUrls);
    const featuresJson = JSON.stringify(features);

    try {
      const response = await octokit.request('POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches', {
        owner: REPO_OWNER,
        repo: REPO_NAME,
        workflow_id: WORKFLOW_ID,
        ref: 'main',
        inputs: {
          jar_urls: jarUrlsJson,
          android_api_level: androidApiLevel,
          features: featuresJson,
          custom_device_name: deviceName,
          custom_version: version,
        },
      });

      if (response.status === 204) {
        window.alert('Build started! Wait for 5 - 10 minutes and check the releases page.');
        setFrameworkJarUrl('');
        setServicesJarUrl('');
        setMiuiServicesJarUrl('');
        setMiuiFrameworkJarUrl('');
        setAndroidApiLevel('34');
        setIsCN('true');
        setDefaultCore('true');
        setCore('false');
        setFixNotification('true');
        setAddGboard('false');
        setDisableFlagSecure('true');
        setMultiFloatingWindow('true');
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

  const handleDeviceNameChange = (e) => {
    const value = e.target.value;
    if (/^[A-Za-z]*$/.test(value)) {
      setCustomDeviceName(value);
    }
  };


  const handleVersionChange = (e) => {
    const value = e.target.value;
    if (/^[A-Za-z0-9.]*$/.test(value) && !value.match(/\.{2,}/)) {
      setCustomVersion(value);
    }
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
              {/* JAR URLs Section */}
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

              {/* Additional Settings Section */}
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
                        <SelectItem value="33">13</SelectItem>
                        <SelectItem value="34">14</SelectItem>
                        <SelectItem value="35">15</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                  <div className="space-y-2">
                    <div className="flex items-center space-x-2">
                      <Label htmlFor="is-cn-select" className="text-[#d1d5db]">Is CN</Label>
                      <TooltipProvider>
                        <Tooltip>
                          <TooltipTrigger asChild>
                            <Info className="h-4 w-4 text-gray-400" />
                          </TooltipTrigger>
                          <TooltipContent>
                            <p>Determines if the build is for the Chinese version</p>
                          </TooltipContent>
                        </Tooltip>
                      </TooltipProvider>
                    </div>
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
                  <div className="space-y-2">
                    <div className="flex items-center space-x-2">
                      <Label htmlFor="defaultcore-select" className="text-[#d1d5db]">Default Core</Label>
                      <TooltipProvider>
                        <Tooltip>
                          <TooltipTrigger asChild>
                            <Info className="h-4 w-4 text-gray-400" />
                          </TooltipTrigger>
                          <TooltipContent>
                            <p>Applies system level core patch (disables system app verification)</p>
                          </TooltipContent>
                        </Tooltip>
                      </TooltipProvider>
                    </div>
                    <Select value={defaultcore} onValueChange={setDefaultCore}>
                      <SelectTrigger id="defaultcore-select" className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectValue placeholder="Select Default Core" />
                      </SelectTrigger>
                      <SelectContent className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectItem value="true">True</SelectItem>
                        <SelectItem value="false">False</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                  <div className="space-y-2">
                    <div className="flex items-center space-x-2">
                      <Label htmlFor="core-select" className="text-[#d1d5db]">Core Patch</Label>
                      <TooltipProvider>
                        <Tooltip>
                          <TooltipTrigger asChild>
                            <Info className="h-4 w-4 text-gray-400" />
                          </TooltipTrigger>
                          <TooltipContent>
                            <p>Fully disables signature verification (needs default core)</p>
                          </TooltipContent>
                        </Tooltip>
                      </TooltipProvider>
                    </div>
                    <Select value={core} onValueChange={setCore}>
                      <SelectTrigger id="core-select" className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectValue placeholder="Select Core Patch" />
                      </SelectTrigger>
                      <SelectContent className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectItem value="true">True</SelectItem>
                        <SelectItem value="false">False</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                  <div className="space-y-2">
                    <div className="flex items-center space-x-2">
                      <Label htmlFor="fix-notification-select" className="text-[#d1d5db]">Fix Notification</Label>
                      <TooltipProvider>
                        <Tooltip>
                          <TooltipTrigger asChild>
                            <Info className="h-4 w-4 text-gray-400" />
                          </TooltipTrigger>
                          <TooltipContent>
                            <p>Reduce notification problem on cn roms</p>
                          </TooltipContent>
                        </Tooltip>
                      </TooltipProvider>
                    </div>
                    <Select value={fixNotification} onValueChange={setFixNotification}>
                      <SelectTrigger id="fix-notification-select" className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectValue placeholder="Select Fix Notification" />
                      </SelectTrigger>
                      <SelectContent className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectItem value="true">True</SelectItem>
                        <SelectItem value="false">False</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                  <div className="space-y-2">
                    <div className="flex items-center space-x-2">
                      <Label htmlFor="add-gboard-select" className="text-[#d1d5db]">Add Gboard</Label>
                      <TooltipProvider>
                        <Tooltip>
                          <TooltipTrigger asChild>
                            <Info className="h-4 w-4 text-gray-400" />
                          </TooltipTrigger>
                          <TooltipContent>
                            <p>add gboard to enhance keyboard</p>
                          </TooltipContent>
                        </Tooltip>
                      </TooltipProvider>
                    </div>
                    <Select value={addGboard} onValueChange={setAddGboard}>
                      <SelectTrigger id="add-gboard-select" className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectValue placeholder="Select Add Gboard" />
                      </SelectTrigger>
                      <SelectContent className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectItem value="true">True</SelectItem>
                        <SelectItem value="false">False</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                  <div className="space-y-2">
                    <div className="flex items-center space-x-2">
                      <Label htmlFor="disable-flag-secure-select" className="text-[#d1d5db]">Disable Flag Secure</Label>
                      <TooltipProvider>
                        <Tooltip>
                          <TooltipTrigger asChild>
                            <Info className="h-4 w-4 text-gray-400" />
                          </TooltipTrigger>
                          <TooltipContent>
                            <p>Disable the FLAG_SECURE window flag</p>
                          </TooltipContent>
                        </Tooltip>
                      </TooltipProvider>
                    </div>
                    <Select value={disableFlagSecure} onValueChange={setDisableFlagSecure}>
                      <SelectTrigger id="disable-flag-secure-select" className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectValue placeholder="Select Disable Flag Secure" />
                      </SelectTrigger>
                      <SelectContent className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectItem value="true">True</SelectItem>
                        <SelectItem value="false">False</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                  <div className="space-y-2">
                    <div className="flex items-center space-x-2">
                      <Label htmlFor="multi-floating-window-select" className="text-[#d1d5db]">Multi Floating Window</Label>
                      <TooltipProvider>
                        <Tooltip>
                          <TooltipTrigger asChild>
                            <Info className="h-4 w-4 text-gray-400" />
                          </TooltipTrigger>
                          <TooltipContent>
                            <p>Increase limit to 50</p>
                          </TooltipContent>
                        </Tooltip>
                      </TooltipProvider>
                    </div>
                    <Select value={multiFloatingWindow} onValueChange={setMultiFloatingWindow}>
                      <SelectTrigger id="multi-floating-window-select" className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectValue placeholder="Select Multi Floating Window" />
                      </SelectTrigger>
                      <SelectContent className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
                        <SelectItem value="true">True</SelectItem>
                        <SelectItem value="false">False</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                </div>

                {/* Custom Device Name and Version */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="space-y-2">
                    <Label htmlFor="custom-device-name-input" className="text-[#d1d5db]">Device Name</Label>
                    <Input
                        type="text"
                        id="custom-device-name-input"
                        value={customDeviceName}
                        onChange={handleDeviceNameChange}
                        placeholder="Enter device name"
                        className="bg-[#2a2a2a] text-white border-[#3a3a3a] focus:border-[#4a4a4a]"
                    />
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="custom-version-input" className="text-[#d1d5db]">Version</Label>
                    <Input
                        type="text"
                        id="custom-version-input"
                        value={customVersion}
                        onChange={handleVersionChange}
                        placeholder="Enter version"
                        className="bg-[#2a2a2a] text-white border-[#3a3a3a] focus:border-[#4a4a4a]"
                    />
                  </div>

                </div>
              </div>

              {/* Submit Button */}
              <Button type="submit" className="w-full bg-[#3a3a3a] text-white hover:bg-[#4a4a4a]">
                Start Build
              </Button>
            </form>
          </CardContent>
          <CardFooter className="flex flex-col items-center space-y-4">
            <Alert className="bg-[#2a2a2a] text-white border-[#3a3a3a]">
              <AlertCircle className="h-4 w-4" />
              <AlertTitle>Note</AlertTitle>
              <AlertDescription>All builds are available on the releases page</AlertDescription>
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
  );
};

export default App;