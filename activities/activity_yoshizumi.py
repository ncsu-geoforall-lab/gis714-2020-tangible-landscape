#!/usr/bin/env python3

"""
Instructions

- Functions intended to run for each scan
  need to be named run_xxxxx

- Do not modify the parameters of the run_xxxxx function
  unless you know what you are doing
  see optional parameters:
  https://github.com/tangible-landscape/grass-tangible-landscape/wiki/Running-analyses-and-developing-workflows#python-workflows

- All gs.run_command/read_command/write_command/parse_command
  need to be passed env parameter (..., env=env)
"""

import grass.script as gs


def run_solar_radiance(scanned_elev, env, **kwargs):
    # convert date to day of year
    import datetime
    doy = datetime.datetime(2020, 1, 1).timetuple().tm_yday
    # precompute slope and aspect
    gs.run_command('r.slope.aspect', elevation=scanned_elev, slope='slope', aspect='aspect', env=env)
    gs.run_command('r.sun', elevation=scanned_elev, slope='slope', aspect='aspect', beam_rad='beam', day=doy, time=8, env=env)
    # extract shade and set color to black and white
    gs.mapcalc("shade = if(beam == 0, 0, 1)", env=env)
    gs.run_command('r.colors', map='beam', color='grey')


# this part is for testing without TL
def main():
    import os

    # we want to run this repetetively without deleted the created files
    os.environ['GRASS_OVERWRITE'] = '1'

    elevation = 'elev_lid792_1m'
    elev_resampled = 'elev_resampled'
    # resampling to have similar resolution as with TL
    gs.run_command('g.region', raster=elevation, res=4, flags='a')
    gs.run_command('r.resamp.stats', input=elevation, output=elev_resampled)

    # this will run all 3 examples (slope, contours, points)
    run_solar_radiance(scanned_elev=elev_resampled, env=None)

if __name__ == '__main__':
    main()

