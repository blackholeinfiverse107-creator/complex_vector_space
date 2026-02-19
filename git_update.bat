@echo off
"C:\Program Files\Git\cmd\git.exe" init
"C:\Program Files\Git\cmd\git.exe" remote remove origin
"C:\Program Files\Git\cmd\git.exe" remote add origin https://github.com/blackholeinfiverse107-creator/complex_vector_space.git
"C:\Program Files\Git\cmd\git.exe" add .
"C:\Program Files\Git\cmd\git.exe" commit -m "Update ComplexVector with immutability and mathematical verification"
"C:\Program Files\Git\cmd\git.exe" push -u origin master
"C:\Program Files\Git\cmd\git.exe" push -u origin main
