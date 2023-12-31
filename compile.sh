#!/bin/bash


case $(arch) in
    "arm64")
        pyinstaller -y --clean BeReel.spec --distpath ./dist_arm
        cd dist_arm
        zip -r BeReel_macos_arm.zip BeReel.app/
        cd ..
        ;;
    "i386")
        pyinstaller -y --clean BeReel.spec --distpath ./dist_x86
        cd dist_x86
        zip -r BeReel_macos_arm.zip BeReel.app/
        cd ..
esac

echo "Compiled for $(arch)"