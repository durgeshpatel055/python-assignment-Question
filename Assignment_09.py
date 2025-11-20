def calculate_notes(amount, start_denom):
    denoms = [100, 50, 20, 10, 5, 2, 1]

    
    start_index = denoms.index(start_denom)


    available_denoms = denoms[start_index:]

    for d in available_denoms:
        match d:
            case 100:
                count = amount // 100
                amount %= 100
                print(f"100 rupees note: {count}")

            case 50:
                count = amount // 50
                amount %= 50
                print(f"50 rupees note: {count}")

            case 20:
                count = amount // 20
                amount %= 20
                print(f"20 rupees note: {count}")

            case 10:
                count = amount // 10
                amount %= 10
                print(f"10 rupees note: {count}")

            case 5:
                count = amount // 5
                amount %= 5
                print(f"5 rupees note: {count}")

            case 2:
                count = amount // 2
                amount %= 2
                print(f"2 rupees note: {count}")

            case 1:
                count = amount // 1
                amount %= 1
                print(f"1 rupees note: {count}")



amount = int(input())
start_denom = int(input())


calculate_notes(amount, start_denom)
