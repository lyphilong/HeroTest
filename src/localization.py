import cv2

def localize_ava_bar_image(image, ratio_crop_w = 1/2):
    """_summary_

    Args:
        image (_type_): _description_
        ratio_crop_w (_type_, optional): _description_. Defaults to 1/2.

    Returns:
        _type_: _description_
    """
    h,w        = image.shape[:2]
    crop_img   = image[0:,0:int(w*ratio_crop_w),:]
    edge       = cv2.Canny(crop_img, 175, 175)
    contours,_ = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    x_max, y_max, w_max, h_max = 0,0,0,0
    for i in contours:
        x,y,w_rect,h_rect = cv2.boundingRect(i)
        if w_rect*h_rect > w_max*h_max:
            x_max, y_max, w_max, h_max = x,y,w_rect,h_rect
    r = max(w_max,h_max)
    if x_max + r > w:
        r = w - x_max
    if y_max + r > h:
        r = h - y_max
    image_localize_ava = image[y_max : y_max + r , x_max: x_max + r]
    
    return image_localize_ava