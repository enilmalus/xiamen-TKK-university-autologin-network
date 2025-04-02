### 只测试了电信，可自动登入电信校园网

### 需要电脑拥有python环境，安装requests库

### 将py文件中参数填充完整，bat文件将路径改为py件实际路径

## 关于开机自启动的几种可能的方法

### 第一种

#### 开机自启动

按 Win + R，输入 taskschd.msc 打开任务计划程序。
点击右侧的 创建任务。
在 常规 选项卡中，填写任务名称AutomaticLogin，并勾选 使用最高权限运行。
在 触发器 选项卡中，点击 新建，选择 启动/登入时时。
在 操作 选项卡中，点击 新建，选择 启动程序，并选择刚才创建的 Autologin.bat 文件。
保存任务。

按 Win + R，输入以下命令并回车：

`shell:startup`

导航到你的 .bat 文件所在的路径，例如：e:\GitHub Study\automatic login\Autologin.bat。
打开启动文件夹：
将 Autologin.bat 文件从源文件夹拖放到启动文件夹中。
如果提示需要管理员权限，点击 继续。

#### 取消开机自启动

按 Win + R，输入 taskschd.msc 打开任务计划程序。
在左侧导航栏中，找到 任务计划程序库。
找到你之前创建的任务 AutomaticLogin。
右键点击任务，选择 删除。

