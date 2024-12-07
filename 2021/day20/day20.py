# https://adventofcode.com/2021/day/20


def readFile():
    with open("./day20/sample.txt", "r") as f:
        return f.readline().strip(), [list(line.strip()) for line in f if line.strip() != '']


def main():
    algo, img = readFile()
    imgDict = dict()
    newImgDict = dict()
    for y in range(len(img)):
        for x in range(len(img[0])):
            if img[y][x] == '#':
                imgDict[(x,y)] = img[y][x]

    for i in range(2):
        xMin, xMax = min([k[0] for k,v in imgDict.items()]), max([k[0] for k,v in imgDict.items()])
        yMin, yMax = min([k[1] for k,v in imgDict.items()]), max([k[1] for k,v in imgDict.items()])

        print(xMin-1, xMax+1, yMin-1, yMax+1)

        for y in range(yMin-1, yMax + 2):
            for x in range(xMin-1, xMax + 2):
                binaryNum = ''
                index = 0
                for yi in range(y-1, y+2):
                    for xi in range(x-1, x+2):
                        binaryNum += '0' if (x+xi,y+yi) not in imgDict else '1'

                        index = index << 1 | (
                            int((xi, yi) in imgDict)
                            if (xMin <= xi <= xMax and yMin <= yi <= yMax)
                            else i & 1 & algo[0]
                        )
                if algo[index]:
                    newImgDict[(x,y)] = '#'
        print(sum([1 for k, v in newImgDict.items() if v == '#']))
        imgDict = newImgDict.copy()
        newImgDict.clear()
        

        # for k,v in newImgDict.items():
        #     if k not in imgDict:
        #         imgDict[k] = v
        #     else:
        #         imgDict[k] = newImgDict[k]

        
 

    


    #img = padImageTwice(img, len(img[0]), len(img))
    #newImg = [row.copy() for row in img]




    # for row in newImg:
    #     print("".join(row))
    # print()
    
    # for i in range(2): # apply enhancement twice
    #     for y in range(1, len(img)-1):
    #         for x in range(1, len(img[0])-1):
    #             pixels = img[y-1][x-1] + img[y-1][x] + img[y-1][x+1] + \
    #                 img[y][x-1] + img[y][x] + img[y][x+1] + \
    #                 img[y+1][x-1] + img[y+1][x] + img[y+1][x+1]
    #             newImg[y][x] = convertPixelsToBits(pixels, alg)

    #     img = [row.copy() for row in newImg]
    #     img = padImageOnce(newImg, len(newImg[0]), len(newImg))
    #     newImg = [row.copy() for row in img]
    #     for row in newImg: 
    #         print("".join(row))
    #     print()


    # print( sum([1 for y in range(len(newImg)) for x in range(len(newImg[0])) if newImg[y][x] == '#']) )


main()