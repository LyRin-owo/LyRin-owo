"""font_getter.py

该 module 用于从 GitHub 仓库中拉取生成图表所需的字体。
"""

import io
import os
import zipfile
import requests

# 定义下载链接和目标文件名
URL = "https://media.githubusercontent.com/media/huawei-fonts/HarmonyOS-Sans/refs/heads/main/HarmonyOS%20Sans.zip"
TARGET_FILE = "HarmonyOS_Sans_SC_Regular.ttf"


def main():
    """该函数为 font_getter 的主函数。"""

    # 检查目标文件是否已经存在
    if os.path.exists(TARGET_FILE):
        print(f"字体文件 {TARGET_FILE} 已存在，跳过下载。")
        return

    # 下载字体文件
    try:
        response = requests.get(URL, timeout=20)
        if response.status_code == 200:
            with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
                # 查找目标文件并解压到当前目录
                for member in zip_ref.namelist():
                    if member.endswith(TARGET_FILE):
                        zip_ref.extract(member)
                        # 移动文件到当前目录
                        extracted_path = os.path.join(os.getcwd(), member)
                        target_path = os.path.join(os.getcwd(), TARGET_FILE)
                        os.rename(extracted_path, target_path)
                        print(f"成功解压 {TARGET_FILE} 到当前目录。")
                        break
        else:
            print(f"下载失败。错误码为 {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"请求过程中发生错误: {e}")


if __name__ == "__main__":
    main()
