[app]
title = AlarmKu
package.name = alarmku
package.domain = org.phobiakalian  # ✅ Hindari duplikasi package name

version = 1.0
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

requirements = python3,kivy,plyer

android.permissions = android.permission.INTERNET,android.permission.VIBRATE,android.permission.WAKE_LOCK,android.permission.POST_NOTIFICATIONS

android.api = 33
android.minapi = 21
android.ndk = 25b

# ✅ PIN BUILD-TOOLS VERSION (wajib, hindari auto-pick versi 37)
android.build_tools = 33.0.2

[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = True