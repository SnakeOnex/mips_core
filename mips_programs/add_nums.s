.text
.global __start
__start: 
    li $t2, 13
    li $t3, 27
    add $t4, $t2, $t3
    move $a0, $t4
    li $v0, 4001
    syscall
