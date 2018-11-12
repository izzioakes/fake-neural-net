def setup():
    size(1500,900)
    add_library('pdf')
    beginRecord(PDF, "boobo2.pdf")

def draw():
    background(255)

    randomseed = 60
    distortion = 600
    pointnumber = 20
    
    pointsize = 4
    strokeweight = 0.5
    fill_alpha = 255
    
    fill(0,fill_alpha)
    strokeWeight(strokeweight)
    randomSeed(randomseed)
    xpoints = [int(random(200, width-200))]
    ypoints = [int(random(200,height-200))]
    ellipse(xpoints[0], ypoints[0], pointsize, pointsize)
    
    for i in range(pointnumber):
        x1 = xpoints[-1]
        y1 = ypoints[-1]
        x2 = x1 + int(random(-distortion,distortion))
        while x2 > width-200 or x2 < 200:
            x2 = x1 + int(random(-distortion,distortion))
        y2 = y1 + int(random(-distortion,distortion))
        while y2 > height-200 or y2 < 200:
            y2 = y1 + int(random(-distortion,distortion))
        xpoints.append(x2)
        ypoints.append(y2)
        ellipse(x2,y2,pointsize, pointsize)
        
    dups = []
    for xpoint1, ypoint1 in zip(xpoints, ypoints):
        for xpoint2, ypoint2 in zip(xpoints[1:], ypoints[1:]):
            point_string = str(xpoint1)+str(ypoint1)+str(xpoint2)+str(ypoint2)
            point_string2 = str(xpoint2)+str(ypoint2)+str(xpoint1)+str(ypoint1)
            if point_string not in dups:
                line(xpoint1,ypoint1,xpoint2,ypoint2)
                dups.append(point_string)
                dups.append(point_string2)
                
    endRecord()
    noLoop()
