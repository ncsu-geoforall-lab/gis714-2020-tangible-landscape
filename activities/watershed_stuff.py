#!/usr/bin/env python3

"""
Instructions

- Functions intended to run for each scan
  need to be named run_xxxxx

- Do not modify the parameters of the run_xxx function
  unless you know what you are doing
  see optional parameters:
  https://github.com/tangible-landscape/grass-tangible-landscape/wiki/Running-analyses-and-developing-workflows#python-workflows

- All gs.run_command/read_command/write_command/parse_command
  need to be passed env parameter (..., env=env)
"""

import grass.script as gs


# def run_slope(scanned_elev, env, **kwargs):
#     gs.run_command('r.slope.aspect', elevation=scanned_elev, slope='slope', env=env)


# def run_contours(scanned_elev, env, **kwargs):
#     interval = 5
#     gs.run_command('r.contour', input=scanned_elev, output='contours', step=interval, flags='t', env=env)

def run_hydro(scanned_elev, env, **kwargs):
    gs.run_command('r.watershed', elevation=scanned_elev, accumulation='flow_accum',
                   basin='watersheds', threshold=1000, flags='a', env=env)
    gs.run_command('r.to.vect', input='watersheds', output='watersheds', type='area', env=env)

def run_watershed_slope(scanned_elev, env, **kwargs):
    gs.run_command('r.watershed', elevation=scanned_elev, accumulation='flow_accum',
                   basin='watersheds', threshold=1000, env=env)
    gs.run_command('r.slope.aspect', elevation=scanned_elev, slope='slope', env=env)
    gs.run_command('r.stats.zonal', base='watersheds', cover='slope', method='average',
                   output='watersheds_slope', env=env)
    gs.run_command('r.colors', map='watersheds_slope', color='bgyr', env=env)

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

    # run_slope(scanned_elev=elev_resampled, env=None)
    # run_contours(scanned_elev=elev_resampled, env=None)
    
    run_hydro(scanned_elev=elev_resampled, env=None)
    
    run_watershed_slope(scanned_elev=elev_resampled, env=None)

if __name__ == '__main__':
    main()
