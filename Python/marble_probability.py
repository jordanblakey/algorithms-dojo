def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    # Given blue and red marbles placed in a bag, and blue and red marbles removed, calc p of drawing a blue marble.
    print(blue_start, red_start, blue_pulled, red_pulled)
    red = red_start - red_pulled
    blue = blue_start - blue_pulled
    return blue/(red+blue)
    
# Refactored:
def guess_blue(bs, rs, bp, rp): return (bs-bp)/((rs-rp)+(bs-bp))
