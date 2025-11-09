import os
import json
import threading
from vosk import Model, KaldiRecognizer
import pyaudio
from datetime import datetime
from voice import Voice
from addfunc import addfunc

class RealTimeSpeechRecognizer:
    def __init__(self, model_path):
        # 检查模型是否存在
        if not os.path.exists(model_path):
            print(f'❌ 模型不存在，请到vosk官网下载语言模型 https://alphacephei.com/vosk/models/vosk-model-cn-0.22.zip')
            print(f"❌ 模型路径不存在: {model_path}")
            return

        # 加载语音识别模型
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)
        # 初始化PyAudio
        self.p = pyaudio.PyAudio()
        # 录音状态控制
        self.recording = False
        self.lock = threading.Lock()
        # 识别结果存储
        self.recognized_text = ""
        self.full_transcript = []
        # 结束关键词
        self.END_KEYWORDS = ["结束", "停止", "退出"]
        self.v = Voice()
        print("✅ 语音识别系统初始化完成")

    def start_recognition(self):
        """开始实时语音识别"""
        with self.lock:
            self.recording = True
        print("🎙️ 语音助手已开启，等待您的指令...")
        # 打开音频流
        stream = self.p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=4000
        )
        stream.start_stream()

        try:
            while True:
                with self.lock:
                    if not self.recording:
                        break

                # 读取音频数据
                data = stream.read(4000, exception_on_overflow=False)

                if self.recognizer.AcceptWaveform(data):
                    # 获取完整识别结果
                    result = json.loads(self.recognizer.Result())
                    text = result.get("text", "").strip()

                    if text:
                        self.recognized_text = text
                        timestamp = datetime.now().strftime("%H:%M:%S")
                        self.full_transcript.append(f"[{timestamp}] {text}")

                        # 实时显示识别结果
                        print(f"📝 识别结果: {text}")
                        addfunc(text)

                        # 检查是否包含结束关键词
                        if any(keyword in text for keyword in self.END_KEYWORDS):
                            self.v.speak('好的主人，已退出')
                            print("⏹️ 检测到结束关键词，停止录音")
                            self.stop_recognition()

                else:
                    # 获取部分识别结果（实时反馈）
                    partial_result = json.loads(self.recognizer.PartialResult())
                    partial_text = partial_result.get("partial", "").strip()

                    if partial_text:
                        # 实时显示正在识别的内容
                        print(f"⏳ 正在识别: {partial_text}", end='\r')

        except Exception as e:
            print(f"❌ 录音过程中出现错误: {e}")
        finally:
            stream.stop_stream()
            stream.close()

    def continue_recognition(self):
        """开始实时语音识别"""
        with self.lock:
            self.recording = True
        print("🎙️ 语音助手已开启，等待您的指令...")
        # 打开音频流
        stream = self.p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=4000
        )
        stream.start_stream()

        try:
            while True:
                with self.lock:
                    if not self.recording:
                        break

                # 读取音频数据
                data = stream.read(4000, exception_on_overflow=False)

                if self.recognizer.AcceptWaveform(data):
                    # 获取完整识别结果
                    result = json.loads(self.recognizer.Result())
                    text = result.get("text", "").strip()

                    if text:
                        self.recognized_text = text
                        timestamp = datetime.now().strftime("%H:%M:%S")
                        self.full_transcript.append(f"[{timestamp}] {text}")

                        # 实时显示识别结果
                        print(f"📝 识别结果: {text}")
                        addfunc(text)

                        # 检查是否包含结束关键词
                        if any(keyword in text for keyword in self.END_KEYWORDS):
                            self.v.speak('好的主人，已退出')
                            print("⏹️ 检测到结束关键词，停止录音")
                            self.stop_recognition()

                else:
                    # 获取部分识别结果（实时反馈）
                    partial_result = json.loads(self.recognizer.PartialResult())
                    partial_text = partial_result.get("partial", "").strip()

                    if partial_text:
                        # 实时显示正在识别的内容
                        print(f"⏳ 正在识别: {partial_text}", end='\r')

        except Exception as e:
            print(f"❌ 录音过程中出现错误: {e}")
        finally:
            stream.stop_stream()
            stream.close()

    def stop_recognition(self):
        """停止语音识别"""
        with self.lock:
            self.recording = False
        self.v.speak('助手已下线，随时等待主人的召唤')

    def save_transcript(self, filename="transcript.txt"):
        """保存完整的识别记录"""
        try:
            pass
            # with open(filename, "w", encoding="utf-8") as f:
            #     f.write("=== 语音识别转录记录 ===\n")
            #     f.write(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n"}")
            #     f.write("=" * 50 + "\n\n")
            #
            #     for line in self.full_transcript:
            #         f.write(line + "\n")
            #
            #     print(f"✅ 转录记录已保存至: {filename}")

        except Exception as e:
            print(f"❌ 保存转录记录失败: {e}")

    def keyboard_listener(self):
        """键盘监听线程"""

        pass

    def run(self):
        print("=" * 60)
        print("🎯 实时中文语音识别系统")
        print("=" * 60)
        print("功能说明:")
        print("  • 说出 '结束'、'停止'、'退出' 自动停止")
        print("-" * 60)
        self.v.speak('主人您好，语音助手启动成功')
        # 启动键盘监听线程
        keyboard_thread = threading.Thread(target=self.keyboard_listener)
        keyboard_thread.daemon = True
        keyboard_thread.start()

        # 开始语音识别
        self.start_recognition()
        # 保存识别结果
        if self.full_transcript:
            output_filename = f"transcript_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            self.save_transcript(output_filename)
            print(f"\n📊 识别统计:")
            print(f"  • 总识别段落: {len(self.full_transcript)}")
            print(f"  • 最后识别内容: {self.recognized_text}")

        else:
            print("❌ 未识别到任何语音内容")
recognizer = None
def main():
    # 模型路径设置（根据实际情况修改）
    global recognizer
    model_path = "./vosk-model-cn-0.22"  # 中文模型目录
    recognizer = RealTimeSpeechRecognizer(model_path)
    recognizer.run()


if __name__ == "__main__":
    main()
