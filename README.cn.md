# MacOS极简本地图床

这个项目是一个专为macOS设计的极简本地图床解决方案。它利用[Flask](https://flask.palletsprojects.com)通过网络映射图片，并通过[rumps](https://github.com/jaredks/rumps)无缝集成至macOS菜单栏。

![](./img/Screenshot%202024-03-18%20at%2018.17.18.png)

功能：
- 支持多图库管理

- 剪贴板监控：自动保存复制到剪贴板的图片，简化图片上传过程。

- URL复制：图片保存后，图片的URL立即复制到剪贴板，便于分享或在其他地方嵌入图片。

这个图床解决方案提供一种直接且高效的本地管理和分享图片的方法，适合用于Markdowns或Obsidian等。

## 安装

1. 安装Python
2. 如果需要，构建Python环境（可选）
3. 克隆仓库

    ```bash
    git clone https://github.com/ErwinLiYH/MiniPicBedMac.git
    cd MiniPicBedMac
    ```

4. 修改__init__.py中的设置

    ```python
    # 图片保存目录
    # 你可以在这里添加和修改图片仓库
    FILES_DIRECTORY = {
    "default": os.path.expanduser('~/mypicbed/'),  # 默认库在~/mypicbed/
    # "其他仓库": "path/to/your/vault"
    }

    # 服务器端口，默认：20119
    PORT = 20119

    # 复制行为：
    # MD复制Markdown代码引用图片
    # URL仅复制图片URL
    # PATH复制图片路径
    # 默认：MD
    COPY_BEVAIOR = "MD"  # "MD", "URL" 或 "PATH"
    ```

5. 安装

    ```bash
    pip install .
    ```

## 使用

1. 运行PicBed

    ```bash
    python -m local_picbed_mac
    ```

2. 复制一个图片
3. 通过点击状态栏应用中的`Selected Vault: xxx`选择保存图片的库（可选）
4. 点击状态栏应用中的`Save Image for Pastedboard`将图片保存到库对应的文件夹
5. 复制自动返回图片的MD/URL/PATH到任何地方