import numpy as np
import cv2
from tqdm import tqdm

from localization import localize_ava_bar_image
from utils import read_image, crop_fit_circle_image, resize_image, get_name

from image_similarity_measures.quality_metrics import rmse, psnr
from skimage.metrics import structural_similarity as ssim 

def calc_similarity_2_image(img1, img2):
  score_rmse = rmse(img1, img2)
  img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)#.astype(int)
  img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)#.astype(int)
  score_ssim = ssim(img1_gray, img2_gray, data_range=255)
  score_psnr = psnr(img1, img2)
  return score_rmse, score_ssim, score_psnr

def make_decision(rmse_cal, ssim_cal, psnr_cal, topk= 5):
  rmse_cal = dict(sorted(rmse_cal.items(), key=lambda item: item[1]))
  ssim_cal = dict(sorted(ssim_cal.items(), key=lambda item: item[1], reverse=True))
  psnr_cal = dict(sorted(psnr_cal.items(), key=lambda item: item[1], reverse= True))

  indicate_rmse = list(rmse_cal.keys())[:topk]
  indicate_ssim = list(ssim_cal.keys())[:topk]
  indicate_psnr = list(psnr_cal.keys())[:topk]
  indicates = list(dict.fromkeys(indicate_ssim + indicate_rmse + indicate_psnr))
  voting = []
  for indicate in indicates:
    tmp_vote = 0
    for scores in (indicate_rmse, indicate_ssim, indicate_psnr):
      if indicate in scores:
        tmp_vote +=1

    voting.append(tmp_vote)
  sorted_voting = list(reversed(np.argsort(voting)))
  sorted_indicated = [indicates[index] for index in sorted_voting]
  return sorted_indicated[:topk]

def match(dir_bars_query = '', dir_images_gallery = '', topk=5):
  result = {}

  for dir_bar in dir_bars_query:
    image_bar_query = read_image(dir_bar)
    ava_hero_image = localize_ava_bar_image(image_bar_query)
    circle_ava_hero = crop_fit_circle_image(ava_hero_image)

    rmse_cal = {}
    ssim_cal = {}
    psnr_cal = {}

    dim = ava_hero_image.shape[:2]
    for dir_image_gallery in tqdm(dir_images_gallery):
      name_image_gallery = get_name(dir_image_gallery)
      image_gallery = read_image(dir_image_gallery)
      circle_ava_hero_gallery = crop_fit_circle_image(image_gallery)
      resized_circle_ava_hero_gallery= resize_image(circle_ava_hero_gallery, dim)

      sr_rmse, sr_ssim, sr_psnr = calc_similarity_2_image(circle_ava_hero, resized_circle_ava_hero_gallery)
      rmse_cal[name_image_gallery] = sr_rmse
      ssim_cal[name_image_gallery] = sr_ssim
      psnr_cal[name_image_gallery] = sr_psnr
    
    result[dir_bar.split("/")[-1]] = make_decision(rmse_cal, ssim_cal, psnr_cal, topk=topk)
  return result