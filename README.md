按 Win + R，输入 taskschd.msc 打开任务计划程序。
点击右侧的 创建任务。
在 常规 选项卡中，填写任务名称（如 AutomaticLogin），并勾选 使用最高权限运行。
在 触发器 选项卡中，点击 新建，选择 在登录时。
在 操作 选项卡中，点击 新建，选择 启动程序，并选择刚才创建的 start_login.bat 文件。
保存任务。

按 Win + R，输入 taskschd.msc 打开任务计划程序。
在左侧导航栏中，找到 任务计划程序库。
找到你之前创建的任务（例如 AutomaticLogin）。
右键点击任务，选择 删除。# xiamen-TKK-university-autologin-network
