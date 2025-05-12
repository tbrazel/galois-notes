def order_spf2_2n(r):
    if r % 2 != 0:
        raise ValueError("Input must be an even integer.")
    
    # Get the 2^{k^2} part
    k = int(r/2)
    output_num = pow(2,(k**2))


    for m in range(2,r+1,2):
        output_num = output_num * (pow(2,m)-1)
    return output_num


def order_o_plus(r):
    k = int(r/2)
    spf2 = order_spf2_2n(r)

    subgp_index = pow(2,k-1)*(pow(2,k)+1)
    return int(spf2/subgp_index)

def order_o_minus(r):
    k = int(r/2)
    spf2 = order_spf2_2n(r)

    subgp_index = pow(2,k-1)*(pow(2,k)-1)
    return int(spf2/subgp_index)

rank = int(input('input rank: '))
print('order of sp(f2) for that rank is: ' + str(order_spf2_2n(rank)))
print('order of O^+ of that rank is '+ str(order_o_plus(rank)))
print('order of O^- of that rank is '+ str(order_o_minus(rank)))