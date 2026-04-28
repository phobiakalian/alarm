[app]
title = AlarmKu
package.name = alarmku
package.domain = org.phobiakalian.alarmku

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0
requirements = python3,kivy==2.1.0,plyer

android.permissions = WAKE_LOCK,VIBRATE,RECEIVE_BOOT_COMPLETED,INTERNET
android.api = 33
android.minapi = 21
android.ndk = 23b
android.sdk = 30

[buildozer]
log_level = 1