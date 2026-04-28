[app]
title = AlarmKu
package.name = alarmku
package.domain = org.phobiakalian.alarmku

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0
requirements = python3,kivy,plyer

[buildozer]
log_level = 2

[app]
android.permissions = INTERNET,VIBRATE,WAKE_LOCK

android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33

[buildozer]
android.accept_sdk_license = True