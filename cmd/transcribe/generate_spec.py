import os
import site
from PyInstaller.utils.hooks import collect_submodules


def find_package_path(package_name):
    """Find the installation path of a Python package."""
    for site_dir in site.getsitepackages():
        package_path = os.path.join(site_dir, package_name)
        if os.path.exists(package_path):
            return package_path

    # Also check the user site-packages directory
    package_path = os.path.join(site.getusersitepackages(), package_name)
    if os.path.exists(package_path):
        return package_path

    raise FileNotFoundError(f"Package {package_name} not found in any site-packages directories.")


def create_spec_file():
    # Find openai-whisper package path
    whisper_path = find_package_path("whisper")
    assets_path = os.path.join(whisper_path, "assets", "mel_filters.npz")

    if not os.path.exists(assets_path):
        raise FileNotFoundError(f"Required asset {assets_path} not found in whisper package.")

    # Generate spec file content for CLI application with code signing
    spec_content = f"""
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['cmd/transcribe/transcribe.py'],  # Replace with your main Python script
    pathex=['.'],
    binaries=[],
    datas=[
        ('{assets_path}', 'whisper/assets'),  # Include mel_filters.npz in the correct location
        ('libs', 'libs')  # Ensure libs are included as well
    ],
    hiddenimports={collect_submodules('libs')},
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,  # Include binaries from Analysis
    a.datas,     # Include data files from Analysis
    [],
    name='transcribe',  # Name of the CLI binary
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Ensure this is a console application
    distpath='dist',  # Specify the output directory
    codesign_identity="Developer ID Application: Mathew Silva (Z25737G79K)"  # Correct signing identity
)
"""

    # Write spec file
    with open("transcribe.spec", "w") as f:
        f.write(spec_content)

    print("Spec file generated and customized successfully.")


if __name__ == "__main__":
    create_spec_file()
