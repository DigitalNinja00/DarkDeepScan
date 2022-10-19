print "ADDRESS> "
var = gets.chomp
puts "usa \'\'"
print "PORTLIST> "
po = gets.chomp
if var!=""
    if po!=""
        system("python3 ./fun_py/especify.py #{var} #{po}")
    end
end
