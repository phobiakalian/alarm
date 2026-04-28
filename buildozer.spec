[app]
title = AlarmKu
package.name = alarmku
package.domain = org.phobiakalian.alarmku
package.version = 1.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0
requirements = python3,kivy,plyer

android.permissions = INTERNET,VIBRATE,WAKE_LOCK,POST_NOTIFICATIONS

android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33

[buildozer]
log_level = 2
warn_on_root = 1

android.accept_sdk_license = True