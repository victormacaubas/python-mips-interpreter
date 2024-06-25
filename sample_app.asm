label1:
    lw $t0, 0($t1)           # Carrega uma palavra da memória no endereço contido em $t1 para o registrador $t0
    lw $t2, 4($t1)           # Carrega uma palavra da memória no endereço (4+$t1) para o registrador $t2

    add $t3, $t0, $t2        # Soma os valores dos registradores $t0 e $t2, armazenando o resultado em $t3
    sub $t4, $t0, $t2        # Subtrai o valor de $t2 do valor de $t0, armazenando o resultado em $t4

    beq $t3, $t4, label2     # Se $t3 for igual a $t4, desvia para o rótulo label2
    bne $t3, $t4, label1     # Se $t3 for diferente de $t4, desvia para o rótulo label1

label2:
    addi $t5, $t3, 10        # Adiciona 10 ao valor de $t3, armazenando o resultado em $t5
    j label1                 # Salta para o rótulo label1