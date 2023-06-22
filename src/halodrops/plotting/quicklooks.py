from halodrops import sonde
from halodrops.helper import paths
from halodrops.qc import profile

from importlib import reload
from gogoesgone import processing as pr
from gogoesgone import zarr_access as za

reload(pr)
reload(za)

import xarray as xr
import numpy as np
import cartopy as cp
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from cartopy.feature import LAND
import cartopy.feature as cfeature
from matplotlib.offsetbox import AnchoredText
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.dates as mdates
from datetime import datetime, date
import s3fs
import pandas as pd


def get_mean_launch_time(ds_flight=None, time_format="%Y%m%d %H:%M:%S"):

    """
    Compute mean launch time from all sondes in the dataset.
    """

    mean_time = ds_flight.launch_time.mean().values

    return mean_time


def get_satellite_data(
    satellite_time="mean_launch_time",
    time_format="%Y%m%d %H:%M:%S",
    satellite_name="goes16",
    channel=13,
    product="ABI-L2-CMIPF",
    extent=(-62, -48, 10, 20),
):

    """
    Access satellite data for nearest time, map to lon/lat grid, and convert to dataset.
    """

    # Ensure time is in correct format
    pd_time = pd.to_datetime(str(satellite_time))
    str_time = pd_time.strftime(time_format)

    # Get filepath to satellite data at nearest time.
    flist = za.nearest_time_url(str_time, time_format, channel, product, satellite_name)
    m = za.get_mapper_from_mzz(flist)

    # Select subset of satellite domain
    img = pr.Image(m)
    subset = img.subset_region_from_latlon_extents(extent, unit="degree")

    return subset


def launch_locations_map(
    ds_flight=None,
    save_filepath="/path/to/save/",
    color_coding_var="IWV",
    color_coding_cmap="gist_earth",
    overlay_satellite=False,
    satellite_data=None,
    satellite_time=None,
    extent=(-62, -48, 10, 20),
    satellite_cmap="cubehelix_r",
    satellite_vmin=280,
    satellite_vmax=300,
):

    """
    Plot dropsonde launch locations, optionally over satellite images.
    """

    fig = plt.figure()

    ax = plt.axes(projection=ccrs.AzimuthalEquidistant())
    ax.coastlines(resolution="50m", linewidth=1.5)
    ax.set_extent(extent, crs=ccrs.PlateCarree())

    # Plot satellite image
    if overlay_satellite == True:
        sat_im = satellite_data.CMI.isel(t=0).plot(
            ax=ax,
            x="lon",
            y="lat",
            cmap=satellite_cmap,
            add_colorbar=True,
            cbar_kwargs={"pad": 0.15, "extend": "both", "aspect": 30},
            vmin=satellite_vmin,
            vmax=satellite_vmax,
            zorder=-1,
            transform=ccrs.PlateCarree(),
        )

    # Plot flight path
    ax.plot(
        ds_flight["lon"].isel(alt=-700),
        ds_flight["lat"].isel(alt=-700),
        c="red",
        linestyle=":",
        transform=ccrs.PlateCarree(),
        zorder=1,
    )

    # Plot launch locations
    im_launches = ax.scatter(
        ds_flight["lon"].isel(alt=-700),
        ds_flight["lat"].isel(alt=-700),
        marker="o",
        edgecolor="grey",
        s=60,
        transform=ccrs.PlateCarree(),
        c=ds_flight[color_coding_var],
        cmap=color_coding_cmap,
    )

    # Assigning axes ticks
    xticks = np.arange(-180, 180, 4)
    yticks = np.arange(-90, 90, 4)

    # Setting up the gridlines
    gl = ax.gridlines(
        crs=ccrs.PlateCarree(),
        draw_labels=True,
        linewidth=1,
        color="gray",
        alpha=0.2,
        linestyle="--",
    )
    gl.xlocator = mticker.FixedLocator(xticks)
    gl.ylocator = mticker.FixedLocator(yticks)
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabel_style = {"size": 12, "color": "k"}
    gl.ylabel_style = {"size": 12, "color": "k"}

    # Colorbar
    cax = fig.add_axes([0.08, -0.05, 0.85, 0.02])
    g = fig.colorbar(
        im_launches,
        cax=cax,
        orientation="horizontal",
        shrink=0.5,
        pad=0.02,
        extend="both",
        aspect=10,
    )
    g.set_label(ds_flight[color_coding_var].long_name, fontsize=12)
    plt.tick_params(labelsize=10)

    # Title
    ax.set_title(f"Satellite Time = {satellite_image.t[0].values}", pad=10)

    # Save figure
    plt.savefig(save_filepath, dpi=300, bbox_inches="tight")