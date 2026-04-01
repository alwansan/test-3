import threading
import time
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.utils import platform

# استيراد ملفك لتشغيله
import B_Ultra_v14

class MainApp(App):
    def build(self):
        # تشغيل سيرفر Flask الخاص بك في مسار منفصل (Thread)
        threading.Thread(target=self.start_flask, daemon=True).start()
        
        # الانتظار ثانية لضمان اشتغال السيرفر
        time.sleep(1)
        
        # إذا كنا على أندرويد، افتح WebView
        if platform == 'android':
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            WebView = autoclass('android.webkit.WebView')
            WebViewClient = autoclass('android.webkit.WebViewClient')
            activity = PythonActivity.mActivity
            
            webview = WebView(activity)
            webview.getSettings().setJavaScriptEnabled(True)
            webview.setWebViewClient(WebViewClient())
            webview.loadUrl("http://localhost:8000")
            
            activity.setContentView(webview)
        
        return Widget() # إرجاع واجهة فارغة (لن تظهر لأن الـ WebView سيغطيها)

    def start_flask(self):
        # تشغيل تطبيق Flask
        B_Ultra_v14.app.run(host='0.0.0.0', port=8000, debug=False, use_reloader=False)

if __name__ == '__main__':
    MainApp().run()