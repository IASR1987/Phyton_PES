import subprocess

# 1. Abrir un programa (Notepad)
subprocess.run(['start', 'notepad.exe'], shell=True)

# 2. Abrir documentos con su aplicación asociada
# Abrir un documento de Word
subprocess.run(['start', 'C:\\ruta\\a\\tu\\documento.docx'], shell=True)
# Abrir un archivo PDF
subprocess.run(['start', 'C:\\ruta\\a\\tu\\archivo.pdf'], shell=True)
# Abrir una imagen
subprocess.run(['start', 'C:\\ruta\\a\\tu\\imagen.png'], shell=True)

# 3. Abrir una URL en el navegador predeterminado
subprocess.run(['start', 'https://www.ejemplo.com'], shell=True)

# 4. Abrir la línea de comandos (cmd)
subprocess.run(['start', 'cmd'], shell=True)

# Abrir PowerShell
subprocess.run(['start', 'powershell'], shell=True)

# 5. Abrir carpetas en el Explorador de Archivos
subprocess.run(['start', 'C:\\ruta\\a\\tu\\carpeta'], shell=True)

# 6. Ejecutar scripts o aplicaciones
subprocess.run(['start', 'python', 'C:\\ruta\\a\\tu\\script.py'], shell=True)

# 7. Abrir archivos de texto para edición
subprocess.run(['start', 'C:\\ruta\\a\\tu\\archivo.txt'], shell=True)

# 8. Abrir aplicaciones de configuración de Windows
# Abrir el Panel de Control
subprocess.run(['start', 'control'], shell=True)
# Abrir la configuración de red
subprocess.run(['start', 'ms-settings:network'], shell=True)
