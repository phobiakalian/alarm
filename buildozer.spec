[app]
title = AlarmKu
package.name = alarmku
package.domain = org.phobiakalian
# ✅ Package akan jadi: org.phobiakalian.alarmku (bukan double "alarmku")

version = 1.0
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

requirements = python3,kivy,plyer

android.permissions = android.permission.INTERNET,android.permission.VIBRATE,android.permission.WAKE_LOCK,android.permission.POST_NOTIFICATIONS

android.api = 33
android.minapi = 21
android.ndk = 25b
# ✅ Hapus android.sdk (deprecated)

# ✅ Tambahkan config untuk kompatibilitas Gradle
android.gradle_dependencies = androidx.core:core-ktx:1.9.0
android.add_aars = 
android.add_jars = 
android.gradle_build_template = gradle.properties

p4a.bootstrap = sdl2
p4a.android_gradle_version = 8.2.1  # ✅ Pin Gradle plugin version

[buildozer]
log_level = 3
warn_on_root = 1
android.accept_sdk_license = True