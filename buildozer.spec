[app]
title = My Hunter App
package.name = myhunterapp
package.domain = org.goanonim
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,requests,urllib3,chardet,idna

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.skip_update = False
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
