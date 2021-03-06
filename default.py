# -*- coding: utf-8 -*-
#------------------------------------------------------------
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.diypowerwall'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID1 = "UC0pBauLp63yzf6sVdEOIUbA"
YOUTUBE_CHANNEL_ID2 = "UCzqf9_I-p-vgOoJrmewEMsg"
YOUTUBE_CHANNEL_ID3 = "UCcMfCkN1juSa49DJFYltOTw"
YOUTUBE_CHANNEL_ID4 = "UCI6ASwT150rendNc5ytYYrQ"
YOUTUBE_CHANNEL_ID5 = "UCBLudMLfVsDbumUJxWIz_WA"
YOUTUBE_CHANNEL_ID6 = "UCZm-Gp9v5KH98bQwkAxyF3w"
YOUTUBE_CHANNEL_ID7 = "UCLKYCkXn8HDEUfIGO2lmCnQ"

# Entry point
def run():
# Get params
	params = plugintools.get_params()

	if params.get("action") is None:
		main_list(params)
	else:
		action = params.get("action")
		exec action+"(params)"

	plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("diypowerwall.main_list "+repr(params))

plugintools.add_item( 
    #action="", 
    title="HBPowerwall",
    url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID1+"/",
    thumbnail=icon,
    folder=True )

plugintools.add_item( 
    #action="", 
    title="UK DIY POWERWALL",
    url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID2+"/",
    thumbnail=icon,
    folder=True )

plugintools.add_item( 
    #action="", 
    title="jehugarcia",
    url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID3+"/",
    thumbnail=icon,
    folder=True )

plugintools.add_item( 
    #action="", 
    title="DIY Tech & Repairs",
    url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID4+"/",
    thumbnail=icon,
    folder=True )

plugintools.add_item( 
    #action="", 
    title="Offgrid Dreaming",
    url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID5+"/",
    thumbnail=icon,
    folder=True )

plugintools.add_item( 
    #action="", 
    title="Colin Hickey",
    url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID6+"/",
    thumbnail=icon,
    folder=True )

plugintools.add_item( 
    #action="", 
    title="Sailing and Electronics",
    url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID7+"/",
    thumbnail=icon,
    folder=True )

run()