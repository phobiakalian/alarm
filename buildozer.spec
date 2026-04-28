[app]
title = AlarmKu
package.name = alarmku
package.domain = org.phobiakalian.alarmku
package.version = 1.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,atlas_d

version = 1.0
requirements = python3,kivy==2.3.0,plyer==2.1.0

[buildozer]
log_level = 2
warn_on_root = 1

[app]
android.permissions = WAKE_LOCK,VIBRATE,RECEIVE_BOOT_COMPLETED,USE_FULL_SCREEN_INTENT,POST_NOTIFICATIONS,INTERNET,FOREGROUND_SERVICE

# Ubuntu 24.04 compatible
android.api = 34
android.minapi = 24
android.ndk = 25.2.9519653
android.sdk = 34

[buildozer]
android.accept_sdk_license = True
android.prep_strip_lib = True