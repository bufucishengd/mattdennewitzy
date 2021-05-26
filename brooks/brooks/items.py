# -*- coding: utf-8 -*-

import scrapy


class Pitch(scrapy.Item):
    date_stamp = scrapy.Field()
    park_sv_id = scrapy.Field()
    play_guid = scrapy.Field()
    ab_total = scrapy.Field()
    ab_count = scrapy.Field()
    pitcher_id = scrapy.Field()
    batter_id = scrapy.Field()
    ab_id = scrapy.Field()
    des = scrapy.Field()
    type = scrapy.Field()
    id = scrapy.Field()
    sz_top = scrapy.Field()
    sz_bot = scrapy.Field()
    pfx_xdatafile = scrapy.Field()
    pfx_zdatafile = scrapy.Field()
    mlbam_pitch_name = scrapy.Field()
    zone_location = scrapy.Field()
    pitch_con = scrapy.Field()
    stand = scrapy.Field()
    strikes = scrapy.Field()
    balls = scrapy.Field()
    p_throws = scrapy.Field()
    gid = scrapy.Field()
    pdes = scrapy.Field()
    spin = scrapy.Field()
    norm_ht = scrapy.Field()
    inning = scrapy.Field()
    pitcher_team = scrapy.Field()
    tstart = scrapy.Field()
    vystart = scrapy.Field()
    ftime = scrapy.Field()
    pfx_x = scrapy.Field()
    pfx_z = scrapy.Field()
    uncorrected_pfx_x = scrapy.Field()
    uncorrected_pfx_z = scrapy.Field()
    x0 = scrapy.Field()
    y0 = scrapy.Field()
    z0 = scrapy.Field()
    vx0 = scrapy.Field()
    vy0 = scrapy.Field()
    vz0 = scrapy.Field()
    ax = scrapy.Field()
    ay = scrapy.Field()
    az = scrapy.Field()
    start_speed = scrapy.Field()
    px = scrapy.Field()
    pz = scrapy.Field()
    pxold = scrapy.Field()
    pzold = scrapy.Field()
    sb = scrapy.Field()
