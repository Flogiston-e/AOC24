input = open("17.txt").read().strip().split("\n")
input.pop(3)
A, B, C, program = [x.split(":")[1] for x in input]
A, B, C = int(A), int(B), int(C)
program = [int(x) for x in program.split(",")]
pl = len(program)

def combo(A,B,C,operand):
    if operand < 4: return operand
    if operand == 4: return A
    if operand == 5: return B
    if operand == 6: return C

def computer(A,B,C,program,pl):
    output = []
    i = 0
    while i < pl-1:
        opcode, operand = program[i:i+2]
        if opcode == 0:
            A = A//(2**combo(A,B,C,operand))
        elif opcode == 1:
            B = B^operand
        elif opcode == 2:
            B = combo(A,B,C,operand)%8
        elif opcode == 3:
            if A != 0:
                i = operand-2
        elif opcode == 4:
            B = B^C
        elif opcode == 5:
            output.append(combo(A,B,C,operand)%8)
        elif opcode == 6:
            B = A//(2**combo(A,B,C,operand))
        elif opcode == 7:
            C = A//(2**combo(A,B,C,operand))
        i += 2
    return output

print(computer(A,B,C,program,pl))

cycles = [8**i*7 for i in range(pl-2,-1,-1)] + [1]
A = sum(cycles[1:-1])+1
up = True
ci = 0
while ci < pl:
    cycle = cycles[ci]
    while True:
        if up:
            A += cycle
        else:
            A -= cycle
        output = computer(A,B,C,program,pl)
        if ci != 0:
            if output[pl-ci] != program[pl-ci]:
                if up:
                    ci -= 1
                    break
                up = True
                continue
        if up:
            if output[pl-ci-1] == program[pl-ci-1]:
                ci += 1
                up = False
                break
print(A)