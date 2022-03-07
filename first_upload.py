def machinePrecision(f=float):
    machine=f(1)
    while f(1)+f(machine)!=f(1):
        new_machine=machine
        machine=f(machine)/f(2)
    return new_machine

print("before:",abs(3.0*(4.0/3.0-1)-1))
print("after:",abs(3.0*(4.0/3.0-1)-1)-machinePrecision())

