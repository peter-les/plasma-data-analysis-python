# attachment_detector.py

import cv2
import numpy as np


def detect_attachment_positions(
    video_path,
    row,
    start_pixel,
    end_pixel,
    threshold,
    factor,
    n0,
    nf,
):
    cap = cv2.VideoCapture(str(video_path))

    frame_count = nf - n0 + 1

    pixel_pos = np.full(frame_count, np.nan)

    position = np.full(frame_count, np.nan)

    missing = 0

    for frame_idx in range(n0, nf + 1):

        cap.set(
            cv2.CAP_PROP_POS_FRAMES,
            frame_idx - 1,
        )

        ret, frame = cap.read()

        if not ret:
            continue

        if len(frame.shape) == 3:
            frame = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2GRAY,
            )

        profile = frame[
            row,
            start_pixel:
        ]

        mask = (
            (profile > threshold)
            &
            (profile < 255)
        )

        indices = np.where(mask)[0]

        output_idx = frame_idx - n0

        if len(indices) == 0:

            missing += 1

            position[output_idx] = np.nan

        else:

            pixel_pos[output_idx] = indices[0]

            position[output_idx] = (
                (
                    pixel_pos[output_idx]
                    + start_pixel
                    - end_pixel
                )
                * factor
                + 14
            )

    cap.release()

    return pixel_pos, position, missing