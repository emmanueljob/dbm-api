import unittest
import json

from dbmclient.models.lineitem import Lineitem
from tests.base import Base


class LineitemTest(Base):

    def testGetByAdvertiser(self):
        loader = Lineitem(LineitemTest.conn)
        # test
        # lineitems = loader.find_by_advertiser(601374)
        
        # bacardi
        lineitems = loader.find_by_advertiser(4617)

        for lineitem in lineitems:
            print lineitem.name

#            print "lineitem['id']",lineitem['id']
#            print "lineitem['io_id']",lineitem['io_id']
#            print "lineitem['type']",lineitem['type']
#            print "lineitem['name']",lineitem['name']
#            print "lineitem['timestamp']",lineitem['timestamp']
#            print "lineitem['status']",lineitem['status']
#            print "lineitem['start_date']",lineitem['start_date']
#            print "lineitem['end_date']",lineitem['end_date']
#            print "lineitem['budget_type']",lineitem['budget_type']
#            print "lineitem['budget']",lineitem['budget']
#            print "lineitem['pacing']",lineitem['pacing']
#            print "lineitem['pacing_rate']",lineitem['pacing_rate']
#            print "lineitem['pacing_amount']",lineitem['pacing_amount']
#            print "lineitem['frequency_enabled']",lineitem['frequency_enabled']
#            print "lineitem['frequency_exposures']",lineitem['frequency_exposures']
#            print "lineitem['frequency_period']",lineitem['frequency_period']
#            print "lineitem['frequency_amount']",lineitem['frequency_amount']
#            print "lineitem['partner_revenue_model']",lineitem['partner_revenue_model']
#            print "lineitem['partner_revenue_amount']",lineitem['partner_revenue_amount']
#            print "lineitem['conversion_counting_type']",lineitem['conversion_counting_type']
#            print "lineitem['conversion_counting_pct']",lineitem['conversion_counting_pct']
#            print "lineitem['conversion_pixel_ids']",lineitem['conversion_pixel_ids']
#            print "lineitem['fees']",lineitem['fees']
#            print "lineitem['integration_code']",lineitem['integration_code']
#            print "lineitem['details']",lineitem['details']
#            print "lineitem['bid_strategy_value']",lineitem['bid_strategy_value']
#            print "lineitem['bid_strategy_unit']",lineitem['bid_strategy_unit']
#            print "lineitem['creative_assignments']",lineitem['creative_assignments']
#            print "lineitem['geo_targeting_include']",lineitem['geo_targeting_include']
#            print "lineitem['geo_targeting_exclude']",lineitem['geo_targeting_exclude']
#            print "lineitem['lang_targeting_include']",lineitem['lang_targeting_include']
#            print "lineitem['lang_targeting_exclude']",lineitem['lang_targeting_exclude']
#            print "lineitem['device_targeting_include']",lineitem['device_targeting_include']
#            print "lineitem['device_targeting_exclude']",lineitem['device_targeting_exclude']
#            print "lineitem['browser_targeting_include']",lineitem['browser_targeting_include']
#            print "lineitem['browser_targeting_exclude']",lineitem['browser_targeting_exclude']
#            print "lineitem['brand_safety_sensitivity']",lineitem['brand_safety_sensitivity']
#            print "lineitem['brand_safety_custom']",lineitem['brand_safety_custom']
#            print "lineitem['channel_targeting_include']",lineitem['channel_targeting_include']
#            print "lineitem['channel_targeting_exclude']",lineitem['channel_targeting_exclude']
#            print "lineitem['site_targeting_include']",lineitem['site_targeting_include']
#            print "lineitem['site_targeting_exclude']",lineitem['site_targeting_exclude']
#            print "lineitem['app_targeting_include']",lineitem['app_targeting_include']
#            print "lineitem['app_targeting_exclude']",lineitem['app_targeting_exclude']
#            print "lineitem['cat_targeting_include']",lineitem['cat_targeting_include']
#            print "lineitem['cat_targeting_exclude']",lineitem['cat_targeting_exclude']
#            print "lineitem['keyword_targeting_include']",lineitem['keyword_targeting_include']
#            print "lineitem['keyword_targeting_exclude']",lineitem['keyword_targeting_exclude']
#            print "lineitem['audience_targeting_similar']",lineitem['audience_targeting_similar']
#            print "lineitem['audience_targeting_include']",lineitem['audience_targeting_include']
#            print "lineitem['audience_targeting_exclude']",lineitem['audience_targeting_exclude']
#            print "lineitem['inventory_targeting_include']",lineitem['inventory_targeting_include']
#            print "lineitem['inventory_targeting_exclude']",lineitem['inventory_targeting_exclude']
#            print "lineitem['daypart_targeting']",lineitem['daypart_targeting']
#            print "lineitem['env_targeting']",lineitem['env_targeting']
#            break
#
#            assert lineitem['id'] is not None
#            if lineitem.id == '4711054':
#                print "UPDATING"
#                lineitem.name = "Liz test"
#                # lineitem.save()

        lineitem = lineitems[0]
        #update budget
        
