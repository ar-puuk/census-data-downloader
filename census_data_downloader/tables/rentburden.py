#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class RentBurdenDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "rentburdenaspercentofincome"
    UNIVERSE = "renter-occupied housing units"
    RAW_TABLE_NAME = 'B25070'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '002': "less_than_10_percent",
        '003': "10_to_14.9_percent",
        '004': "15_to_19.9_percent",
        '005': "20_to_24.9_percent",
        '006': "25_to_29.9_percent",
        '007': "30_to_34.9_percent",
        '008': "35_to_39.9_percent",
        '009': "40_to_49.9_percent",
        '010': "50_percent_or_more",
        '011': "not_computed"
    })
