[app]
title = My Hunter App BRI
package.name = myhunterapp
package.domain = org.goanonim17
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True
android.api = 33
android.ndk = 25b
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
