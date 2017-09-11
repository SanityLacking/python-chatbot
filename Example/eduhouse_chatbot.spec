# -*- mode: python -*-

block_cipher = None


a = Analysis(['eduhouse_chatbot.py'],
             pathex=['C:\\Users\\s2829382\\Projects\\Chatbot\\TensorFlow\\download\\eduhouse\\example'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='eduhouse_chatbot',
          debug=False,
          strip=False,
          upx=True,
          console=True )
