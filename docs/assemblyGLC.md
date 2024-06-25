### Gramática Livre de Contexto para MIPS Assembly

#### Símbolos Terminais:
- Instruções: `add`, `sub`, `and`, `or`, `nor`, `lw`, `sw`, `beq`, `bne`, `j`, `addi`, `subi`, `andi`, `ori`
- Registradores: `$zero`, `$t0`, ..., `$t9`, `$s1`, ..., `$s7`, `$a0`, ..., `$a3`, `$v0`, `$v1`, `$gp`, `$fp`, `$ra`, `$at`
- Outros símbolos: `,`, `:`, `(`, `)`

#### Símbolos Não-terminais:
- `<program>`
- `<instruction>`
- `<R_instruction>`
- `<I_instruction>`
- `<J_instruction>`
- `<register>`
- `<immediate>`
- `<label>`
- `<address>`

#### Produções:
1. `<program> -> <label_decl> <program> | <instruction> <program> | ε`
2. `<instruction> -> <R_instruction> | <I_instruction> | <J_instruction>`
3. `<R_instruction> -> "add" <register> "," <register> "," <register> | "sub" <register> "," <register> "," <register> | "and" <register> "," <register> "," <register> | "or" <register> "," <register> "," <register> | "nor" <register> "," <register> "," <register>`
4. `<I_instruction> -> "lw" <register> "," <address> | "sw" <register> "," <address> | "beq" <register> "," <register> "," <label> | "bne" <register> "," <register> "," <label> | "addi" <register> "," <register> "," <immediate> | "subi" <register> "," <register> "," <immediate> | "andi" <register> "," <register> "," <immediate> | "ori" <register> "," <register> "," <immediate>`
5. `<J_instruction> -> "j" <label>`
6. `<register> -> "$zero" | "$t0" | "$t1" | "$t2" | "$t3" | "$t4" | "$t5" | "$t6" | "$t7" | "$t8" | "$t9" | "$s0" | "$s1" | "$s2" | "$s3" | "$s4" | "$s5" | "$s6" | "$s7"`
7. `<immediate> -> <digit> <digit> <digit> <digit>`
8. `<label> -> [A-Za-z_][A-Za-z0-9_]*`
9. `<address> -> <immediate> "(" <register> ")"`
10. `<label_decl> -> <label> ":"`

Usamos uma abordagem de analisador descendente recursivo, que envolve a criação de uma função para cada não terminal na gramática. 

1. Definimos Classes de Token e o Lexer: O lexer converterá a string de entrada em tokens.
2. Classe Parser: O parser converterá a lista de tokens em uma árvore de sintaxe abstrata (AST).