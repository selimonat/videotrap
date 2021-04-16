# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from goprocam import constants
from goprocam import GoProCamera
import datetime
import time


def take_photo(n_photos=1, time_between=0):
    """

    :return:
    """
    gp_cam = GoProCamera.GoPro(constants.auth)
    # gp_cam.overview()
    gp_cam.sendCamera(constants.Hero3Commands.PHOTO_RESOLUTION,constants.Hero3Commands.PhotoResolution.PR5MP_W)
    n = 0
    while n <= n_photos:

        gp_cam.take_photo()

        filename = datetime.datetime.now().isoformat()
        gp_cam.downloadLastMedia(custom_filename=f"/Users/sonat/Desktop/gopro/{filename}.png")
        gp_cam.delete(1)
        time.sleep(time_between)
        n += 1


if __name__ == '__main__':
    take_photo(96, 3600)

