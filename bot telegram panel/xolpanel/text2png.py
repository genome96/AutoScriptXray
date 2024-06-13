# coding=utf8

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def text2png(text, fullpath, color="#000", bgcolor="#FFF", fontfullpath=None, fontsize=13, leftpadding=3, rightpadding=3, width=300):
    REPLACEMENT_CHARACTER = u'\uFFFD'
    NEWLINE_REPLACEMENT_STRING = ' ' + REPLACEMENT_CHARACTER + ' '
    linkback = "created via @XolPanel"
    fontlinkback = ImageFont.truetype('font.ttf', 15)
    linkbackx = fontlinkback.getsize(linkback)[0]
    linkback_height = fontlinkback.getsize(linkback)[1]
    font = ImageFont.load_default() if fontfullpath == None else ImageFont.truetype(
        fontfullpath, fontsize)
    text = text.replace('\n', NEWLINE_REPLACEMENT_STRING)
    lines = []
    line = u""
    for word in text.split():
        if word == REPLACEMENT_CHARACTER:
            lines.append(line[1:])
            line = u""
            lines.append(u"")
        elif font.getsize(line + ' ' + word)[0] <= (width - rightpadding - leftpadding):
            line += ' ' + word
        else:
            lines.append(line[1:])
            line = u""

            line += ' ' + word

    if len(line) != 0:
        lines.append(line[1:])

    line_height = font.getsize(text)[1]
    img_height = line_height * (len(lines) + 1)

    img = Image.new("RGBA", (width, img_height), bgcolor)
    draw = ImageDraw.Draw(img)

    y = 0
    for line in lines:
        draw.text((leftpadding, y), line, color, font=font)
        y += line_height

    draw.text((width - linkbackx, img_height - linkback_height),
              linkback, color, font=fontlinkback)

    img.save(fullpath, dpi=(300, 300))
