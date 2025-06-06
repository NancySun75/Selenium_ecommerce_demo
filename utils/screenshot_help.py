import os

def take_screenshot(driver, filename):
    # 获取当前脚本的上一级目录（你的项目根目录）
    base_dir = os.path.dirname(os.path.dirname(__file__))

    # 拼接 data 文件夹路径
    data_dir = os.path.join(base_dir, "screenshot")


    # 拼接完整文件路径
    full_path = os.path.join(data_dir, filename)

    # 截图并保存
    driver.save_screenshot(full_path)
    print(f"📸 截图已保存到: {full_path}")
