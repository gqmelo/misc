function ssh_agent_start --description 'Start ssh-agent if necessary and export the variables'
	set CURRENT_PID (pgrep -u $USER ssh-agent)
	if test -z "$SSH_AGENT_PID" -o "$SSH_AGENT_PID" != "$CURRENT_PID"
		echo "Re-starting Agent for $USER"
		pkill -15 -u $USER ssh-agent
		eval (ssh-agent -s | sed 's!export.*!!' | sed 's!SSH_!set -U SSH_!' | tr '=' ' ')
	else
		echo "ssh-agent already running"
	end
end
