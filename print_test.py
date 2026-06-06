import subprocess

def print_text_unix(text):
    try:
        # 使用 lp 命令，'-' 表示从标准输入（stdin）接收文本内容
        process = subprocess.Popen(['lp'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=text)
        
        if process.returncode == 0:
            print("已发送至打印机队列")
        else:
            print(f"打印失败: {stderr}")
    except FileNotFoundError:
        print("错误：未找到 'lp' 命令，请确保系统已安装并配置 CUPS 打印服务。")

# 测试调用
print_text_unix("你好，这是由 Python 自动调用默认打印机打印的一段话。")