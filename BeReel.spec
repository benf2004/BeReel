import sys, platform
sys.path.append('')

uname = platform.uname()
arch = uname.machine
iconfile = "static/images/BeReel_logo.icns" if uname.system=="Darwin" else "static/images/BeReel_logo.ico"

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('templates', 'templates'), ('static', 'static')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='BeReel',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

if uname.system == "Darwin":
    app = BUNDLE(exe,
                 name='BeReel.app',
                 version='1.0.0',
                 icon=iconfile,
                 bundle_identifier='com.bereel.bereelapp')
