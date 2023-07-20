# Text Alignment

width = int(input())
c = 'H'

# Top cone
for i in range(1, width*2-1+1, 2):
    print((c*i).center(width*2-1))
    
# Top pillar
for i in range(0, width+1):
    print((c*width).center(width*2) + (c*width).center(width*6))
    
# Middle Belt
for i in range((width+1)//2):
    print((c*(width*5)).center(width*6))
    
# bottom pillar
for i in range(0, width+1):
    print((c*width).center(width*2) + (c*width).center(width*6))
    
# bottom cone
for i in range(width*2-1, -1, -2):
    print((c*i).center((width*2-1+1)*5))
