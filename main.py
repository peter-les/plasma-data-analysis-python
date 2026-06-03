# main.py

import numpy as np

from config import *

from attachment_detector import (
    detect_attachment_positions,
)

from extrema import (
    find_extrema,
    reorder_for_periods,
    reorder_for_velocity,
)

from statistics import (
    calculate_periods,
    calculate_motion_statistics,
)

from uncertainties import (
    calculate_output_uncertainties,
)

from plotting import (
    plot_attachment,
)


def main():

    print(
        "Loading video..."
    )

    pixel_pos, position, missing = (
        detect_attachment_positions(
            VIDEO_PATH,
            ROW,
            START_PIXEL,
            END_PIXEL,
            THRESHOLD,
            FACTOR,
            N0,
            NF,
        )
    )

    print(
        f"Missing frames: {missing}"
    )

    time = np.arange(
        (N0 - 1)
        * FRAME_TIME_US,
        (NF - 1)
        * FRAME_TIME_US
        + FRAME_TIME_US,
        FRAME_TIME_US,
    )

    ymax, ymin, imax, imin = (
        find_extrema(
            position
        )
    )

    (
        ymax_p,
        ymin_p,
        imax_p,
        imin_p,
    ) = reorder_for_periods(
        ymax.copy(),
        ymin.copy(),
        imax.copy(),
        imin.copy(),
    )

    (
        t_periods,
        periods_max,
        periods_min,
    ) = calculate_periods(
        time,
        imax_p,
        imin_p,
    )

    (
        ymax,
        ymin,
        imax,
        imin,
    ) = reorder_for_velocity(
        ymax,
        ymin,
        imax,
        imin,
    )

    stats = (
        calculate_motion_statistics(
            ymax,
            ymin,
            imax,
            imin,
            time,
        )
    )

    unc = (
        calculate_output_uncertainties(
            stats["velocities"],
            stats["distances"],
            stats["times"],
            ymax,
            ymin,
            periods_max,
            periods_min,
            stats["v_average"],
            stats["d_average"],
            stats["t_average"],
        )
    )

    print()
    print(
        "RESULTS"
    )
    print(
        "------------------"
    )

    print(
        f"Velocity: {stats['v_average']:.1f} ± {unc['v_std']:.1f} m/s"
    )

    print(
        f"Movement time: {stats['t_average']:.2f} ± {unc['t_std']:.2f} us"
    )

    print(
        f"Restrike period: {t_periods:.2f} ± {unc['t_periods_std']:.2f} us"
    )

    print(
        f"Distance: {stats['d_average']:.2f} ± {unc['d_std']:.2f} mm"
    )

    print(
        f"Lmin: {stats['Lmin_average']:.2f} ± {unc['Lmin_std']:.2f} mm"
    )

    print(
        f"Lmax: {stats['Lmax_average']:.2f} ± {unc['Lmax_std']:.2f} mm"
    )

    if GRAPHS:

        plot_attachment(
            time,
            position,
            imax,
            imin,
            ymax,
            ymin,
            900,
        )


if __name__ == "__main__":
    main()