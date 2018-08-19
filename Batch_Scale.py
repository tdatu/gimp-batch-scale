#!/usr/bin/env python

#   Gimp-Python - allows the writing of Gimp plugins in Python.
#   Copyright (C) 2018 Anthony Datu <>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gimpfu import *
import os, sys

gettext.install("gimp20-python", gimp.locale_directory, unicode=True)


def batch_scales(source_directory, output_directory, width, height):

    if not os.path.exists(output_directory):
        os.mkdir(output_directory)
    
    if os.path.exists(source_directory):
        os.chdir(source_directory)
        for f in os.listdir(os.getcwd()):

            #Only process image format below
            if(f[-3:].lower() in ["jpg", "png", "tiff", "bmp", "jpeg", "gif", "psd","xcf"]):
                img = pdb.gimp_file_load(source_directory + os.sep + f, f)

                #Get image dimensions
                img_width = pdb.gimp_image_width(img)
                img_height = pdb.gimp_image_height(img)

                #Determine orientation
                orientation = "landscape"

                if(img_height > img_width):
                    orientation = "portrait"
                
                # Compute new height or width 
                # Calculations ensure width or height does not
                # Fall under the minimum constraints
                new_height = height
                new_width = width

                if(orientation == "landscape"):
                    new_height = width * img_height / img_width
                else:
                    new_width = height * img_width / img_height

                #Resize to width x height
                pdb.gimp_image_scale(img, new_width, new_height)

                #Crop
                pdb.gimp_image_crop(img, width, height, 0, 0)

                pdb.gimp_message(width)
                pdb.gimp_message(height)

                #Save the image
                pdb.gimp_file_save(
                    img, 
                    img.layers[0], 
                    output_directory + os.sep + img.name, 
                    img.name                 
                )


register(
    "python-fu-batch-scale",
    N_("Scale images in batches"),
    "Scale images.",
    "Anthony Datu",
    "Anthony Datu",
    "2018",
    N_("_BatchScale..."),
    "RGB*, GRAY*",
    [
        (
            PF_DIRNAME, "source",
            _("Source Folder"), 
            os.path.join(os.environ["USERPROFILE"],"Pictures")
            if "USERPROFILE" in os.environ 
            else os.path.join(os.environ["HOME"],"Pictures")
        ),
        (
            PF_DIRNAME, "output",
            _("Output Folder"), 
            os.path.join(os.environ["USERPROFILE"],"Pictures")
            if "USERPROFILE" in os.environ 
            else os.path.join(os.environ["HOME"],"Pictures")
        ),
        (PF_INT, "width", _("Min Width"), 1920),
        (PF_INT, "height", _("Min Height"), 1080)
    ],
    [],
    batch_scales,
    menu="<Image>/Image/Transform",
    )

main()
