# extrema.py

import numpy as np


def find_extrema(position):

    ymax = []
    ymin = []

    imax = []
    imin = []

    for i in range(len(position) - 1):

        if (
            position[i]
            - position[i + 1]
        ) > 1:

            ymax.append(position[i])

            ymin.append(position[i + 1])

            imax.append(i)

            imin.append(i + 1)

    ymax = np.asarray(ymax)
    ymin = np.asarray(ymin)

    imax = np.asarray(imax)
    imin = np.asarray(imin)

    return (
        ymax,
        ymin,
        imax,
        imin,
    )


def reorder_for_periods(
    ymax,
    ymin,
    imax,
    imin,
):

    if (
        len(ymin)
        == len(ymax) + 1
        and imax[0] > imin[0]
    ):

        imin = imin[1:]

    elif (
        len(ymax)
        == len(ymin)
        and imax[0] > imin[0]
    ):

        imax = imax[:-1]

        imin = imin[1:]

    elif (
        len(ymax)
        == len(ymin) + 1
        and imax[0] < imin[0]
    ):

        imax = imax[:-1]

    return (
        ymax,
        ymin,
        imax,
        imin,
    )


def reorder_for_velocity(
    ymax,
    ymin,
    imax,
    imin,
):

    if (
        len(ymin)
        == len(ymax) + 1
        and imax[0] > imin[0]
    ):

        ymin = ymin[:-1]
        imin = imin[:-1]

    elif (
        len(ymax)
        == len(ymin) + 1
        and imax[0] < imin[0]
    ):

        ymax = ymax[1:]
        imax = imax[1:]

    elif (
        len(ymax)
        == len(ymin)
        and imax[0] < imin[0]
    ):

        ymax = ymax[1:]
        imax = imax[1:]

        ymin = ymin[:-1]
        imin = imin[:-1]

    return (
        ymax,
        ymin,
        imax,
        imin,
    )