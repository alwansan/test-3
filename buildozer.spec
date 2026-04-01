[app]
title = B-Ultra
package.name = bultra
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

# إصدار التطبيق
version = 1.0

# المكاتب التي يحتاجها تطبيقك (سيتم دمج بايثون معها)
requirements = python3, kivy, flask, yt-dlp, pyjnius

# صلاحيات الأندرويد المطلوبة (مهم جداً للإنترنت وتحميل الملفات)
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# دعم المعماريات الحديثة للهواتف
android.archs = arm64-v8a, armeabi-v7a

# منع إطفاء الشاشة أو إغلاق التطبيق أثناء التحميل
android.wakelock = True