[app]
title = AlarmKu
package.name = alarmku
package.domain = org.phobiakalian
version = 1.0
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
requirements = python3,kivy,plyer

android.permissions = android.permission.INTERNET,android.permission.VIBRATE,android.permission.WAKE_LOCK,android.permission.POST_NOTIFICATIONS
android.api = 33
android.minapi = 21
android.ndk = 25b

# ✅ PIN BUILD-TOOLS VERSION (wajib!)
android.build_tools = 33.0.2

# ✅ Gunakan system SDK path (opsional, tapi membantu)
# android.sdk_path = /usr/local/lib/android/sdk

[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = True