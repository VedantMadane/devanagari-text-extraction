filepath = "D:\\Projects\hindi-text\\sanskrit\\dokumen.tips_maitrayani-samhita-of-yajurveda.pdf"

import fitz
import cv2
import numpy as np
import pdf2image
import pytesseract

# Extract page 3 from PDF in proper quality
page_3 = np.array(pdf2image.convert_from_path(filepath,
                                              first_page=3, last_page=3,
                                              dpi=300, grayscale=True)[0])

# Inverse binarize for contour finding
thr = cv2.threshold(page_3, 128, 255, cv2.THRESH_BINARY_INV)[1]

# Find contours w.r.t. the OpenCV version
cnts = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# STEP 1: Extract texts outside of the two tables

# Mask out the two tables
cnts_tables = [cnt for cnt in cnts if cv2.contourArea(cnt) > 10000]
no_tables = cv2.drawContours(thr.copy(), cnts_tables, -1, 0, cv2.FILLED)

# Find bounding rectangles of texts outside of the two tables
no_tables = cv2.morphologyEx(no_tables, cv2.MORPH_CLOSE, np.full((21, 51), 255))
cnts = cv2.findContours(no_tables, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
rects = sorted([cv2.boundingRect(cnt) for cnt in cnts], key=lambda r: r[1])

# Extract texts from each bounding rectangle
print('\nExtract texts outside of the two tables\n')
for (x, y, w, h) in rects:
    text = pytesseract.image_to_string(page_3[y:y+h, x:x+w],)
                                    #    config='--psm 6', lang='Devanagari')
    text = text.replace('\n', '').replace('\f', '')
    print('x: {}, y: {}, text: {}'.format(x, y, text))

# STEP 2: Extract texts from inside of the two tables

rects = sorted([cv2.boundingRect(cnt) for cnt in cnts_tables],
               key=lambda r: r[1])

# Iterate each table
for i_r, (x, y, w, h) in enumerate(rects, start=1):

    # Find bounding rectangles of cells inside of the current table
    cnts = cv2.findContours(page_3[y+2:y+h-2, x+2:x+w-2],
                            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    inner_rects = sorted([cv2.boundingRect(cnt) for cnt in cnts],
                         key=lambda r: (r[1], r[0]))

    # Extract texts from each cell of the current table
    print('\nExtract texts inside table {}\n'.format(i_r))
    for (xx, yy, ww, hh) in inner_rects:

        # Set current coordinates w.r.t. full image
        xx += x
        yy += y

        # Get current cell
        cell = page_3[yy+2:yy+hh-2, xx+2:xx+ww-2]

        # For table 1, simply extract texts as-is
        if i_r == 1:
            text = pytesseract.image_to_string(cell, )
                                            #    config='--psm 6',
                                            #    lang='Devanagari')
            text = text.replace('\n', '').replace('\f', '')
            print('x: {}, y: {}, text: {}'.format(xx, yy, text))

        # For table 2, extract single elements
        if i_r == 2:

            # Floodfill rectangles around numbers
            ys, xs = np.min(np.argwhere(cell == 0), axis=0)
            temp = cv2.floodFill(cell.copy(), None, (xs, ys), 255)[1]
            mask = cv2.floodFill(thr[yy+2:yy+hh-2, xx+2:xx+ww-2].copy(),
                                 None, (xs, ys), 0)[1]

            # Extract left (Hindi) and right (English) parts
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,
                                    np.full((2 * hh, 5), 255))
            cnts = cv2.findContours(mask,
                                    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]
            boxes = sorted([cv2.boundingRect(cnt) for cnt in cnts],
                           key=lambda b: b[0])

            # Extract texts from each part of the current cell
            for i_b, (x_b, y_b, w_b, h_b) in enumerate(boxes, start=1):

                # For the left (Hindi) part, extract Hindi texts
                if i_b == 1:

                    text = pytesseract.image_to_string(
                        temp[y_b:y_b+h_b, x_b:x_b+w_b],
                        config='--psm 6',
                        lang='Devanagari')
                    text = text.replace('\f', '')

                # For the left (English) part, extract English texts
                if i_b == 2:

                    text = pytesseract.image_to_string(
                        temp[y_b:y_b+h_b, x_b:x_b+w_b],
                        # config='--psm 6',
                        lang='eng')
                    text = text.replace('\f', '')

                print('x: {}, y: {}, text:\n{}'.format(xx, yy, text))