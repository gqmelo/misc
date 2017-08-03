function long_command_notify --description 'Show a desktop notification depending on last command duration'
	set -l last_status $status
	if not test $CMD_DURATION; return; end
	if test $CMD_DURATION -gt (math "1000 * 10")
		if test $last_status -ne 0
			set notify_icon 'dialog-error'
		else
			set notify_icon 'emblem-default'
		end
		set secs (math "$CMD_DURATION / 1000")
		switch (uname)
			case Linux
				notify-send -i $notify_icon "$history[1]" "Returned $last_status, took $secs seconds"
			case Darwin
				osascript -e "display notification \"Returned $last_status, took $secs seconds\" with title \"$history[1]\""
		end
		# Avoid repeating the message (when the window is resized for example)
		set -gx CMD_DURATION 0
	end
end
