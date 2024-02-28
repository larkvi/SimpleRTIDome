# SimpleRTIDome

A GitHub supporting and documenting a simple—and inexpensive—DIY camera-agnostic (and hopefully soon, camera-integrated) Refectance Transformation Imaging (RTI) dome, suitable for teaching and experimentation.

3D printing files have been uploaded for the v2 version of the prototype. These files work, but are due to be rebuilt shortly to amend small issues. Due to delays in receiving parts from China, the v3 version (hopefully the release version) is not expected until June 2024 at the earliest. If you have interest or feedback, please feel free to use the issues or email me.

There are three scripts currently included in the repository. Due to a fundamental issue with the Neopixels library, they currently muse be run with `sudo`, which is less than desirable for many reasons, not the least because the files written will be owned by root. Until a workaround is developed, it is necessary to use the `chgrp -R` and `chown -R` commands on the parent folder of the resulting files after each use, in order to facilitate copying and use by non-root processes.

`prelight.py` is mainly used for variants of the dome that do not have the integrated Raspberry Pi Camera Module 3 in them, where a DSLR is being used instead. It allows the lighting of a few pixels for the purpose of focus and exposure.

`rti_loop_gphoto2.py` is used when connecting the dome to a USB camera, such as a DSLR.

`rti_loop_picam2.py` is called when using the integrated Raspberry Pi Camera Module 3.

The difference between the two commands is the library that is used in order to communicate with the camera. It is intended to merge them in the future, and allow the passing of all commands as arguments on the command line. At the moment, the simplest way to use either, in my opinion, is to open the Thonny editor using `sudo thonny` and edit the variables at the top to name batches and the like.

More information and build plans will be posted shortly.