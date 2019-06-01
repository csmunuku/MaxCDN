#!/usr/bin/env python
# AUTHOR: Chandra Munukutla
# Description: script to purge cache for pull zones based on zone_id.
# This is using python 3.7 version
# If we use older python versions, we would encounter few warnings.. about
# SNIMissingWarning and InsecurePlatformWarning
# Also print command changes (for 2.x version of python). Need to adjust those accordingly
# Pre-requisites: python 3.7 or above
#                 All the dependency modules (maxcdn, pp) needs to be installed via pip.
#                 IPs from where we need to run this script needs to be whitelisted in MaxCDN!
################################################################################################
import pprint as pp
from maxcdn import MaxCDN

companyalias = "<my_company_name_here>"
# zone_type would be either pull or push - pull indicates ==> pull zones
zone_type = "pull"

# newly created "Purge-Cache" Application has been created
# with permissions to be able to work with MaxCDN via API.
# Below are the consumer_key and consumer_secret for that.
consumer_key = "<consumer_key_here>"
consumer_secret = "<secret_key_here>"

#zones = [] # pull zones list.. ie., comma seperated pull zone numbers
# pull zone ids list.
zones = [123456,234567]

api = MaxCDN(companyalias, consumer_key, consumer_secret)

for zone_id in zones:
  print("Purging zone: %s" % (zone_id))
  res = api.purge(zone_id)
  try:
    if res["code"] == 200:
        print("SUCCESS!")
    else:
        print("Failed with code: " + res["code"])
        exit(res["code"])
  except KeyError:
        print("Something went terribly wrong!")
        pp.pprint(res)
        exit(1)
