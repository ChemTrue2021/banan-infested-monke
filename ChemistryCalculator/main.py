try:
    import PyQt5, webview, PyQtWebEngine 
except:
    import os
    os.system("pip install PyQt5 PyQtWebEngine pywebview")

mainwindow = webview.create_window('Hello World', 'page.html')

webview.start()