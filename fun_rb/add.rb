#PROGRAMA PARTE DE @ROBOTMAIN
print "ADDRESS$> "
test = gets.chomp
if test!=""
    system("python3 ./fun_py/basic_scan.py #{test}")
end
if test==""
    print "Debes especificar la direccion BREAK\n"
    sleep 4
    system("./a.out")
end
