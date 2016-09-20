#!/bin/sh
notify-send "Current playing" "`banshee --query-artist`
`banshee --query-album`
`banshee --query-title`"

